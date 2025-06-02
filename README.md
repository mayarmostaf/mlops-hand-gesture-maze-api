# Hand Gesture Recognition API

This repository serves a hand gesture classification model through a **FastAPI** backend. The API receives hand landmarks (from MediaPipe), applies preprocessing, and returns a predicted class. This project also includes unit testing, Docker containerization, monitoring with Prometheus + Grafana, and deployment setup.

---

## 🚀 Features

* **Model Serving**: FastAPI-based REST API
* **Unit Testing**: With `pytest`
* **Containerization**: Using Docker and Docker Compose
* **Monitoring**: Prometheus & Grafana for metrics visualization
* **Deployment**: Docker Compose setup for deployment on platforms like ClawCloud, AWS EC2, etc.

---

## 🔧 Endpoints

| Endpoint   | Method | Description                            |
| ---------- | ------ | -------------------------------------- |
| `/`        | GET    | Health check root                      |
| `/health`  | GET    | API health status                      |
| `/predict` | POST   | Accepts hand landmarks & returns class |

**Example Input** (42 floats for x1-y21):

```json
{
  "landmarks": [0.1, 0.2, ..., 0.98, 0.99]  // length: 42
}
```

**Example Output**:

```json
{
  "prediction": "Thumbs Up"
}
```

---

## 📈 Monitoring Metrics

We collect and visualize the following:

| Type           | Metric                          | Reason                                                       |
| -------------- | ------------------------------- | ------------------------------------------------------------ |
| Model-related  | `model_latency_95th_percentile` | Monitor prediction speed under load                          |
| Data-related   | `request_count_by_input_size`   | Detect unusual input patterns or API misuse                  |
| Server-related | `cpu_usage`, `memory_usage`     | Ensure the system is performing well without overutilization |

### Grafana Dashboard Screenshots

![Graphana_whole_dashboard](https://github.com/user-attachments/assets/1ef92aab-5ae5-4355-9148-445d6b69ea81)
![graphana_dashboard_part1](https://github.com/user-attachments/assets/3c7fe3f5-b2b5-4396-95ad-afa70850149d)
![graphana_dashboard_part2](https://github.com/user-attachments/assets/77f7b5cb-5a70-40ea-9c8c-90063c62acf5)


---

## 🛋️ Docker Setup

**Run the whole system (API + Prometheus + Grafana)**:

```bash
docker-compose up --build
```

API will be available at: [http://localhost:8000](http://localhost:8000)

Prometheus at: [http://localhost:9090](http://localhost:9090)
Grafana at: [http://localhost:3000](http://localhost:3000)

---

## 🗭 Unit Testing

Tests are written using `pytest`. To run the tests:

```bash
pytest test_main.py
```

---

## 🛠️ Deployment

The project is deployed on:

* **railway** (Free \$5 credit)


Deployment steps:

1. Clone the repository.
2. Set up a cloud VM or platform.
3. Copy `docker-compose.yml` & project files to the server.
4. Run `docker-compose up -d`
5. Monitor via Grafana dashboard.

---

## 📁 Project Structure

```bash
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── __pycache__
│   ├── schemas.py
│   └── utils.py
├── bin
│   ├── best_xgb_model.pkl
│   └── target_encoder.pkl
├── docker-compose.yml
├── Dockerfile
├── prometheus.yml
├── __pycache__
│   ├── Application.cpython-310.pyc
│   ├── test_app.cpython-310-pytest-8.3.5.pyc
│   └── test_main.cpython-310-pytest-8.3.5.pyc
├── README.md
├── requirements.txt
├── screens
│   ├── graphana_dashboard_part1.png
│   ├── graphana_dashboard_part2.png
│   ├── Graphana_whole_dashboard.png
│   ├── pytest.png
│   ├── railway_deployment_part1.png
│   ├── railway_deployment_part2.png
│   ├── railway_deployment_part3.png
│   ├── swagger.png
│   ├── swagger_predict.png
│   ├── workflow_part1.png
│   └── workflow_part2.png
└── test_main.py
```

---

## 🙌 Acknowledgements

* Built with [FastAPI](https://fastapi.tiangolo.com/), [Prometheus](https://prometheus.io/), and [Grafana](https://grafana.com/)
* Model trained using [XGBoost](https://xgboost.readthedocs.io/)
* MediaPipe for hand landmark detection (not included here)

---

## 📆 Status

**Production** ✅ – deployed, tested, and monitored.

---
