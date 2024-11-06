Example of instrumenting simple library without changing the main
program or the library

Run main.py without instrumentation.
```
python3 main.py
```

Wrap instrumentation code around func() in lib.py and run the main program.
```
python3 instrument.py main.py
```
