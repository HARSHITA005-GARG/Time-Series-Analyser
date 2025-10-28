# src/visualization.py
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import streamlit as st
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def plot_time_series(df, column):
    """
    Plot a basic time series line chart.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df.index, df[column], color='tab:blue')
    ax.set_title(f"{column} over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    st.pyplot(fig)

def plot_decomposition(df, column, period=12):
    """
    Decompose time series into trend, seasonality, and residuals.
    """
    try:
        result = seasonal_decompose(df[column], model='additive', period=period)
        fig = result.plot()
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Decomposition failed: {e}")
def plot_forecast(df, column, forecast_df):
    """
    Plot the original time series along with forecasted values.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df.index, df[column], label='Original', color='tab:blue')
    ax.plot(forecast_df['ds'], forecast_df['yhat'], label='Forecast', color='tab:orange')
    ax.fill_between(forecast_df['ds'], forecast_df['yhat_lower'], forecast_df['yhat_upper'], color='tab:orange', alpha=0.3)
    ax.set_title(f"{column} Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    ax.legend()
    st.pyplot(fig)
    
def plot_residuals(residuals):
    """
    Plot residuals of the forecast.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(residuals.index, residuals, color='tab:green')
    ax.set_title("Forecast Residuals")
    ax.set_xlabel("Date")
    ax.set_ylabel("Residuals")
    st.pyplot(fig)
    
def plot_acf_pacf(series, lags=30):
    """
    Plot ACF and PACF for a given time series.
    """


    fig, axes = plt.subplots(1, 2, figsize=(15, 4))
    plot_acf(series, lags=lags, ax=axes[0])
    plot_pacf(series, lags=lags, ax=axes[1])
    st.pyplot(fig)
    
def plot_model_diagnostics(model):
    """
    Plot diagnostics for a fitted time series model.
    """
    try:
        fig = model.plot_diagnostics(figsize=(15, 10))
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Model diagnostics plotting failed: {e}")
        
def plot_correlation_heatmap(df):
    """
    Plot a heatmap of correlations between different columns in the dataframe.
    """


    try:
        corr = df.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
        ax.set_title("Correlation Heatmap")
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Correlation heatmap plotting failed: {e}")
