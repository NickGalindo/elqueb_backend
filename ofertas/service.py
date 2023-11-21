from manager.load_config import CONFIG

import requests
from pymongo import MongoClient

from ofertas.models import Oferta

def addOferta(oferta: Oferta, mongodb: MongoClient):
    ofertasCol = mongodb.db.ofertas

    ofertasCol.insert_one({
        "_id": oferta.ofertaid,
        "oferta": oferta.oferta,
        "category": oferta.category,
        "region": oferta.region,
        "ofertante": oferta.ofertante
    })

    json_payload = {
        "ofertaid": oferta.ofertaid,
        "oferta": oferta.oferta,
        "category": oferta.category,
        "region": oferta.region
    }

    resp = requests.post(CONFIG["AI_HOST"]+"/addOferta", json=json_payload)

    print(resp.status_code)

    return True

def deleteOferta(ofertaid: )
