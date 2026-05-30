import streamlit as st
from i18n import _


def render_sidebar():
    with st.sidebar:
        st.page_link("streamlit_app.py", label=_("nav_home"))
        st.page_link("pages/1_Analysis.py", label=_("nav_analysis"))
