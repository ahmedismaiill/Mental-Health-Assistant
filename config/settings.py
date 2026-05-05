##############################
# Data Directory for RAG Base
##############################

DATA1_DIR_RAG_BASE = 'data/rag_base/mental_health_counseling_conversations1.csv'
DATA2_DIR_RAG_BASE = 'data/rag_base/mental_health_counseling_conversations2.csv'

################################################
# Local Vector Database Configuration (ChromaDB)
################################################
VECTOR_DB_DIR = './local_db'
CHUNK_SIZE = 1600
CHUNK_OVERLAP = 200
LENGTH_FUNCTION = len
SEARCH_K = 5

###########################################################
# Ollama Configuration (Local LLM and Embeddings Provider )
###########################################################

OLLAMA_EMBEDDINGS_MODEL = "nomic-embed-text"
OLLAMA_LLM_MODEL = "llama3.2:3b"

##############################
# API Configuration
##############################

API_CHAT_URL = 'http://localhost:8001/chat'
API_GENERATE_REPORT_URL = 'http://localhost:8001/generate'
API_PREDICT_URL = 'http://localhost:8002/predict'

#############################################
# Model Configuration for Depression Detection
#############################################

DEPRESSION_MODEL_DIR = r"D:\Mental Health Assistant NLP Practical Exam\backend\mental_app\models\depression_model"
