import faust
from model_management import load_model, predict
from config import load_config

config = load_config()

app = faust.App('faustream', broker=f"kafka://{config['kafka']['broker']}")
model = load_model(config['model']['path'])

class PredictionRequest(faust.Record, serializer='json'):
    id: str
    data: dict

class PredictionResult(faust.Record, serializer='json'):
    id: str
    prediction: float

request_topic = app.topic(config['kafka']['topic'], value_type=PredictionRequest)
prediction_topic = app.topic(config['kafka']['prediction_topic'], value_type=PredictionResult)

@app.agent(request_topic)
async def process(stream):
    async for request in stream:
        result = predict(request.data)
        await prediction_topic.send(value=PredictionResult(id=request.id, prediction=result))
