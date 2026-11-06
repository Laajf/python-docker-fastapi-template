from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    email: str = Field(..., alias='email_address')
