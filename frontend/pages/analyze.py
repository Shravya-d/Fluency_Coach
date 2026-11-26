
import streamlit as st

from components import render_html
from components.header import page_header
from services.api_client import analyze_audio
from config import ALLOWED_AUDIO_TYPES


def show_analyze():

    page_header(
        "Speech Analysis",
        "Upload a speech recording to identify possible disfluencies."
    )

    render_html("""
    <div class="info-panel">
        <p>
        <b>Before uploading</b><br>
        Choose a quiet environment when recording your speech.
        Speak naturally and make sure your audio is clear.
        Upload a short recording in WAV or MP3 format.
        </p>
    </div>
    """)

    # AUDIO UPLOAD
    st.markdown(
        '<div class="section-heading">01 · Upload your audio</div>',
        unsafe_allow_html=True
    )

    audio_file = st.file_uploader(
        "Choose your speech recording",
        type=ALLOWED_AUDIO_TYPES,
        help="Supported formats: WAV and MP3."
    )

    if audio_file is not None:
        audio_bytes = audio_file.getvalue()

        # AUDIO PREVIEW
        st.markdown(
            '<div class="section-heading">02 · Preview your recording</div>',
            unsafe_allow_html=True
        )

        st.audio(
            audio_bytes,
            format=audio_file.type
        )

        file_size = len(audio_bytes) / 1024

        st.success("Your audio file is ready for analysis.")
        st.caption(f"File name: {audio_file.name}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("File size", f"{file_size:.1f} KB")

        with col2:
            st.metric("File format", audio_file.name.split(".")[-1].upper())

        st.markdown("---")

        # ANALYSIS
        st.markdown(
            '<div class="section-heading">03 · Analyze your speech</div>',
            unsafe_allow_html=True
        )

        if st.button(
            "✨ Analyze My Speech",
            use_container_width=True
        ):

            with st.spinner("Analyzing your speech..."):

                result = analyze_audio(audio_file)

            if result.get("status") == "error":

                st.warning(
                    result.get(
                        "message",
                        "Analysis is currently unavailable."
                    )
                )

                st.info(
                    "If the issue persists, check that the backend service "
                    "is available."
                )

            elif "possible_disfluency" in result:

                st.markdown("### Analysis Result")

                if result["possible_disfluency"]:

                    st.warning(
                        "Possible speech disfluency detected."
                    )

                else:

                    st.success(
                        "No possible speech disfluency detected."
                    )

                st.write(
                    result.get(
                        "message",
                        "Analysis completed."
                    )
                )

            else:

                st.error(
                    "Unexpected response received from the backend."
                )

    else:

        st.info(
            "Upload an audio file to see its preview and begin analysis."
        )

    render_html("""
    <div class="footer">
        FLUENCY COACH · SPEECH AWARENESS PLATFORM<br>
        This tool supports speech awareness and is not a medical diagnosis.
    </div>
    """)
