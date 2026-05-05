from fastapi import APIRouter, HTTPException
from backend.rag_app.api.schemas import AssessmentData, ChatRequest
from backend.rag_app.core.rag_core import setup_rag_chain
from backend.rag_app.core.generate_report import generate_insights

router = APIRouter()

try:
    chat_chain = setup_rag_chain()
except Exception as e:
    print(f"FAILED TO LOAD RAG CHAIN: {e}")
    chat_chain = None

@router.post("/chat")
def chat(req: ChatRequest):
    if chat_chain is None:
        raise HTTPException(status_code=500, detail="RAG system is not initialized.")
    try:
        response = chat_chain.invoke(
            {"input": req.message},
            config={"configurable": {"session_id": req.session_id}}
        )
        return {"answer": response["answer"]}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
    
@router.post("/generate")
def handle_generate_report(data: AssessmentData):
    try:
        report_text = generate_insights(data)
        return {"report": report_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))