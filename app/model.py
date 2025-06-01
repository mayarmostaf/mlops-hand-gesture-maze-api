import os
import joblib
from .utils import preprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(script_dir, "../bin/best_xgb_model.pkl")
label_encoder_path = os.path.join(script_dir, "../bin/target_encoder.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(label_encoder_path)

def predict_class(landmarks):
    df = preprocess(landmarks)
    pred = model.predict(df)
    return label_encoder.inverse_transform(pred)[0]
