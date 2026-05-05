# 🧠 MindGuard Pro: AI-Powered Clinical Mental Health Portal

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Llama](https://img.shields.io/badge/Llama_3.2-LLM-blueviolet)
![ChromaDB](https://img.shields.io/badge/Chroma-Vector_DB-ff69b4)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview
Early detection and intervention are critical in mental healthcare. **MindGuard Pro** is an advanced AI-powered diagnostic dashboard designed to screen for depression by analyzing linguistic patterns across key behavioral domains.

Built on a robust **microservices architecture**, this project integrates a custom **DistilBERT** deep learning model for ensemble sentiment classification with **Llama 3.2** and **Retrieval-Augmented Generation (RAG)** for generating personalized clinical insights. It provides real-time diagnostic reports and features a highly interactive, secure 24/7 AI companion chatbot to offer empathetic, context-aware emotional support.

---

## 📊 Clinical Domain Description
Instead of relying on rigid multiple-choice questionnaires, MindGuard Pro uses **Natural Language Processing (NLP)** to analyze free-text user responses across three critical behavioral domains:

*   **🌅 Domain 1: Routine & Energy:** Evaluates morning energy levels, sleep quality, and daily habits.
*   **👥 Domain 2: Social Connection:** Assesses interactions with friends, family, and feelings of support or isolation.
*   **📅 Domain 3: Temporal Outlook:** Analyzes future-oriented thinking, anticipation, and dread regarding the upcoming week.

**Diagnostic Logic:**
The system evaluates text length and linguistic markers. If the neural classification detects high-confidence distress signals in 2 or more domains, it flags an **Elevated Risk of Depression**; otherwise, it reports an **Optimal Baseline**.

---

## 🎥 Project Demos

### 2. Streamlit 

https://github.com/user-attachments/assets/11c38dce-7653-4b45-b21a-d476a2d61fa6

---

## 🛠 Methodology: Training & Architecture

### 1. Data Collection & Preprocessing
To train the underlying depression detection model, three publicly available datasets from Kaggle (spanning Reddit and Twitter) were combined to capture diverse writing styles and emotional expressions.
*   **Corpus Size:** 69,731 raw samples ➔ **66,762 unique samples** after strict deduplication and cleaning (URL stripping, HTML tag removal).
*   **Class Balance:** Highly balanced distribution (~52% Not Depressed, ~48% Depressed).
*   **Data Split:** Stratified into **70% Training** (46,733), **15% Validation** (10,014), and **15% Testing** (10,015).

### 2. Model Training & Fine-Tuning
The core classification engine uses **DistilBERT (`distilbert-base-uncased`)**, selected for retaining 97% of BERT's language understanding while being 60% faster.
*   **Tokenization:** Sequences truncated/padded to a maximum length of **128 tokens** (sufficient for the vast majority of social media text).
*   **Training Loop:** Fine-tuned over 5 epochs with early stopping. The optimal model checkpoint was saved at **Epoch 4**, achieving a peak validation F1-score of **99.53%**.

### 3. Microservices Backend (FastAPI & RAG)
The application decouples heavy ML inference from the frontend using a microservices approach:
*   **NLP Prediction API (`Port 8002`):** Ingests the 3 domain answers, feeds them through the trained PyTorch DistilBERT model, and returns binary risk labels.
*   **LLM & RAG Generation API (`Port 8001`):** Hosts **Llama 3.2** alongside a **ChromaDB** vector database. It uses RAG mapped to mental health counseling datasets to ensure the chatbot grounds its empathetic advice in actual counseling context.

### 4. Frontend Architecture (Streamlit)
*   **Dynamic UI:** Built with enterprise-grade CSS injections for a clinical theme. Includes simulated latency masking (typing dots) while waiting for backend LLM inference.
*   **Stateful Chat:** Floating popover chat UI utilizing `st.session_state` that persists across the diagnostic session.

---

## 📈 Model Accuracy & Evaluation Results

The fine-tuned DistilBERT model underwent rigorous evaluation on both an internal held-out test set and an entirely unseen external dataset to prove real-world generalizability.

### 🏆 Internal Test Set Performance
Evaluated on **10,015** unseen samples from the original dataset distribution. The confusion matrix recorded merely 25 False Positives and 36 False Negatives.

| Metric | Not Depressed | Depressed | **Overall** |
| :--- | :---: | :---: | :---: |
| **Precision** | 0.99 | 1.00 | 0.99 |
| **Recall** | 0.99 | 0.99 | 0.99 |
| **F1-Score** | 0.99 | 0.99 | 0.99 |
| **Accuracy** | — | — | **99.39%** |

### 🌍 External Dataset Validation
To test robust real-world generalizability, the model was validated against a completely independent dataset (Suchintika Sarkar's Sentiment Analysis dataset, **31,755** samples).

| Metric | Not Depressed | Depressed | **Overall** |
| :--- | :---: | :---: | :---: |
| **Precision** | 0.97 | 0.88 | 0.92 |
| **Recall** | 0.88 | **0.97** | 0.92 |
| **F1-Score** | 0.92 | 0.92 | 0.92 |
| **Accuracy** | — | — | **92.16%** |

*🔍 **Clinical Insight:** While overall accuracy dropped slightly on external data, the model maintained an exceptional **Recall of 0.97 for the Depressed class**. This translates to high sensitivity—ensuring that genuine signs of emotional distress are rarely missed, prioritizing user safety.*

---

## 📂 Project Structure

```text
D:.
│   .gitattributes
│   .gitignore
│   app.py                     # Main Streamlit Frontend
│   README.md
│   requirements.txt
│
├───backend
│   ├───mental_app             # PyTorch DistilBERT Classification Microservice
│   │   │   main.py
│   │   ├───api
│   │   │       routes.py
│   │   │       schemas.py
│   │   ├───core
│   │   │       model.py
│   │   │       preprocessing.py
│   │   └───models
│   │       └───depression_model
│   │               config.json
│   │               model.safetensors
│   │               tokenizer.json
│   │               tokenizer_config.json
│   │
│   └───rag_app                # Llama 3.2 & ChromaDB RAG Microservice
│       │   main.py
│       ├───api
│       │       routes.py
│       │       schemas.py
│       └───core
│               engine.py
│               generate_report.py
│               ingest_data.py
│               rag_core.py
│
├───config
│       settings.py
│
├───data                       # Training & Context Datasets
│   ├───combined_data
│   ├───depression_reddit_dataset_(cleaned)
│   ├───depression_tweets
│   └───rag_base
│           mental_health_counseling_conversations1.csv
│           mental_health_counseling_conversations2.csv
│
├───doc
│       NLP Practical Exam.pdf
│
├───frontend                   # UI/UX Assets
│       css.py
│
├───local_db                   # ChromaDB Vector Store
│       chroma.sqlite3
│       └───fea9cb2b-3947-4d3d-9906-44e953d026df
│
└───notebooks                  # Model Training & EDA
        Mental Health Assisstant.ipynb
```

---

## 💻 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ahmedismaiill/Mental-Health-Assistant.git
    cd MindGuard-Pro
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch Backend Microservices (FastAPI)**
    Open two separate terminal instances:
    
    *Terminal 1 (Start the LLM & RAG Chatbot API):*
    ```bash
    uvicorn backend.rag_app.main:app --port 8001 --reload
    ```

    *Terminal 2 (Start the PyTorch Classification API):*
    ```bash
    uvicorn backend.mental_app.main:app --port 8002 --reload
    ```

4.  **Launch the Streamlit Frontend App**
    Open a third terminal instance:
    ```bash
    streamlit run app.py
    ```
