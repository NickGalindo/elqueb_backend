import json
import requests
from time import sleep

from colorama import Fore
import colorama

colorama.init(autoreset=True)

with open("./data_push/ofertas.json", "r") as file:
    data = json.load(file)

for i in data:
    i["ofertaid"] = str(i["ofertaid"])
    res = requests.post("http://localhost:8000/ofertas/addOferta", json=i)
    print(i)
    print(Fore.GREEN + str(res.status_code))
    sleep(1)
    
