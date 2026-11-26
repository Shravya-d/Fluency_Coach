
import streamlit as st

from components import render_html
from components.cards import feature_card, step_card


def show_home():

    
    # HERO SECTION
    render_html("""
    <div class="hero">
        <div class="hero-tag">SPEECH AWARENESS</div>
        <h1>Every Voice Deserves<br>to Be Heard.</h1>
        <p>
            Fluency Coach is a speech support project designed to
            identify possible speech disfluencies from short audio
            recordings and encourage greater awareness of speech patterns.
        </p>
    </div>
    """)

    # INTRODUCTION
    st.markdown(
        '<div class="section-heading">What is Fluency Coach?</div>',
        unsafe_allow_html=True
    )

    render_html("""
    <p class="section-description">
        Understanding speech patterns is the first step towards
        building awareness and confidence.
    </p>
    <div class="info-panel">
        <p>
        Speech does not always flow smoothly. Some speakers may experience
        repetitions, prolongations, blocks or other interruptions while
        speaking. These are known as speech disfluencies.
        <br><br>
        Fluency Coach aims to identify possible disfluencies in recorded
        speech. It is designed as a supportive awareness tool, not as
        a medical diagnostic system.
        </p>
    </div>
    """)

    # PROBLEM STATEMENT
    st.markdown(
        '<div class="section-heading">Why are we building this?</div>',
        unsafe_allow_html=True
    )

    render_html("""
    <p class="section-description">
        Our motivation and the problem we aim to address.
    </p>
    """)

    col1, col2 = st.columns(2)

    with col1:
        feature_card(
            "🎙️",
            "Speech is individual",
            "Every person has a unique speaking pattern. "
            "Disfluencies can occur naturally during everyday communication."
        )

    with col2:
        feature_card(
            "🔍",
            "Awareness matters",
            "Identifying possible interruptions in speech can help "
            "users understand their own speech patterns."
        )

    # CURRENT OBJECTIVE
    st.markdown(
        '<div class="section-heading">What does our system do?</div>',
        unsafe_allow_html=True
    )

    render_html("""
    <p class="section-description">
        The current development phase focuses on speech disfluency detection.
    </p>
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        feature_card(
            "📤",
            "Upload Audio",
            "Upload a short speech recording in a supported audio format."
        )

    with col2:
        feature_card(
            "🔍",
            "Analyze Speech",
            "The system analyzes the uploaded recording to identify "
            "possible speech disfluencies."
        )

    with col3:
        feature_card(
            "📊",
            "View Results",
            "View the outcome of the speech analysis."
        )

    # WORKFLOW
    st.markdown(
        '<div class="section-heading">How it works</div>',
        unsafe_allow_html=True
    )

    render_html("""
    <p class="section-description">
        A simple overview of the speech analysis process.
    </p>
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        step_card("STEP 01", "Upload Audio", "Choose a speech recording.")

    with col2:
        step_card("STEP 02", "Audio Analysis", "The uploaded recording is analyzed.")

    with col3:
        step_card("STEP 03", "Detection", "Possible speech disfluencies are identified.")

    with col4:
        step_card("STEP 04", "View Results", "See the analysis outcome.")

    # FUTURE SCOPE
    st.markdown(
        '<div class="section-heading">Where we plan to go next</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        feature_card(
            "🗂️",
            "Disfluency Classification",
            "Future work: identify different categories of disfluencies."
        )

    with col2:
        feature_card(
            "🌱",
            "Practice Exercises",
            "Future work: suggest suitable speech practice activities."
        )

    with col3:
        feature_card(
            "📈",
            "Progress Tracking",
            "Future work: provide a private view of practice history "
            "and progress trends."
        )

    # CALL TO ACTION
    st.markdown("""
    <div class="hero" style="margin-top:35px; padding:32px;">
        <h1 style="font-size:30px;">Ready to explore your speech?</h1>
        <p>
            Visit the Analyze Speech page to upload an audio recording
            and explore your speech analysis results.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # FOOTER
    st.markdown("""
    <div class="footer">
        FLUENCY COACH · SPEECH AWARENESS PLATFORM<br>
        Designed to support awareness, not replace professional evaluation.
    </div>
    """, unsafe_allow_html=True)
