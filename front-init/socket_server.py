from socket import socket, AF_INET, SOCK_DGRAM
import json
import pickle
from datetime import datetime

def run_server():
    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.bind(('localhost', 5000))
        while True:
            data, _= sock.recvfrom(1024)
            data_dict = pickle.loads(data)
            save_to_json(data_dict)

def save_to_json(data_dict):
    time = data_dict['time']
    with open('storage/data.json', 'r+') as f:
        existed_data = json.load(f)
        existed_data[time] = {
            'username': data_dict['name'], 
            'message': data_dict['message']
        }
        f.seek(0)
        json.dump(existed_data, f, indent=2)
        
if __name__ == '__main__':
    run_server()

