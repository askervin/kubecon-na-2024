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

This example is part of the KubeCon NA 2024 talk:
Platform Performance Optimization for AI
by Dixita Narang and Antti Kervinen.
[talk](https://sched.co/1i7m0)
[slides](https://docs.google.com/presentation/d/1lqjjpbUAsCf3muFf9YWN5HGwwHB3XxBJmX2-C7JP41k/)
