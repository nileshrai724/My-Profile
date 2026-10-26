# 4. Containerized health API

A tiny HTTP service with `/health` and `/` endpoints, packaged as a
non-root Docker container with a Docker health check.

## Run

Requires Docker:

```bash
docker build -t devops-health-api .
docker run --rm -p 8080:8080 devops-health-api
```

Open `http://localhost:8080/health` in a browser or use `curl`. Stop the
container with Ctrl+C.

## Try next

Add a `/version` endpoint, structured request logs, or a test stage in a
multi-stage Docker build.
