import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns([3, 1])
option = None

df = pd.read_csv('reuters_summaries.csv')

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
        #df = pd.read_csv('crude_oil_summary_new.csv')
        df_crude = df[df['keyword']=='crude oil']
        for index, series in df_crude.iterrows():
            st.markdown("### [{}]({})".format(series['title'], series['link']))
            st.markdown("*{}*".format(series['published']))
            st.markdown('**Keywords:  {}**'.format(series['keywords']))
            st.write(series['summary'])
            st.divider()
    
    if option == 'Biofuel':
        #df = pd.read_csv('biofuel_summary_new.csv')
        df_bio = df[df['keyword']=='biofuel']
        for index, series in df.iterrows():
            st.markdown("### [{}]({})".format(series['title'], series['link']))
            st.markdown("*{}*".format(series['published']))
            st.markdown('**Keywords:  {}**'.format(series['keywords']))
            st.write(series['summary'])
            st.divider()
    
