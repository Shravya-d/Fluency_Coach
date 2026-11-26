
import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* Main application */
    .stApp {
        background: linear-gradient(
            135deg,
            #0b1020 0%,
            #111a32 55%,
            #17152f 100%
        );
        color: #f4f6ff;
    }

    /* Keep the custom radio navigation as the only sidebar menu. */
    [data-testid="stSidebarNav"] {
        display: none;
    }

    /* Hide Streamlit branding and deployment controls without hiding the header. */
    #MainMenu {
        visibility: hidden;
    }

    [data-testid="stDeployButton"],
    button[data-testid="stBaseButton-header"] {
        display: none !important;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Main content width */
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .stMarkdown,
    [data-testid="stWidgetLabel"] {
        color: #f4f6ff;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(
            120deg,
            #243b70,
            #503b83,
            #783f83
        );
        padding: 48px 42px;
        border-radius: 24px;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 12px 35px rgba(0,0,0,0.25);
    }

    .hero-tag {
        color: #d8d5ff;
        font-size: 13px;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 700;
    }

    .hero h1 {
        color: white;
        font-size: 45px;
        line-height: 1.15;
        margin: 16px 0;
    }

    .hero p {
        color: #e0e5ff;
        font-size: 17px;
        line-height: 1.7;
        max-width: 720px;
    }

    /* Section headings */
    .section-heading {
        color: #ffffff;
        font-size: 27px;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 8px;
    }

    .section-description {
        color: #aebbd8;
        font-size: 15px;
        margin-bottom: 22px;
    }

    /* Feature cards */
    .feature-card {
        background: rgba(255,255,255,0.055);
        border: 1px solid rgba(255,255,255,0.12);
        padding: 23px;
        border-radius: 17px;
        min-height: 180px;
        margin-bottom: 15px;
        height: 100%;
        box-sizing: border-box;
        overflow-wrap: anywhere;
    }

    .feature-icon {
        font-size: 29px;
        margin-bottom: 12px;
    }

    .feature-card h3 {
        color: #ffffff;
        font-size: 19px;
        margin-bottom: 9px;
    }

    .feature-card p {
        color: #b7c2dc;
        font-size: 14px;
        line-height: 1.65;
    }

    /* Information panels */
    .info-panel {
        background: rgba(125, 115, 255, 0.10);
        border-left: 4px solid #9b91ff;
        padding: 20px 23px;
        border-radius: 12px;
        margin: 20px 0;
    }

    .info-panel p {
        color: #d6ddf3;
        line-height: 1.7;
    }

    /* Workflow */
    .step-card {
        background: rgba(255,255,255,0.045);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        min-height: 145px;
        height: 100%;
        box-sizing: border-box;
        overflow-wrap: anywhere;
    }

    .step-number {
        color: #b7a8ff;
        font-size: 13px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .step-card h4 {
        color: white;
        margin: 12px 0 8px 0;
    }

    .step-card p {
        color: #aebbd8;
        font-size: 13px;
    }

    /* Footer */
    .footer {
        border-top: 1px solid rgba(255,255,255,0.12);
        margin-top: 55px;
        padding-top: 22px;
        color: #8998b8;
        text-align: center;
        font-size: 13px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #10172b;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
        padding-top: 0.8rem;
    }

    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        color: #e9edff;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.12);
        margin: 1rem 0;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] {
        gap: 0.35rem;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] label {
        background: rgba(255,255,255,0.045);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 10px;
        padding: 0.45rem 0.65rem;
        transition: background-color 150ms ease, border-color 150ms ease;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: rgba(125,115,255,0.16);
        border-color: rgba(155,145,255,0.45);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #7666e8, #a16be8);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 22px;
        font-weight: 600;
    }

    .stButton > button:hover {
        border: 1px solid #c2b7ff;
        color: white;
    }

    .stButton > button:focus-visible {
        outline: 2px solid #d6ceff;
        outline-offset: 2px;
    }

    /* Upload / input containers */
    [data-testid="stFileUploader"] {
        background: rgba(255,255,255,0.035);
        border-radius: 12px;
    }

    [data-testid="stFileUploader"] section {
        border-color: rgba(255,255,255,0.2);
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 1.25rem 1rem 2rem;
        }

        .hero {
            padding: 32px 24px;
            border-radius: 18px;
        }

        .hero h1 {
            font-size: clamp(30px, 8vw, 40px);
        }

        .section-heading {
            font-size: 23px;
        }

        .feature-card,
        .step-card {
            min-height: auto;
        }
    }

    </style>
    """, unsafe_allow_html=True)
