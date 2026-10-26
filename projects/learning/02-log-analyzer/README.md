# 2. Log analyzer

Summarize a simple web-server access log, counting total requests, HTTP status
codes, and the most frequent client addresses.

## Run

Requires Python 3.10+; uses only the standard library.

```bash
python log_analyzer.py sample.log
```

Pass another log file as the first argument. Unrecognized lines are counted
instead of silently discarded.

## Try next

Add time-range filters, JSON output, or support for your server's log format.
