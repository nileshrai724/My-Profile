"""Print a small, portable JSON report about the current host."""

import json
import os
import platform
import shutil
import sys
from pathlib import Path


def build_report(path: str = ".") -> dict[str, object]:
    """Build a system report for the filesystem containing path."""
    target = Path(path).expanduser().resolve()
    usage = shutil.disk_usage(target)
    return {
        "hostname": platform.node(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "python_version": platform.python_version(),
        "cpu_count": os.cpu_count(),
        "disk_path": str(target),
        "disk_total_bytes": usage.total,
        "disk_free_bytes": usage.free,
        "disk_used_percent": round((usage.used / usage.total) * 100, 2),
    }


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    try:
        print(json.dumps(build_report(path), indent=2))
    except (OSError, ValueError) as error:
        print(f"Unable to inspect {path!r}: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
