import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Explorer Pro")
st.write("This is the csv data explorer built be Madbe")
uploaded_file=st.file_uploader("Upload the file: ",type="csv")


if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader("Statistics")
    st.dataframe(df.describe())

    st.subheader("Null values")
    st.write(df.isnull().sum().reset_index().rename(columns={0:'Type'}))

    numeric_df=df.select_dtypes(include=np.number)
    st.subheader("Correlation Matrix")
    corr = numeric_df.corr()
    fig,ax=plt.subplots()
    sns.heatmap(corr,annot=True,cmap='coolwarm',ax=ax)
    st.pyplot(fig)

    col=st.selectbox("Choose a numeric column for histogram",numeric_df.columns)
    fig2,ax2=plt.subplots()
    sns.histplot(df[col].dropna(),kde=True)
    st.pyplot(fig2)

