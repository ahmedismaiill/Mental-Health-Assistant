import requests
import streamlit as st
import time
from config.settings import API_CHAT_URL, API_PREDICT_URL, API_GENERATE_REPORT_URL
from frontend.css import STYLE, CHAT_CSS, TOP_NAVIGATION_HEADER, REPORT_HTML
import streamlit.components.v1 as components

# ==============================================================================
# 1. API COMMUNICATION FUNCTIONS
# ==============================================================================

def get_bot_response(user_text):
    try:
        session_id = "default_user_session" 
        
        response = requests.post(
            API_CHAT_URL,
            json={
                "message": user_text, 
                "session_id": session_id
            },
            timeout=60
        )
        
        if response.status_code == 200:
            return response.json()["answer"]
        else:
            return f"Error: Server returned {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error: {str(e)}"

def get_model_predict_from_api(ans1, ans2, ans3):
    try:
        response = requests.post(API_PREDICT_URL, json={"ans1": ans1, "ans2": ans2, "ans3": ans3}, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Server returned {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_llm_insights_via_api(ans1, ans2, ans3, risk_status):
    """Calls the FastAPI backend to get the Llama 3.2 generated report."""
    API_URL = API_GENERATE_REPORT_URL
    payload = {
        "ans1": ans1,
        "ans2": ans2,
        "ans3": ans3,
        "risk_level": risk_status
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=60)
        if response.status_code == 200:
            data = response.json()
            return data["report"]
        else:
            return f"⚠️ API Error: {response.status_code} - {response.text}"
    except requests.exceptions.ConnectionError:
        return "⚠️ Error: Could not connect to the API. Is your FastAPI server running?"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {str(e)}"

# ==============================================================================
# 2. PAGE CONFIGURATION & THEME
# ==============================================================================
st.set_page_config(
    page_title="MindGuard Pro | Clinical Portal",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session State for Results & Chat
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None

def clear_results():
    st.session_state.analysis_results = None

# Inject custom CSS styles
st.markdown(STYLE, unsafe_allow_html=True)

# ==============================================================================
# 3. TOP NAVIGATION HEADER 
# ==============================================================================
st.markdown(TOP_NAVIGATION_HEADER, unsafe_allow_html=True)

# ==============================================================================
# 4. MAIN ASSESSMENT PORTAL
# ==============================================================================
col_main = st.columns([1, 6, 1])[1] 

with col_main:
    st.markdown("<h1 style='text-align: center; font-family: Syne, sans-serif; font-weight: 700; font-size: 42px;'>Clinical Assessment Dashboard</h1>", unsafe_allow_html=True)
    
    st.markdown("<div class='domain-title'>🌅 Domain 1: Routine & Energy</div>", unsafe_allow_html=True)
    st.markdown("<div class='domain-desc'>Describe your morning energy levels, sleep quality, and daily habits over the past two weeks.</div>", unsafe_allow_html=True)
    ans1 = st.text_area("Q1", placeholder="I usually wake up feeling...", height=120, label_visibility="collapsed", on_change=clear_results)
    
    st.markdown("<div class='domain-title'>👥 Domain 2: Social Connection</div>", unsafe_allow_html=True)
    st.markdown("<div class='domain-desc'>How have your interactions with friends, family, or colleagues been lately? Do you feel supported?</div>", unsafe_allow_html=True)
    ans2 = st.text_area("Q2", placeholder="Lately, engaging with others feels...", height=120, label_visibility="collapsed", on_change=clear_results)
    
    st.markdown("<div class='domain-title'>📅 Domain 3: Temporal Outlook</div>", unsafe_allow_html=True)
    st.markdown("<div class='domain-desc'>What are your thoughts regarding the upcoming week? Do you look forward to any particular activities?</div>", unsafe_allow_html=True)
    ans3 = st.text_area("Q3", placeholder="When I think about next week, I...", height=120, label_visibility="collapsed", on_change=clear_results)
    
    st.markdown("<br>", unsafe_allow_html=True)
        
    if st.button("🚀 Run Diagnostic Ensemble Analysis"):
        if not (ans1 and ans2 and ans3):
            st.warning("⚠️ Please complete all three behavioral domains to proceed.")
            clear_results()
        elif len(ans1.split()) < 3 or len(ans2.split()) < 3 or len(ans3.split()) < 3:
            st.error("⚠️ Each response must contain at least **3 words**.")
            clear_results()
        else:
            # STEP 1: API Prediction (Classification)
            with st.spinner("Analyzing neural linguistic patterns..."):
                time.sleep(0.5)
                response = get_model_predict_from_api(ans1, ans2, ans3)
                total = response["label1"] + response["label2"] + response["label3"]
                
                # Temporarily store to state
                st.session_state.analysis_results = {
                    "v1": response["label1"], "v2": response["label2"], "v3": response["label3"], 
                    "total": total
                }

            # STEP 2: Call FastAPI (Llama 3.2 Insights)
            with st.spinner("Generating personalized AI insights via API..."):
                risk_status = "Elevated Risk of Depression" if total >= 2 else "Stable / Optimal Baseline"
                llm_report = get_llm_insights_via_api(ans1, ans2, ans3, risk_status)

            # Update session state with LLM report
            st.session_state.analysis_results["llm_report"] = llm_report

    # ── PROFESSIONAL DIAGNOSTIC REPORT OUTPUT ──
    if st.session_state.analysis_results is not None:
        res = st.session_state.analysis_results
        total = res["total"]

        def get_badge(is_risk):
            if is_risk:
                return "<span class='badge badge-risk'>● Elevated Risk</span>"
            return "<span class='badge badge-optimal'>● Optimal Baseline</span>"
        
        b1, b2, b3 = get_badge(res['v1']), get_badge(res['v2']), get_badge(res['v3'])

        if total >= 2:
            verdict_class = "verdict-risk"
            v_icon = "⚠️"
            v_title = f"High-Confidence Signals Detected ({total}/3 Domains)"
            v_desc = "<strong>Clinical Assessment:</strong> Consistent linguistic patterns of emotional distress identified. We strongly recommend clinical follow-up for a formal evaluation by a healthcare professional."
        else:
            verdict_class = "verdict-optimal"
            v_icon = "🛡️"
            v_title = "Negative Screening Results"
            v_desc = "<strong>Clinical Assessment:</strong> Analysis indicates a stable emotional baseline. No consistent patterns of clinical depression were detected across the evaluated behavioral domains."

        report_html = REPORT_HTML.format(
            v_icon=v_icon, v_title=v_title, v_desc=v_desc, b1=b1, b2=b2, b3=b3, verdict_class=verdict_class
        )
        st.markdown(report_html, unsafe_allow_html=True) 
        
        st.markdown("---")
        st.markdown("<h3 style='color: #4A90E2;'>🧠 Personalized AI Insights</h3>", unsafe_allow_html=True)
        st.info(res["llm_report"], icon="✨")

# ==============================================================================
# 5. FLOATING COMPANION CHATBOT
# ==============================================================================

with st.popover(label="💬 Open Chat"): 
    st.markdown(CHAT_CSS, unsafe_allow_html=True)
    
    st.markdown("""
<div class="chat-header-pro">
<div class="chat-icon-pro">🌒</div>
<div>
<div class="chat-title">MindGuard AI Companion</div>
<div class="chat-status">
<span class="status-dot"></span>Secure & Active
</div>
</div>
</div>
""", unsafe_allow_html=True)

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages =[{"role": "assistant", "content": "Welcome. I'm here to listen. What's on your mind?"}]

    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.chat_messages:
            div_class = "bot" if msg["role"] == "assistant" else "user"
            icon = "👨🏻‍⚕️" if msg["role"] == "assistant" else "🙍🏻"
            st.markdown(f"""
<div class="chat-row {div_class}">
<div class="msg-avatar">{icon}</div>
<div class="bubble">{msg["content"]}</div>
</div>
""", unsafe_allow_html=True)

    prompt = st.chat_input("Speak freely...")

    if prompt:
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        
        with chat_container:
            st.markdown(f"""
<div class="chat-row user">
<div class="msg-avatar">🙍🏻</div>
<div class="bubble">{prompt}</div>
</div>
""", unsafe_allow_html=True)
            
            typing_placeholder = st.empty()
            typing_placeholder.markdown("""
<div class="chat-row bot">
<div class="msg-avatar">👨🏻‍⚕️</div>
<div class="bubble" style="padding: 14px 18px;">
<div class="typing-dots"><span></span><span></span><span></span></div>
</div>
</div>
""", unsafe_allow_html=True)
            
            components.html("""
                <script>
                    function snapToBottom() {
                        const doc = window.parent.document;
                        const popover = doc.querySelector('div[data-testid="stPopoverBody"]');
                        if (popover) { popover.scrollTop = popover.scrollHeight; }
                    }
                    snapToBottom(); setTimeout(snapToBottom, 50);
                </script>
            """, height=0)
            
            bot_reply = get_bot_response(prompt)
            typing_placeholder.empty()
            
        st.session_state.chat_messages.append({"role": "assistant", "content": bot_reply})
        st.rerun()

    components.html("""
        <script>
            function maintainBottomScroll() {
                const doc = window.parent.document;
                const popover = doc.querySelector('div[data-testid="stPopoverBody"]');
                if (popover) { popover.scrollTop = popover.scrollHeight; }
            }
            maintainBottomScroll();
            setTimeout(maintainBottomScroll, 50);
            setTimeout(maintainBottomScroll, 150);
        </script>
    """, height=0)

# ==============================================================================
# 6. FOOTER
# ==============================================================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.divider()
f1, f2, f3 = st.columns([2, 2, 1])
f1.caption("© 2026 MindGuard Research Systems | NLP Practical Exam")
f2.caption("Powered by Microservices Architecture & Streamlit Enterprise")
f3.markdown("<p style='text-align: right; color: #2ecc71; font-size: 12px;'>v1.0 Stable</p>", unsafe_allow_html=True)