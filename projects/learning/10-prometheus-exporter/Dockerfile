FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY exporter.py .
RUN useradd --system --no-create-home appuser
USER appuser
EXPOSE 8000
CMD ["python", "exporter.py"]
