from typing import Dict, List
from fastapi import APIRouter, Request

from ofertas.models import Oferta, SemanticSearchTerms

from ofertas import service

router = APIRouter()

@router.post("/addOferta")
async def addOferta(request: Request, oferta: Oferta) -> Dict:
    service.addOferta(oferta, request.app.state.mongoConnection)
    return {"status": "success"}

@router.get("/deleteOferta/{ofertaid}")
async def deleteOferta(request: Request, ofertaid: str) -> Dict:
    if service.deleteOferta(ofertaid, request.app.state.mongoConnection):
        return {"status": "success"}
    return {"status": "failed"}

@router.get("/getOferta/{ofertaid}")
async def getOferta(request: Request, ofertaid: str) -> Oferta | None:
    resp = service.getOferta(ofertaid, request.app.state.mongoConnection)
    if resp is None:
        return None
    return Oferta(
        ofertaid=resp["_id"],
        title=resp["title"],
        description=resp["description"],
        category=resp["category"],
        region=resp["region"],
        ofertante=resp["ofertante"]
    )

@router.post("/semanticSearch")
async def semanticSearch(request: Request, search_terms: SemanticSearchTerms) -> List[Oferta]:
    return service.semanticSearch(search_terms, request.app.state.mongoConnection)

@router.get("/recommendOfertas/{userid}")
async def recommendOfertas(request: Request, userid: str) -> List[Oferta]:
    return service.recommendOfertas(userid, request.app.state.mongoConnection)

@router.get("/queryOfertas")
async def queryOfertas(request: Request, category: str | None, region: str | None, ofertante: str | None) -> List[Oferta]:
    return service.queryOfertas(category, region, ofertante, request.app.state.mongoConnection)
