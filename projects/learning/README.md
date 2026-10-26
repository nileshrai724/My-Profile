# DevOps Learning Lab: 10 Hands-on Projects

Ten small projects for practicing common DevOps skills. Start with the Python
examples; continue into containers, CI/CD, infrastructure, orchestration, and
monitoring. Each project is intentionally small enough to understand and extend.

> **Safety:** Projects that use Docker, Terraform, Ansible, or Kubernetes are
> examples. Review their files before running them. Terraform writes only a
> local file; Ansible gathers facts from localhost; Kubernetes manifests are
> not applied automatically.

| # | Project | What you'll practice | Start here |
|---|---|---|---|
| 1 | System health report | Python, JSON, host and disk information, unit tests | [01-system-health](./01-system-health/) |
| 2 | Log analyzer | Python, regular expressions, command-line arguments | [02-log-analyzer](./02-log-analyzer/) |
| 3 | Timestamped backup | Bash, archives, input validation | [03-backup-script](./03-backup-script/) |
| 4 | Containerized health API | Python HTTP server, Docker, health checks | [04-docker-health-api](./04-docker-health-api/) |
| 5 | Python CI workflow | GitHub Actions, automated tests | [05-github-actions-ci](./05-github-actions-ci/) |
| 6 | Local Terraform artifact | Terraform, variables, outputs, local provider | [06-terraform-local](./06-terraform-local/) |
| 7 | Ansible localhost facts | Ansible inventory, playbooks, facts | [07-ansible-facts](./07-ansible-facts/) |
| 8 | Kubernetes web deployment | Pods, Deployments, Services, resource limits | [08-kubernetes-web/](./08-kubernetes-web/) |
| 9 | Docker Compose web app | Multi-container development, health checks | [09-compose-web/](./09-compose-web/) |
| 10 | Prometheus metrics exporter | Python metrics endpoint, Prometheus scrape config | [10-prometheus-exporter/](./10-prometheus-exporter/) |

## Suggested order

1. Run projects 1 and 2 with Python 3.10 or later.
2. Run project 3 in Bash (Linux, macOS, or WSL).
3. Install Docker Desktop for projects 4 and 9.
4. Push the repository to GitHub to see project 5 run automatically.
5. Install Terraform and Ansible to try projects 6 and 7.
6. Use a local Kubernetes cluster such as kind or minikube for project 8.
7. Run project 10 with Docker Compose and open Prometheus at `http://localhost:9090`.

Every project has its own README with commands and ideas for extending it.
