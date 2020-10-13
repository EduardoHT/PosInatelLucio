import paho.mqtt.client as mqtt
import json
from datetime import datetime

print("Conectando ao MQTT Broker...")
mqtt_client = mqtt.Client()
mqtt_client.connect('localhost', 1883)

from pynput import keyboard

count = 0

def on_press(key):
    global count
    # Registra data e hora de novos usuários
    data = datetime.now().strftime('%Y-%m-%d')
    hora = datetime.now().strftime('%H: %M: %S')
    if key == keyboard.Key.enter:
        count += 1
        print(count)
        mensagem = {
            'Movimento': 'Entrando',
            'Total': count,
            'Data': data,
            'Hora': hora
        }
        mqtt_client.publish('in242', json.dumps(mensagem))
    elif key == keyboard.Key.space:
        count -= 1
        print(count)
        mensagem = {
            'Movimento': 'Saindo',
            'Total': count
        }
        mqtt_client.publish('in242', json.dumps(mensagem))

def main():
    with keyboard.Listener(on_press=on_press) as listener:
         listener.join()

if __name__ == '__main__':
    main()