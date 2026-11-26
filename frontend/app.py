
import streamlit as st

from components import render_html
from styles import load_css

from pages.home import show_home
from pages.analyze import show_analyze
from pages.about import show_about


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Fluency Coach",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD CUSTOM CSS
load_css()


# SIDEBAR
with st.sidebar:

    render_html("""
        <div style="text-align:center; padding:20px 5px;">
            <div style="font-size:42px;">🎙️</div>
            <h2 style="color:white; margin:5px 0;">
                Fluency Coach
            </h2>
            <p style="color:#9daecc; font-size:12px;">
                SPEECH AWARENESS PLATFORM
            </p>
        </div>
    """)

    st.markdown("---")

    selected_page = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "🎙️ Analyze Speech",
            "ℹ️ About Project"
        ],
        label_visibility="visible"
    )

    st.markdown("---")

    render_html("""
        <div style="padding:12px; background:#1b2540;
                    border-radius:12px;">
            <p style="font-size:13px; color:#b7c2dc;">
                <b>Current focus</b><br><br>
                Possible speech disfluency detection from
                short audio recordings.
            </p>
        </div>
    """)


# PAGE ROUTING
if selected_page == "🏠 Home":
    show_home()

elif selected_page == "🎙️ Analyze Speech":
    show_analyze()

elif selected_page == "ℹ️ About Project":
    show_about()
