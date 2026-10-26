FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py .
RUN useradd --system --no-create-home appuser
USER appuser
EXPOSE 8081
CMD ["python", "app.py"]
