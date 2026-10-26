"""Expose a simple process-uptime metric for Prometheus."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
import time

STARTED_AT = time.monotonic()


class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_error(404, "Try /metrics")
            return

        uptime = time.monotonic() - STARTED_AT
        body = (
            "# HELP learning_exporter_uptime_seconds Exporter process uptime.\n"
            "# TYPE learning_exporter_uptime_seconds gauge\n"
            f"learning_exporter_uptime_seconds {uptime:.2f}\n"
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args), flush=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    ThreadingHTTPServer(("0.0.0.0", port), MetricsHandler).serve_forever()
