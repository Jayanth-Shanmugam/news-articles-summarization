import streamlit as st
import pandas as pd

col1, col2 = st.columns([3, 1])
    
with col1:
    st.title('AGRIXCHANGE')
    st.divider()
    df = pd.read_csv('../notebooks/agrixchange_news_summaries.csv')
    for index, series in df.iterrows():
        st.markdown("### [{}]({})".format(series['title'], series['link']))
        st.markdown("*{}*".format(series['published']))
        st.markdown('**Keywords:  {}**'.format(series['content_keywords']))
        st.write(series['summary'])
        st.divider()
    