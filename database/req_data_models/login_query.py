from pydantic import BaseModel


class LoginQuery(BaseModel):

    username: str
    password: str