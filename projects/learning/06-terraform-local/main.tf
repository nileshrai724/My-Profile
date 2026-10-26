terraform {
  required_version = ">= 1.5.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

resource "local_file" "learning_lab" {
  filename        = "${path.module}/learning-lab.txt"
  content         = "Created by Terraform. No cloud resources were provisioned.\n"
  file_permission = "0644"
}

output "generated_file" {
  description = "Path to the local file created by Terraform."
  value       = local_file.learning_lab.filename
}
