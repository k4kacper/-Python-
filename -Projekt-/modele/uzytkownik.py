from pydantic import BaseModel, EmailStr

class Uzytkownik(BaseModel):
    id: int
    imie: str
    email: EmailStr