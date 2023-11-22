from pydantic import BaseModel

class Oferta(BaseModel):
    ofertaid: str
    title: str
    description: str
    category: str
    region: str
    ofertante: str

class SemanticSearchTerms(BaseModel):
    search_term: str
    category: str | None = None
    region: str | None = None
