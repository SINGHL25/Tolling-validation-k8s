# Tolling-validation-k8s
Tolling Validation Microservices Demo (K8s-ready, Docker-compose local)
Tolling-validation-k8s Demo

This is a containerized demo project simulating a tolling system validation pipeline with FastAPI microservices, a Streamlit dashboard, and lightweight JSON-based storage. It is built to demonstrate a modular tolling architecture that can later be deployed to Kubernetes (k8s).

🚦 Features

Plate Ingestion Service (FastAPI)
Accepts vehicle plate input and stores it in JSON DB.

Classification Service (FastAPI)
Classifies a plate as valid/invalid (simple rule-based logic for demo).

Streamlit Dashboard
Web-based UI to view plates, classify them, and track status.

JSON DB
Lightweight JSON files act as a database for demo purposes.

Dockerized Services
All services are containerized and orchestrated with docker-compose.

📂 Project Structure
tolling-validation-k8s/
│── docker-compose.yml
│── README.md
│
├── ingestion_service/
│   ├── app.py               # FastAPI plate ingestion service
│   ├── requirements.txt     # Dependencies
│   └── Dockerfile
│
├── classification_service/
│   ├── app.py               # FastAPI classification service
│   ├── requirements.txt
│   └── Dockerfile
│
├── dashboard/
│   ├── app.py               # Streamlit dashboard
│   ├── requirements.txt
│   └── Dockerfile
│
└── data/
    └── plates.json          # JSON database file
⚡ Quick Start

Clone the project

git clone https://github.com/yourusername/tolling-validation-k8s.git
cd tolling-validation-k8s

Start with Docker Compose

docker-compose up --build

Access Services:

Plate Ingestion API → http://localhost:8001/docs

Classification API → http://localhost:8002/docs

Streamlit Dashboard → http://localhost:8501

🧪 Example Usage

Use the Plate Ingestion API to add a plate:

curl -X POST "http://localhost:8001/ingest" -H "Content-Type: application/json" -d '{"plate": "ABC123"}'

Go to Streamlit Dashboard → see the ingested plate.

Classify it via dashboard → Result shown as valid/invalid.

🚀 Deployment to Kubernetes

This demo can be extended with:

Helm charts or k8s manifests (Deployment, Service, Ingress).

ConfigMaps/Secrets for externalized config.

Persistent Volumes for database storage.

(Optional k8s manifests will be added in the next update.)

📦 Tech Stack

Python 3.10

FastAPI → Microservices

Streamlit → Dashboard

Docker & Docker Compose → Container orchestration

🔮 Roadmap




🤝 Contributing

PRs and issues are welcome! Fork, improve, and submit a PR.

📝 License

MIT License. Free to use, modify, and distribute.
