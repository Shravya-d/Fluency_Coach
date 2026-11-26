import streamlit as st


def render_html(markup: str) -> None:
    st.markdown(" ".join(markup.split()), unsafe_allow_html=True)