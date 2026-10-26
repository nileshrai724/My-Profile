# 7. Ansible localhost facts

Run a read-only Ansible playbook that gathers facts from the local machine and
prints a small selection. It does not install packages or change system files.

## Run

Requires Ansible on Linux, macOS, or WSL:

```bash
ansible-playbook -i inventory.ini site.yml
```

## Try next

Add another read-only task, such as checking available disk space. Before
adding tasks that change a machine, understand their effects and test in a
disposable environment.
