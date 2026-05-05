from pydantic import BaseModel

class RequestText(BaseModel):
    ans1: str
    ans2: str
    ans3: str