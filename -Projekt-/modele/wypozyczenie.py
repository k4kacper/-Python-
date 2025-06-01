from datetime import datetime
from pydantic import BaseModel, EmailStr

class Wypozyczenie(BaseModel):
    id: int
    nazwaKsiazki: str
    emailUzytkownika: EmailStr
    wypozyczono_date: datetime
    return_date: datetime | None