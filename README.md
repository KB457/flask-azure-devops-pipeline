# 🚀 Flask App CI/CD on Azure using Terraform, Docker & GitHub Actions

This project demonstrates a full DevOps pipeline where a Flask application is:

- Containerized with **Docker**
- Pushed to **Azure Container Registry (ACR)** using **GitHub Actions**
- Deployed to **Azure Linux Web App**
- Infrastructure provisioned with **Terraform**

## 🧱 Tech Stack
- Terraform (IaC)
- Docker
- GitHub Actions (CI/CD)
- Azure Container Registry (ACR)
- Azure App Service (Linux)
- Python + Flask

## 🔁 Workflow Overview

1. `terraform apply` sets up ACR and App Service.
2. GitHub Actions automatically builds and pushes the Docker image to ACR on every push.
3. Azure Web App pulls and runs the latest container.

## 📂 Folder Structure

├── docker/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── terraform/
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   └── outputs.tf
├── .github/
│   └── workflows/
│       └── docker-deploy.yml
├── .gitignore
└── README.md



## 🚀 Result

Live deployed Flask app: **Hello from Flask on Azure!**  
Delivered using a production-style CI/CD DevOps pipeline.