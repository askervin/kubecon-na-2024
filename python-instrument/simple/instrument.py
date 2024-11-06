import runpy
import sys

import lib

def wrapped_callable(f):
    def wrap(*args, **kwargs):
        print("wrap before call")
        rv = f(*args, **kwargs)
        print("wrap after call")
        return rv
    return wrap

lib.func = wrapped_callable(lib.func)

sys.argv.pop(0)
runpy.run_module(sys.argv[0].replace(".py", ""), run_name="__main__")
