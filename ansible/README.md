### Ansible installation instructions

```
# Install ansible globally
sudo python3 -m pip install ansible

# Install roles
ansible-galaxy role install geerlingguy.docker geerlingguy.pip weareinteractive.apt

# Run playbooks, install docker-compose on aws
ansible-playbook playbooks/install_docker.yml

```