# 5. GitHub Actions Python CI

Run the system-health project's unit tests automatically when changes are
pushed or a pull request is opened. The workflow uses GitHub-hosted runners
and does not deploy or access cloud resources.

## Run locally

```bash
cd ../01-system-health
python -m unittest
```

## Try next

Add a Python-version matrix, linting, or a coverage report. Keep deployment
steps separate and require explicit approvals for production environments.
