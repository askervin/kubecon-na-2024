Example of instrumenting code without changing a program or a library

Run mychat.py without instrumentation.
```
python3 mychat.py
```

Instrument streamer.put(), run mychat.py, and print put() timestamps.
```
python3 instrument.py mychat.py
```

This example is part of the KubeCon NA 2024 talk:
Platform Performance Optimization for AI
by Dixita Narang and Antti Kervinen.
[talk](https://sched.co/1i7m0)
[slides](https://docs.google.com/presentation/d/1lqjjpbUAsCf3muFf9YWN5HGwwHB3XxBJmX2-C7JP41k/)
