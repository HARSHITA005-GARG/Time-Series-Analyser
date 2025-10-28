# src/utils.py
import pandas as pd
import numpy as np
import streamlit as st

def detect_frequency(df):
    """
    Automatically detect the frequency of a datetime index (daily, monthly, etc.)
    """
    try:
        freq = pd.infer_freq(df.index)
        return freq
    except Exception:
        return None


def fill_missing_dates(df):
    """
    Ensure continuous date index by filling missing dates and optionally forward-filling values.
    """
    try:
        full_range = pd.date_range(df.index.min(), df.index.max(), freq=pd.infer_freq(df.index) or 'D')
        df = df.reindex(full_range)
        df = df.ffill()  # forward-fill missing values
        return df
    except Exception as e:
        st.warning(f"Date filling failed: {e}")
        return df


def detect_outliers(df, column, z_thresh=3):
    """
    Detect outliers based on Z-score.
    Returns a dataframe with an extra 'is_outlier' column.
    """
    try:
        df = df.copy()
        z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
        df["is_outlier"] = z_scores > z_thresh
        return df
    except Exception as e:
        st.error(f"Outlier detection failed: {e}")
        return df


def display_outliers(df, column):
    """
    Plot the time series and highlight outliers in red.
    """
    import matplotlib.pyplot as plt

    try:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df.index, df[column], label="Data", color="tab:blue")
        outliers = df[df["is_outlier"]]
        ax.scatter(outliers.index, outliers[column], color="red", label="Outliers")
        ax.legend()
        ax.set_title(f"{column} with Outliers Highlighted")
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Could not plot outliers: {e}")
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