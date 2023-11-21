from pydantic import BaseModel

class Oferta(BaseModel):
    ofertaid: str
    oferta: str
    category: str
    region: str
    ofertante: str

class SemanticSearchTerms(BaseModel):
    search_term: str
    category: str | None
    region: str | None
