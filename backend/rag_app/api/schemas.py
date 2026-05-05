from pydantic import BaseModel

class AssessmentData(BaseModel):
    ans1: str
    ans2: str
    ans3: str
    risk_level: str

class ChatRequest(BaseModel):
    message: str
    session_id: str