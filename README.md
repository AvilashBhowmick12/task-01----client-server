# Client-Server Project

## Overview

This project is a client-server application built using Docker and Kubernetes. It demonstrates how to create, deploy, and manage microservices in a containerized environment.

## Features

- **Client**: A user interface for interacting with the server.
- **Server 01**: Handles specific requests and processes data.
- **Server 02**: Provides additional functionalities and services.
- **Kubernetes**: Orchestrates the deployment and scaling of services.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Kubernetes](https://kubernetes.io/docs/setup/) cluster set up.
- [kubectl](https://kubernetes.io/docs/tasks/tools/) command-line tool installed.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AvilashBhowmick12/client-server-project.git
   cd client-server-project

2. Build Docker images:

    ```bash
    cd client
    docker build -t your-client-image .
    cd ../server01
    docker build -t your-server01-image .
    cd ../server02
    docker build -t your-server02-image .

3. Deploy to Kubernetes:

    ```bash
    cd k8s
    kubectl apply -f deployment.yaml

4. Expose the client service:

    ```bash
    kubectl expose deployment client --type=LoadBalancer --port=80

5. Get the external IP:

    ```bash
    kubectl get services

6. Access the client application via the external IP in your web browser.

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
[Docker](https://www.docker.com/)
[Kubernetes](https://kubernetes.io/)