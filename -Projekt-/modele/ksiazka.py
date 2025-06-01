from pydantic import BaseModel

class Ksiazka(BaseModel):
    id: int
    tytul: str
    autor: str
    rok: int
    dostepna: bool = True