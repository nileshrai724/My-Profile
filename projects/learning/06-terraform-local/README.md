# 6. Terraform local artifact

Use Terraform to generate a small text file locally. This demonstrates
variables, a provider, a resource, and outputs without creating cloud
resources.

## Run

Requires Terraform:

```bash
terraform init
terraform plan
terraform apply
```

Review the plan first. `apply` writes `learning-lab.txt` in this project.
Remove it with `terraform destroy` when finished.

## Try next

Add variables for the message and filename, or generate a local configuration
file from a template.
