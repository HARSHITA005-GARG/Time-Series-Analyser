# src/analysis.py
import streamlit as st

def basic_analysis(df):
    """
    Display basic information and statistics for a time series dataset.
    """
    st.markdown("### 📘 Data Summary")
    st.write(df.describe())

    st.markdown("### 🧭 Missing Values")
    st.write(df.isnull().sum())

    st.markdown("### 🕒 Date Range")
    st.write(df.index.min(), "→", df.index.max())
    
    st.markdown("### 📊 Data Types")
    st.write(df.dtypes)
    st.markdown("### 🔍 Head of Dataset")
    
    st.write(df.head())
    st.markdown("### 🔍 Tail of Dataset")
    st.write(df.tail())
