# 10. Prometheus metrics exporter

Expose a Prometheus-compatible metric showing the exporter's process uptime,
then scrape it with a local Prometheus container.

## Run

Requires Docker Desktop with Compose:

```bash
docker compose up --build
```

- Metrics: `http://localhost:8000/metrics`
- Prometheus: `http://localhost:9090`

In Prometheus, query `learning_exporter_uptime_seconds`. Stop with Ctrl+C and
run `docker compose down`.

## Try next

Add request counters, document metric names, and create a Grafana dashboard.
Avoid exposing real infrastructure or sensitive data through public metrics.
