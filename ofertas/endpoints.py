from fastapi import APIRouter, Request

from ofertas.models import Oferta, SemanticSearchTerms

from ofertas import service

router = APIRouter()

@router.post("/addOferta")
async def addOferta(request: Request, oferta: Oferta):
    service.addOferta(oferta, request.app.state.mongoConnection)
    return {"status": "success"}

@router.get("/deleteOferta/{ofertaid}")
async def deleteOferta(request: Request, ofertaid: str):
    pass

@router.get("/getOferta/{ofertaid}")
async def getOferta(request: Request, ofertaid: str):
    pass

@router.post("/semanticSearch")
async def semanticSearch(request: Request, search_terms: SemanticSearchTerms):
    pass

@router.get("/recommendOfertas/{userid}")
async def recommendOfertas(request: Request, userid: str):
    pass

@router.get("/queryOfertas")
async def queryOfertas(request: Request, category: str, region: str, ofertante: str):
    pass
