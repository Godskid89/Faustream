import os
import joblib
from datetime import datetime


model_instance = None
last_loaded_timestamp = None
model_path = None

def load_model(path):
    global model_instance, last_loaded_timestamp, model_path
    model_instance = joblib.load(path)
    last_loaded_timestamp = datetime.now()
    model_path = path

def predict(data):
    if model_instance is None:
        raise ValueError("Model not loaded")
    check_and_reload_model()
    return model_instance.predict([data])[0]

def get_model_last_modified_time(path):
    return datetime.fromtimestamp(os.path.getmtime(path))

def check_and_reload_model():
    global last_loaded_timestamp
    if model_path is None:
        return
    last_modified = get_model_last_modified_time(model_path)
    if last_modified > last_loaded_timestamp:
        load_model(model_path)
