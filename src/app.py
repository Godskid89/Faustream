import faust
from src import model_management
from src import config
from src import utils
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

config = config.load_config()

app = faust.App('faustream', broker=f"kafka://{config['kafka']['broker']}", loglevel='info')
model = model_management.load_model(config['model']['path'])

class PredictionRequest(faust.Record, serializer='json'):
    id: str
    data: dict

class PredictionResult(faust.Record, serializer='json'):
    id: str
    prediction: str

request_topic = app.topic(config['kafka']['topic'], value_type=PredictionRequest)
print(f"Request Topic is {request_topic}.")
prediction_topic = app.topic(config['kafka']['prediction_topic'], value_type=PredictionResult)
print(f"Prediction Topic is {prediction_topic}.")

@app.agent(request_topic)
async def process(stream):
    async for request in stream:
        print(f"The request is {request}.")
        data_access_path = config['data_access']['path']
        text_to_predict = utils.get_data_from_path(request, data_access_path) or ''
        result = model_management.predict(text_to_predict)
        logging.info(f"The result is {result}")

        print(f"The result is {result}.")
        await prediction_topic.send(value=PredictionResult(id=request.id, prediction=result))
        print(f"Successfully sent prediction for request ID {request.id} to prediction topic.")
        logging.info(f"Successfully sent prediction for request ID {request.id} to prediction topic.")


