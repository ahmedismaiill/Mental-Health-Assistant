from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import Chroma
from langchain.chains import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from config.settings import VECTOR_DB_DIR, OLLAMA_EMBEDDINGS_MODEL, OLLAMA_LLM_MODEL, SEARCH_K

###################################################################################################################################
### This is the "brain" of your app. It loads the existing database, sets up Llama 3.2, defines the prompts, and wires up the memory.
###################################################################################################################################

# Dictionary to store chat histories for different sessions/users
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def setup_rag_chain():
    # 1. Load Existing Database
    embeddings = OllamaEmbeddings(model=OLLAMA_EMBEDDINGS_MODEL)
    vectorstore = Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embeddings
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": SEARCH_K})

    # 2. Setup LLM
    llm = ChatOllama(model=OLLAMA_LLM_MODEL, temperature=0.7) 

    # 3. Setup Prompts
    
    contextualize_q_system_prompt = """Given a chat history and the latest user question \
    which might reference context in the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."""

    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    
    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

    qa_system_prompt = """You are a warm, conversational, and supportive mental health assistant. 
    You act like a wise, empathetic friend who happens to know professional counseling techniques.

    CRITICAL RULES YOU MUST FOLLOW:
    1. Speak naturally. DO NOT start your responses with "I'm so sorry to hear that" or "That must be really tough." Vary your openings and talk like a normal person.
    2. DO NOT suggest hotlines, doctors, or professional help unless the user explicitly mentions self-harm, physical abuse, or severe trauma. For everyday stress, sadness, or relationship issues, just be a listening ear.
    3. Keep your answers relatively concise. Avoid lecturing. 
    4. Ask gentle, open-ended questions occasionally to keep the conversation flowing naturally.
    5. Use the provided context to guide your advice, but weave it in naturally.
    6. If the provided context is completely unrelated to the user's current issue, ignore the context and use your own empathy to support them.

    7. VERY IMPORTANT FORMATTING RULES:
- Do NOT use bullet points, asterisks (*), dashes (-), or numbered lists.
- Write everything in natural paragraphs or simple sentences.
- Do NOT structure your response like a list.
- Avoid markdown formatting entirely.
    Context:
    {context}"""

    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    # 4. Wire Chains Together
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    # 5. Attach Memory
    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    
    return conversational_rag_chain