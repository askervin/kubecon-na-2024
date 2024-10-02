# instrument - transparently instrument selected functions and run a program
#
# instead of running
#     python3 prog.py ARGS
# run:
#     python3 instrument.py prog.py ARGS

import time
import transformers

calls = {} # key -> list of call timestamps

# wrapper that records new timestamp before calling the original function.
def call_timestamp_wrapper(func, key=None):
    def wrap(*args, **kwargs):
        t = time.time()
        if key not in calls:
            calls[key] = []
        calls[key].append(t)
        return func(*args, **kwargs)
    return wrap

# returned_object_wrapper is a 2nd order wrapper.
# It wraps a method of an object returned by the original function.
def returned_object_wrapper(func, method_name, wrapper, key=None):
    def wrap(*args, **kwargs):
        obj = func(*args, **kwargs)
        setattr(obj, method_name, wrapper(getattr(obj, method_name), key=key))
        return obj
    return wrap

# wrap TextStreamer so that the "put" method of the returned streamer
# object gets wrapped in the call_timestamp_wrapper.
transformers.TextStreamer = returned_object_wrapper(
    transformers.TextStreamer,
    "put",
    call_timestamp_wrapper,
    key="streamer.put")


if __name__ == "__main__":
    import pprint
    import sys
    import runpy

    # run the main program
    sys.argv.pop(0)
    main_module = sys.argv[0]
    if main_module.endswith(".py"):
        main_module = main_module[:-len(".py")]
    runpy.run_module(main_module, run_name="__main__")

    # print recorded call timestamps
    pprint.pprint(calls)
