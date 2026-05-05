from langchain_ollama import ChatOllama
from backend.rag_app.api.schemas import AssessmentData
from config.settings import OLLAMA_LLM_MODEL

def generate_insights(data: AssessmentData):
    try:
        llm = ChatOllama(model=OLLAMA_LLM_MODEL, temperature=0.7)
        
        prompt = f"""You are a compassionate, professional AI mental health assistant.
        You are reviewing a user's self-assessment. Based on a separate diagnostic model, 
        their current state is flagged as: {data.risk_level}.
        
        Here is what the user said:
        - Domain 1 (Routine & Energy): {data.ans1}
        - Domain 2 (Social Connection): {data.ans2}
        - Domain 3 (Temporal Outlook): {data.ans3}
        
        Task: Write a personalized, empathetic summary report (3 brief paragraphs).
        1. Acknowledge and validate their specific feelings based strictly on their answers.
        2. Highlight any positive coping mechanisms they mentioned, or gently point out areas of fatigue/isolation.
        3. Provide brief, encouraging advice. If their state is "Elevated Risk", gently encourage speaking to a professional.
        
        IMPORTANT RULES:
        - Do NOT medically diagnose them. 
        - Do NOT invent information that the user did not say.
        - Format with friendly markdown, bolding key phrases for readability.
        """
        
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error generating insights: {str(e)}"