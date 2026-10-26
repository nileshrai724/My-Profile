# 3. Timestamped backup script

Create a compressed archive of a source directory. The script requires an
explicit destination directory and refuses to overwrite an existing archive.

## Run

Run with Bash on Linux, macOS, or WSL:

```bash
bash backup.sh ./my-folder ./backups
```

The destination directory is created when needed. Review the script and make
sure the destination has enough space before backing up large folders.

## Try next

Add retention cleanup, checksum verification, or an exclusion-file option.
