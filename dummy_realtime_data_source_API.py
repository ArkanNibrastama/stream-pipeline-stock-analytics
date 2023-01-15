import json
import requests
from random import randint
from datetime import datetime
from credentials import API_KEY

def initialization():

    conn = requests.get(f"https://api.goapi.id/v1/stock/idx/companies?api_key={API_KEY}")
    get = conn.text
    data_emiten = json.loads(get)
    emiten_list = [emiten["ticker"] for emiten in data_emiten["data"]["results"]]
    
    return emiten_list


def get_data(emiten_list):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " WIB"
    emiten = emiten_list[randint(0, len(emiten_list)-1)]
    price = randint(50, 2000)

    data = {

        "time" : time,
        "stock code" : emiten,
        "current price" : price

    }

    return data