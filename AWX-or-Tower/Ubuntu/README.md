# Ubuntu Playbooks

This repository contains Ansible playbooks designed for managing and automating tasks on Ubuntu systems.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Playbooks](#playbooks)
- [License](#license)

## Introduction

These playbooks are tailored for Ubuntu environments, providing a streamlined way to configure, deploy, and manage systems.

## Requirements

- Ansible 2.9 or later
- Ubuntu 18.04 or later
- Properly configured SSH access to target machines

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/rioux/Charles-GitHub-1.git
    cd AWX-or-Tower/Ubuntu
    ```

2. Run a playbook:
    ```bash
    ansible-playbook -i inventory playbook.yml
    ```

## Playbooks

- **setup.yml**: Initial system setup and configuration.
- **deploy.yml**: Application deployment tasks.
- **update.yml**: System updates and package management.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.