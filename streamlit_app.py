from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="APAC Helpdesk Zendesk Dashboard", layout="wide")

html = Path(__file__).parent.joinpath("Zendesk_Dashboard.html").read_text(encoding="utf-8")
components.html(html, height=2400, scrolling=True)
