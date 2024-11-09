from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    idade: int
    pai: str | None