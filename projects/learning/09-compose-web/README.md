# 9. Docker Compose web app

Run a small Python web service with Docker Compose. Compose builds the image,
publishes port 8081, and checks its health endpoint.

## Run

Requires Docker Desktop with Compose:

```bash
docker compose up --build
```

Visit `http://localhost:8081/health`. Stop and remove the container with
Ctrl+C, then `docker compose down`.

## Try next

Add a reverse proxy or a second service, then make the app depend on a healthy
service rather than relying on startup timing.
