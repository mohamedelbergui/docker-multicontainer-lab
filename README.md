# 🐳 Docker Multi-Container Lab

## 📝 About This Project

This project is a hands-on lab designed to **learn and master Docker, Docker Compose, and multi-container architecture**. The main objective was to containerize a complete web application, manage inter-container communication within an isolated Docker network, and apply security best practices (privilege separation and secret management through environment variables).

---

## 🏗️ Project Architecture

The infrastructure is divided into three distinct microservices that communicate with each other:

* **Reverse Proxy (Nginx):** The single entry point of the application. It handles incoming requests and forwards them to the API.
* **Backend API (Flask / Python):** Processes business logic, exposes the REST API, and communicates with the database using the `psycopg2` driver.
* **Database (PostgreSQL):** Persistently stores application user data.

---

## 🚀 Installation & Deployment

Follow these steps to clone and run the project locally in just a few seconds.

### 1. Clone the Repository

```bash
git clone <github-repository-url>
cd DockerProject
```

### 2. Configure Environment Variables

For security reasons, database credentials are not publicly shared. Create your own `.env` file at the project root based on the provided template:

```bash
cp .env-example .env
```

Open the newly created `.env` file and define your database username, password, and database name.

### 3. Deploy the Infrastructure with Docker Compose

Build the images and start all containers:

```bash
docker compose up --build
```

To stop and remove the containers:

```bash
docker compose down
```

---

## 🛣️ API Routes & Features

Once the infrastructure is running, the application exposes the following endpoints:

| Route    | Method | Description                    | Return Type                 |
| -------- | ------ | ------------------------------ | --------------------------- |
| `/`      | GET    | Application entry point        | Plain Text (Hello World) 🌐 |
| `/users` | GET    | Retrieve all users             | JSON (Array) 📊             |
| `/users` | POST   | Add a new user to the database | JSON (Success Message) 📥   |

---

## 🛠️ DevOps Skills Demonstrated in This Lab

* **Application Containerization:** Writing optimized Dockerfiles.
* **Local Orchestration:** Using Docker Compose to connect multiple services (App, Database, Proxy).
* **Docker Networking:** Secure isolation and communication between containers.
* **Secrets Management:** Handling sensitive configurations through a `.env` file excluded from Git using `.gitignore`.
