from typing import Dict

from fastapi import APIRouter, Request

from users.models import OfertasHistory, User

from users import service

router = APIRouter()

@router.post("/addUser")
async def addUser(request: Request, usr: User) -> Dict:
    service.addUser(usr.userid, usr.name, request.app.state.mongoConnection)
    return {"status": "success"}

@router.get("/deleteUser/{userid}")
async def deleteUser(request: Request, userid: str):
    if not service.deleteUser(userid, request.app.state.mongoConnection):
        return {"status": "failed"}
    return {"status": "success"}


@router.get("/getUser/{userid}")
async def getUser(request: Request, userid: str) -> User:
    usr = service.getUser(userid, request.app.state.mongoConnection)
    return User(
        userid=usr["_id"],
        name=usr["name"]
    )

@router.post("/updateUserHistory/{userid}")
async def updateUserHistory(request: Request, userid: str, history: OfertasHistory):
    if not service.updateUserHistory(userid, history, request.app.state.mongoConnection):
        return {"status": "failed"}

    return {"status": "success"}

