import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns([3, 1])
    
with col1:
    st.title('GRAINTRADE')
    st.divider()
    df = pd.read_csv('graintrade_summaries.csv')
    for index, series in df.iterrows():
        st.markdown("### [{}]({})".format(series['title'], series['link']))
        st.markdown("*{}*".format(series['published']))
        st.markdown('**Keywords:  {}**'.format(series['keywords']))
        st.write(series['summary'])
        st.divider()
    
