import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns([3, 3, 3])

with col2:
    st.markdown("<center><h1>Welcome to the News Summaries App!</h1></center>", unsafe_allow_html = True)
    st.image('landing_page_img.jpg')
    st.markdown("")