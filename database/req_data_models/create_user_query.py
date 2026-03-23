from pydantic import BaseModel

class CreateUserQuery(BaseModel):
    username: str
    email: str
    phone: str
