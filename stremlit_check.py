import streamlit as st
import pandas as pd


header = st.container()
dataset = st.container()


def get_data(filename):
    data = pd.read_csv(filename)
    return data


with header:
    st.markdown("<h1 style='text-align: center; color: red;'>Source feed statistics dashboard</h1>",
                unsafe_allow_html=True)

with dataset:
    st.subheader('Source feed statistics')
    source_data = get_data('data/source_feed_stat.csv')

    st.write(source_data)

    feed_stat = pd.DataFrame(source_data['Кол-во новостей'].head(15))
    st.bar_chart(feed_stat)
