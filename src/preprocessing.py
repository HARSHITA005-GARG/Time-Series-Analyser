# src/preprocessing.py

import pandas as pd
import streamlit as st
import numpy as np

def load_data(filepath, date_column):
    """
    Load a time series dataset, parse dates, clean numeric columns, and set index.
    Automatically cleans and converts columns to numeric types where possible.
    """
    try:
        # Read CSV and parse date column
        df = pd.read_csv(filepath, parse_dates=[date_column])
        df.set_index(date_column, inplace=True)
        df.sort_index(inplace=True)

        # ✅ Clean numeric columns: remove junk, convert to float
        for col in df.columns:
            if df[col].dtype == 'object':  # only clean text-like columns
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(r'[^0-9.\-]', '', regex=True)  # remove ? , $ etc.
                )
                df[col] = pd.to_numeric(df[col], errors='coerce')

        # ✅ Drop rows with all NaNs after cleaning
        df.dropna(how='all', inplace=True)

        return df

    except Exception as e:
        raise ValueError(f"Error loading or cleaning data: {e}")



def handle_missing_values(df, method='interpolate'):
    """
    Handle missing values in the DataFrame.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        method (str): 'interpolate', 'drop', or 'fill_zero'.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    try:
        if method == 'interpolate':
            return df.interpolate()
        elif method == 'drop':
            return df.dropna()
        elif method == 'fill_zero':
            return df.fillna(0)
        else:
            raise ValueError("Invalid method for handling missing values.")
    except Exception as e:
        st.warning(f"⚠️ Missing value handling failed: {e}")
        return df


def resample_data(df, rule='D', agg_func='mean'):
    """
    Resample the DataFrame to a different frequency.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        rule (str): Resampling frequency (e.g., 'D' for daily, 'M' for monthly).
        agg_func (str): Aggregation function ('mean', 'sum', 'max', 'min').
    Returns:
        pd.DataFrame: Resampled DataFrame.
    """
    try:
        if agg_func == 'mean':
            return df.resample(rule).mean()
        elif agg_func == 'sum':
            return df.resample(rule).sum()
        elif agg_func == 'max':
            return df.resample(rule).max()
        elif agg_func == 'min':
            return df.resample(rule).min()
        else:
            raise ValueError("Invalid aggregation function for resampling.")
    except Exception as e:
        st.warning(f"⚠️ Resampling failed: {e}")
        return df


def normalize_data(df, method='min-max'):
    """
    Normalize numeric columns in the DataFrame.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        method (str): 'min-max' or 'z-score'.
    Returns:
        pd.DataFrame: Normalized DataFrame.
    """
    try:
        if method == 'min-max':
            return (df - df.min()) / (df.max() - df.min())
        elif method == 'z-score':
            return (df - df.mean()) / df.std()
        else:
            raise ValueError("Invalid normalization method.")
    except Exception as e:
        st.warning(f"⚠️ Normalization failed: {e}")
        return df


def difference_data(df, periods=1):
    """
    Apply differencing to make the time series stationary.
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        periods (int): Number of periods for differencing.
    Returns:
        pd.DataFrame: Differenced DataFrame.
    """
    try:
        return df.diff(periods=periods).dropna()
    except Exception as e:
        st.warning(f"⚠️ Differencing failed: {e}")
        return df
