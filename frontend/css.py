# ── ULTIMATE GLASSMORPHISM & UI ENHANCEMENT CSS ──────────────────────────────
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Syne:wght@600;700&family=DM+Sans:wght@400;500&display=swap');
    
    /* Hide Sidebar & Hamburger Menu entirely */
    [data-testid="stSidebar"], .st-emotion-cache-16ids9d {display: none;}[data-testid="stHeader"] {background: rgba(0,0,0,0);}
    
    html, body,[data-testid="stAppViewContainer"] {
        background-color: #05070A;
        font-family: 'Inter', sans-serif;
        color: #E0E0E0;
    }

    /* Top Navigation Bar */
    .nav-bar {
        background: rgba(10, 13, 18, 0.85);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        padding: 15px 50px;
        position: fixed;
        top: 0; left: 0; right: 0;
        display: flex; justify-content: space-between; align-items: center;
        z-index: 999;
    }

    /* ── DOMAIN TEXT TYPOGRAPHY ── */
    .domain-title {
        color: #00D1FF;
        font-family: 'Syne', sans-serif;
        font-size: 20px;
        font-weight: 600;
        margin-top: 35px;
        margin-bottom: 5px;
    }
    .domain-desc {
        color: #8B949E;
        font-size: 15px;
        margin-bottom: 15px;
    }

    /* ── ENHANCED TEXT AREAS ── */
    .stTextArea textarea {
        background-color: rgba(10, 13, 18, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        font-size: 15px !important;
        padding: 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.3) !important;
    }
    .stTextArea textarea:focus {
        border-color: #00D1FF !important;
        background-color: rgba(10, 13, 18, 0.9) !important;
        box-shadow: 0 0 0 2px rgba(0, 209, 255, 0.2), inset 0 2px 4px rgba(0,0,0,0.5) !important;
    }

    /* ── PROFESSIONAL "RUN" BUTTON ── */
    .stButton > button {
        background: linear-gradient(135deg, #00C6FF 0%, #0072FF 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        color: #ffffff !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        border-radius: 14px !important;
        height: 65px; 
        width: 100%; 
        margin-top: 20px !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 8px 24px rgba(0, 114, 255, 0.3) !important;
    }
    .stButton > button:hover { 
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 14px 32px rgba(0, 114, 255, 0.5) !important; 
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
    }

    /* ── PERFECT FLOATING MESSENGER PILL BUTTON ── */
    div[data-testid="stPopover"] {
        position: fixed !important;
        bottom: 35px !important;
        right: 35px !important;
        left: auto !important;
        top: auto !important;
        z-index: 1000 !important;
        width: auto !important;
    }
    div[data-testid="stPopover"] > button {
        background: linear-gradient(135deg, #6C5CE7 0%, #0084FF 100%) !important;
        color: white !important;
        border-radius: 40px !important;
        width: auto !important;
        padding: 0 28px !important;
        height: 60px !important;
        border: 2px solid rgba(255,255,255,0.2) !important;
        box-shadow: 0 8px 24px 0 rgba(108, 92, 231, 0.4) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: 0.3s ease !important;
    }

    /* ── PREMIUM DIAGNOSTIC REPORT CSS ── */
    .report-container {
        background: linear-gradient(145deg, rgba(16, 23, 36, 0.7), rgba(11, 16, 26, 0.9));
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 40px;
        margin-top: 40px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
        backdrop-filter: blur(20px);
        animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .report-header h2 {
        font-family: 'Syne', sans-serif;
        color: #F8FAFC;
        margin: 0 0 5px 0;
        font-size: 28px;
    }
    .report-header p {
        color: #64748B;
        font-size: 14px;
        margin: 0 0 30px 0;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
    }
    .domain-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-bottom: 30px;
    }
    .domain-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 20px;
        display: flex;
        align-items: center;
        gap: 15px;
        transition: transform 0.3s ease;
    }
    .domain-card:hover {
        transform: translateY(-5px);
        background: rgba(30, 41, 59, 0.8);
        border-color: rgba(255,255,255,0.1);
    }
    .d-icon {
        font-size: 28px;
        background: rgba(255,255,255,0.03);
        width: 55px; height: 55px;
        display: flex; align-items: center; justify-content: center;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    .d-text h4 {
        margin: 0 0 8px 0;
        font-size: 15px;
        color: #E2E8F0;
        font-weight: 600;
    }
    .badge {
        font-size: 12px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .badge-risk { background: rgba(244, 63, 94, 0.15); color: #FB7185; border: 1px solid rgba(244, 63, 94, 0.3); }
    .badge-optimal { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }
    
    .final-verdict {
        padding: 25px;
        border-radius: 16px;
        display: flex;
        gap: 20px;
        align-items: flex-start;
    }
    .verdict-risk {
        background: linear-gradient(135deg, rgba(225, 29, 72, 0.1), rgba(159, 18, 57, 0.2));
        border: 1px solid rgba(225, 29, 72, 0.3);
    }
    .verdict-optimal {
        background: linear-gradient(135deg, rgba(5, 150, 105, 0.1), rgba(6, 78, 59, 0.2));
        border: 1px solid rgba(5, 150, 105, 0.3);
    }
    .v-icon { font-size: 35px; }
    .v-content h3 {
        margin: 0 0 8px 0;
        font-size: 20px;
        font-family: 'Syne', sans-serif;
    }
    .verdict-risk .v-content h3 { color: #FDA4AF; }
    .verdict-optimal .v-content h3 { color: #6EE7B7; }
    .v-content p {
        margin: 0; font-size: 15px; color: #CBD5E1; line-height: 1.6;
    }
    @media (max-width: 900px) {
        .domain-grid { grid-template-columns: 1fr; }
    }
</style>
"""

CHAT_CSS = """
<style>
/* ── POPOVER BODY (PRO VERSION) ── */
div[data-testid="stPopoverBody"] {
    position: fixed !important;
    bottom: 110px !important;
    right: 35px !important;
    left: auto !important;
    top: auto !important;
    transform: none !important;
    width: 500px !important;
    max-width: 90vw !important;
    height: 650px !important;
    overflow-y: auto !important;
    padding: 5px 5px 5px 5px !important;
    border-radius: 22px !important;
    background: linear-gradient(145deg, rgba(11,17,26,0.85), rgba(15,23,42,0.95)) !important;
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.15) !important;
    box-shadow: 0 15px 40px rgba(0,0,0,0.6), 0 0 0 1px rgba(0, 209, 255, 0.15), 0 0 25px rgba(0, 209, 255, 0.15);
    animation: fadeInChat 0.50s ease;
}
@keyframes fadeInChat {
    from { opacity: 0; transform: translateY(20px) scale(0.97); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}
div[data-testid="stPopoverBody"]::-webkit-scrollbar { width: 0px; }
.chat-header-pro {
    display: flex; align-items: center; gap: 12px; padding-bottom: 12px;
    margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.08);
}
.chat-icon-pro {
    width: 42px; height: 42px; border-radius: 50%;
    background: linear-gradient(135deg, #00D1FF, #0072FF);
    display: flex; align-items: center; justify-content: center;
    font-size: 25px; color: white;
    box-shadow: 0 4px 15px rgba(0, 209, 255, 0.4);
    border: 2px solid rgba(255,255,255,0.2);
}
.chat-title { font-size: 15px; font-weight: 600; color: #F8FAFC; }
.chat-status { font-size: 11px; color: #00FF00; letter-spacing: 0.5px; }
.status-dot {
    width: 8px; height: 8px; background: #00FF00; border-radius: 50%;
    display: inline-block; margin-right: 6px; animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(0,209,255,0.6); }
    70% { box-shadow: 0 0 0 8px rgba(0,209,255,0); }
    100% { box-shadow: 0 0 0 0 rgba(0,209,255,0); }
}
.chat-row { display: flex; align-items: flex-end; gap: 10px; margin-bottom: 16px; }
.chat-row.user { flex-direction: row-reverse; } 
.chat-row.bot { flex-direction: row; }
.msg-avatar {
    width: 28px; height: 28px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; flex-shrink: 0;
}
.chat-row.bot .msg-avatar {
    background: linear-gradient(135deg, #38BDF8 0%, #3B82F6 100%);
    box-shadow: 0 2px 8px rgba(56, 189, 248, 0.4);
    border: 1px solid rgba(255,255,255,0.2);
}
.chat-row.user .msg-avatar {
    background: #1E293B; border: 1px solid #334155; color: #94A3B8;
}
.bubble { 
    padding: 12px 16px; font-size: 15px; line-height: 1.5; 
    width: fit-content; max-width: 80%; 
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15); letter-spacing: 0.2px;
}
.chat-row.bot .bubble { 
    background: #1E293B; color: #F8FAFC; 
    border: 1px solid #334155; border-radius: 16px 16px 16px 4px; 
}
.chat-row.user .bubble { 
    background: linear-gradient(135deg, #0EA5E9 0%, #2563EB 100%); 
    color: #FFFFFF; border-radius: 16px 16px 4px 16px; 
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3); 
}
.typing-dots { display: flex; align-items: center; gap: 5px; height: 18px; }
.typing-dots span {
    width: 6px; height: 6px; background-color: #94A3B8; border-radius: 50%;
    animation: typing-bounce 1.4s infinite ease-in-out both;
}
.typing-dots span:nth-child(1) { animation-delay: -0.32s; }
.typing-dots span:nth-child(2) { animation-delay: -0.16s; }
@keyframes typing-bounce {
    0%, 80%, 100% { transform: scale(0); opacity: 0.5; }
    40% { transform: scale(1); opacity: 1; }
}
</style>
"""

TOP_NAVIGATION_HEADER = """
    <div class="nav-bar">
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="font-size: 24px;">🛡️</span>
            <span style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 22px;">MindGuard <span style="color: #00D1FF;">Pro</span></span>
        </div>
    </div>
    <div style="margin-top: 100px;"></div>

"""

REPORT_HTML = """
<div class="report-container">
<div class="report-header">
<h2>📑 Diagnostic AI Report</h2>
<p>Generated by MindGuard Ensemble Engine</p>
</div>
<div class="domain-grid">
<div class="domain-card">
<div class="d-icon">🌅</div>
<div class="d-text">
<h4>Routine & Energy</h4>
{b1}
</div>
</div>
<div class="domain-card">
<div class="d-icon">👥</div>
<div class="d-text">
<h4>Social Connection</h4>
{b2}
</div>
</div>
<div class="domain-card">
<div class="d-icon">📅</div>
<div class="d-text">
<h4>Temporal Outlook</h4>
{b3}
</div>
</div>
</div>
<div class="final-verdict {verdict_class}">
<div class="v-icon">{v_icon}</div>
<div class="v-content">
<h3>{v_title}</h3>
<p>{v_desc}</p>
</div>
</div>
</div>
"""