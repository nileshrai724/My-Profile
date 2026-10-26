"""Summarize common fields in an Nginx/Apache-style access log."""

import collections
import re
import sys
from pathlib import Path

LOG_PATTERN = re.compile(
    r'^(?P<client>\S+) \S+ \S+ \[[^]]+\] '
    r'"(?P<request>[^"]*)" (?P<status>\d{3}) \S+'
)


def analyze(lines: list[str]) -> dict[str, object]:
    statuses: collections.Counter[str] = collections.Counter()
    clients: collections.Counter[str] = collections.Counter()
    total = malformed = 0

    for line in lines:
        match = LOG_PATTERN.match(line)
        if not match:
            malformed += 1
            continue
        total += 1
        statuses[match.group("status")] += 1
        clients[match.group("client")] += 1

    return {
        "requests": total,
        "malformed_lines": malformed,
        "status_codes": dict(sorted(statuses.items())),
        "top_clients": clients.most_common(5),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(sys.argv[0]).name} <log-file>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        report = analyze(path.read_text(encoding="utf-8").splitlines())
    except OSError as error:
        print(f"Unable to read {path}: {error}", file=sys.stderr)
        return 1

    print(f"Requests: {report['requests']}")
    print(f"Malformed lines: {report['malformed_lines']}")
    print(f"Status codes: {report['status_codes']}")
    print(f"Top clients: {report['top_clients']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
