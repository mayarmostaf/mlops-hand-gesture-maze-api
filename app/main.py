from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from .schemas import HandLandmarks
from .model import predict_class
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mayarmostaf.github.io",
        "https://mayarmostaf.github.io/MLOPs-Final-Project",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.get("/")
def root():
    logging.info("Root endpoint accessed")
    return {"message": "Hand gesture recognition API is up."}

@app.get("/health")
def health():
    logging.info("Health check endpoint accessed")
    return {"status": "healthy"}

@app.post("/predict")
def predict(input: HandLandmarks):
    logging.info(f"Received landmarks: {input.landmarks}")
    prediction = predict_class(input.landmarks)
    logging.info(f"Prediction result: {prediction}")
    return {"prediction": prediction}
