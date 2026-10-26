#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <source-directory> <backup-directory>" >&2
  exit 2
fi

source_dir=$1
backup_dir=$2

if [[ ! -d "$source_dir" ]]; then
  echo "Source directory does not exist: $source_dir" >&2
  exit 1
fi

mkdir -p -- "$backup_dir"
timestamp=$(date -u +"%Y%m%dT%H%M%SZ")
source_name=$(basename -- "${source_dir%/}")
archive="${backup_dir%/}/${source_name}-${timestamp}.tar.gz"

if [[ -e "$archive" ]]; then
  echo "Refusing to overwrite existing archive: $archive" >&2
  exit 1
fi

tar -czf "$archive" -C "$(dirname -- "$source_dir")" "$source_name"
echo "Created backup: $archive"
