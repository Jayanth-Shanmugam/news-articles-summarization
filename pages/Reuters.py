import streamlit as st
import pandas as pd

col1, col2 = st.columns([3, 1])
option = None

with col2:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    option = st.selectbox('', ['Crude Oil', 'Biofuel'])
    
with col1:
    st.title('REUTERS')
    st.divider()
    if option == 'Crude Oil':
        df = pd.read_csv('crude_oil_summary_new.csv')
        for index, series in df.iterrows():
            st.markdown("### [{}]({})".format(series['title'], series['links']))
            st.markdown("*{}*".format(series['published']))
            st.markdown('**Keywords:  {}**'.format(series['keywords']))
            st.write(series['summaries'])
            st.divider()
    
    if option == 'Biofuel':
        df = pd.read_csv('biofuel_summary_new.csv')
        for index, series in df.iterrows():
            st.markdown("### [{}]({})".format(series['title'], series['links']))
            st.markdown("*{}*".format(series['published']))
            st.markdown('**Keywords:  {}**'.format(series['keywords']))
            st.write(series['summaries'])
            st.divider()
    
