Example of instrumenting code without changing a program or a library

Run mychat.py without instrumentation.
```
python3 mychat.py
```

Instrument streamer.put(), run mychat.py, and print put() timestamps.
```
python3 instrument.py mychat.py
```
