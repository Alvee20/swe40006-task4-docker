# SWE40006 Task 4: Containerised Flask Web App

A simple Python Flask web application, containerised with Docker, published to Docker Hub as a multi-architecture image, and deployed on two separate Docker hosts.

**Unit:** SWE40006 Software Deployment and Evolution

**Target level:** Task 4.1 (Pass) and Task 4.2 (Credit)

## Links

| Item | Link |
|---|---|
| Docker Hub image | https://hub.docker.com/r/alvee20/swe40006-flask |
| Live deployment (AWS EC2) | http://52.62.50.28:8080 |

## Files

| File | Purpose |
|---|---|
| `app.py` | Flask app. Listens on `0.0.0.0` (port 5000 by default, overridable with the `PORT` environment variable) and displays the container ID that served the request. |
| `requirements.txt` | Python dependencies (Flask 3.1.0). |
| `Dockerfile` | Builds the image from `python:3.12-slim`, installs dependencies, then copies the app. |

## Run locally

```bash
docker build -t swe40006-flask:1.0 .
docker run -d -p 8080:5000 --name flask-local swe40006-flask:1.0
```

Open http://localhost:8080.

Host port 8080 is used because port 5000 is reserved by AirPlay Receiver on macOS.

## Build and push a multi-architecture image

The image was built on an Apple Silicon Mac (arm64) but deployed to an x86_64 EC2 instance, so it is published for both architectures:

```bash
docker login
docker buildx build --platform linux/amd64,linux/arm64 \
  -t alvee20/swe40006-flask:1.0 --push .
```

## Run on any Docker host

```bash
docker pull alvee20/swe40006-flask:1.0
docker run -d -p 8080:5000 --restart unless-stopped \
  --name flask-ec2 alvee20/swe40006-flask:1.0
```

Docker automatically pulls the variant that matches the host's CPU architecture.

## Deployment environments

| Host | Architecture | Docker |
|---|---|---|
| MacBook Air M2 (local) | linux/arm64 | Docker Desktop 4.93.0 (Engine 29.8.1) |
| AWS EC2 t3.micro, Amazon Linux 2023 (Sydney) | linux/amd64 | Docker Engine 25.0.14 |
