import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Poll Results Visualizer")

file = st.file_uploader("Upload Poll Data CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write(df.head())

    st.subheader("Poll Distribution")
    fig = px.pie(df, names='Option', title='Poll Results')
    st.plotly_chart(fig)

    st.subheader("Satisfaction Level")
    fig2 = px.bar(df, x='Option', y='Satisfaction', color='Option')
    st.plotly_chart(fig2)
