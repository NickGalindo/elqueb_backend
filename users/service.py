from typing import Dict
from pymongo import MongoClient

def addUser(userid: str, username: str, mongodb: MongoClient):
    usersCol = mongodb.db.users
    usersCol.insert_one({"_id": userid, "name": username, "history": []})

    return True

def getUser(userid: str, mongodb: MongoClient) -> Dict:
    usr = mongodb.db.users.find_one({"_id": userid})
    assert(usr is not None)
    return usr

def deleteUser(userid: str, mongodb: MongoClient) -> bool:
    res = mongodb.db.users.delete_one({"_id": userid})
    return res["acknowledged"] #type: ignore
