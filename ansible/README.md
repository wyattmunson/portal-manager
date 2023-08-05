# Ansible

Ansible rocks.

## Prerequisites

In theory, on a fresh Ubuntu install, `git` and `ansible` are the only prerequisite apt packages needed for portal-manager and Ansible. Ansible will install all other requirements needed by portal-manager.

```bash
sudo apt update
sudo apt install git -y
sudo apt install ansible -y
git clone https://github.com/wyattmunson/portal-manager ~
```

## Running

These packages are configured to run locally on the host machine.

```bash
ansible-playbook k01-install-packages.yml
```
