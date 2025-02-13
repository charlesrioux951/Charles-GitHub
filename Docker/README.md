# Docker on Linux

## Introduction
This guide provides an overview of how to install and use Docker on a Linux system.  
There will be a section on "rootless" container/Docker. This was created on some  
security flaws on containers. One can become root on the base server... I wont tell how :-) 

## Prerequisites
- A Linux-based operating system
- Sudo privileges

## Installation

### Step 1: Update Your System
```bash
sudo apt-get update
```

### Step 2: Install Docker
```bash
sudo apt-get install docker.io
```

### Step 3: Start and Enable Docker
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 4: Verify Installation
```bash
docker --version
```

## Basic Usage

### Pull an Image
```bash
docker pull ubuntu
```

### Run a Container
```bash
docker run -it ubuntu
```

### List Running Containers
```bash
docker ps
```

### Stop a Container
```bash
docker stop <container_id>
```

## Conclusion
You have successfully installed and started using Docker on your Linux system. For more detailed information, refer to the [official Docker documentation](https://docs.docker.com/).
