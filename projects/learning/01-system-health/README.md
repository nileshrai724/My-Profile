# 1. System health report

Print a JSON snapshot of the current operating system, Python version, CPU
count, and free/total disk space.

## Run

Requires Python 3.10+; uses only the standard library.

```bash
python health_report.py
```

Optional: provide a path to inspect a different mounted disk.

```bash
python health_report.py .
```

Run the tests from this directory with `python -m unittest`.

## Try next

Add memory information, warn when free disk space falls below a threshold, or
write timestamped reports to a file.
