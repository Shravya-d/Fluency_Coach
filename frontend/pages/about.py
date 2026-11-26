
import streamlit as st

from components import render_html
from components.header import page_header


def show_about():

    # PAGE HEADER
   
    # INTRODUCTION
    st.markdown("## About Fluency Coach")

    st.write("""
    Fluency Coach is a speech awareness platform that helps users
    understand their speech patterns by analyzing uploaded audio
    recordings and identifying possible speech disfluencies.
    """)

    st.markdown("---")

    # WORKFLOW
    st.markdown("## How Fluency Coach Works")

    st.write(
        "Follow these four simple steps to analyze your speech."
    )

    steps = [
        (
            "01",
            "Upload Audio",
            "Upload a short speech recording in WAV or MP3 format."
        ),
        (
            "02",
            "Audio Processing",
            "The system prepares the uploaded audio for analysis."
        ),
        (
            "03",
            "Speech Analysis",
            "The system analyzes the recording to identify possible speech disfluencies."
        ),
        (
            "04",
            "View Results",
            "View the possible speech disfluency detection result."
        )
    ]

    for number, title, description in steps:

        render_html(
            f"""
            <div class="step-card">
                <div class="step-number">STEP {number}</div>
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            """
        )

    # FOOTER
    render_html("""
    <div class="footer">
        FLUENCY COACH · SPEECH AWARENESS PLATFORM
    </div>
    """)
