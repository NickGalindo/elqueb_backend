from typing import Dict

from fastapi import APIRouter, Request

from users.models import User

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
async def getUser(request: Request, userid: str) -> Dict:
    return service.getUser(userid, request.app.state.mongoConnection)
