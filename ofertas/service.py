from typing import List
from manager.load_config import CONFIG

import requests
from pymongo import MongoClient

from ofertas.models import Oferta, SemanticSearchTerms

def addOferta(oferta: Oferta, mongodb: MongoClient):
    ofertasCol = mongodb.db.ofertas

    ofertasCol.insert_one({
        "_id": oferta.ofertaid,
        "title": oferta.title,
        "description": oferta.description,
        "category": oferta.category,
        "region": oferta.region,
        "ofertante": oferta.ofertante
    })

    json_payload = {
        "ofertaid": oferta.ofertaid,
        "oferta": oferta.title + "\n" + oferta.description,
        "category": oferta.category,
        "region": oferta.region
    }

    resp = requests.post(CONFIG["AI_HOST"]+"/addOferta", json=json_payload)

    print(resp.status_code)

    return True

def deleteOferta(ofertaid: str, mongodb: MongoClient):
    resp = requests.get(CONFIG["AI_HOST"]+f"/deleteOferta/{ofertaid}")
    res = mongodb.db.ofertas.delete_one({"_id": ofertaid})
    return True

def getOferta(ofertaid: str, mongodb: MongoClient):
    oferta = mongodb.db.ofertas.find_one({"_id": ofertaid})
    return oferta

def semanticSearch(search_terms: SemanticSearchTerms, mongodb: MongoClient):
    resp = requests.post(CONFIG["AI_HOST"]+f"/semanticSearch", json=search_terms.__dict__)
    res = mongodb.db.ofertas.find({"_id": {"$in": resp.json()}})

    search_res: List[Oferta] = []
    for i in res:
        search_res.append(Oferta(
            ofertaid=i["_id"],
            title=i["title"],
            description=i["description"],
            category=i["category"],
            region=i["region"],
            ofertante=i["ofertante"]
        ))

    return search_res

def recommendOfertas(userid: str, mongodb: MongoClient):
    usr = mongodb.db.users.find_one({"_id": userid})

    if usr is None:
        return []

    resp = requests.post(CONFIG["AI_HOST"]+f"/recommendOfertas", json=usr["history"])
    res = mongodb.db.ofertas.find({"_id": {"$in": resp.json()}})

    search_res: List[Oferta] = []
    for i in res:
        search_res.append(Oferta(
            ofertaid=i["_id"],
            title=i["title"],
            description=i["description"],
            category=i["category"],
            region=i["region"],
            ofertante=i["ofertante"]
        ))

    return search_res

def queryOfertas(category: str | None, region: str | None, ofertante: str | None, mongodb: MongoClient):
    query = {}

    if category:
        query["category"] = category
    if region:
        query["region"] = region
    if ofertante:
        query["ofertante"] = ofertante

    res = mongodb.db.ofertas.find(query)

    results: List[Oferta] = []
    
    for i in res:
        results.append(Oferta(
            ofertaid=i["_id"],
            title=i["title"],
            description=i["description"],
            category=i["category"],
            region=i["region"],
            ofertante=i["ofertante"]
        ))

    return results
