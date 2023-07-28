import streamlit as st
import pandas as pd

col1, col2, col3= st.columns([3, 3, 3])

with col2:
    st.markdown("<center><h1>Welcome to the News Summaries App!</h1></center>", unsafe_allow_html = True)
    st.image('landing_page_img.jpg')
    st.markdown("")
    st.markdown("<center><h2>How Do I Use the App?</h2></center>", unsafe_allow_html=True)
    st.markdown("<ul><li><h3>Click the arrow on the top left corner to access articles from the various news websites</h3></li><li><h3>Click on the title to visit the original article</h3></li><li><h3>Select a keyword from the dropdown menu on the right to view news articles related to that keyword</h3></li></ul>", unsafe_allow_html=True) 
                 

    
