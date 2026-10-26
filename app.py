"""Streamlit application entry point for Voltwise."""

import streamlit as st


st.set_page_config(page_title="Voltwise", layout="wide")
st.title("Voltwise")
st.caption("Predict smarter. Power better.")
st.info("Configure an electricity demand dataset to begin exploring forecasts.")find artifacts reports data -maxdepth 3 -type f -printf '%p (%k KB)\n' | sort