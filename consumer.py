import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import datetime

mongo_client = MongoClient('localhost',27018)
mongo_db = mongo_client['in242']
mongo_collection = mongo_db['count']

def msg_recebida(mqtt_client, obj, msg):
    print('Recebendo mensagem...')
    print(msg.payload)
    msg_formatada = json.loads(msg.payload)
    msg_formatada['data_coleta'] = datetime.datetime.now()
    mongo_collection.insert_one(msg_formatada)
    print('Mensagem inserida...')

print('Conectando ao Broker MQTT...')
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost', 1883)
mqtt_client.on_message = msg_recebida
mqtt_client.subscribe('in242')
mqtt_client.loop_forever()


