from fastapi import APIRouter
from .schemas import RequestText
from ..core.model import predict_sentiment

router = APIRouter()

@router.post("/predict")
def predict(req: RequestText):
    try:
        result1 = predict_sentiment(req.ans1)
        result2 = predict_sentiment(req.ans2)
        result3 = predict_sentiment(req.ans3)
        return {"label1": result1, "label2": result2, "label3": result3}
    except Exception as e:
        return {"error": str(e)}