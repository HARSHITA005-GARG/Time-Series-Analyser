# src/forecasting.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
import streamlit as st
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


def forecast_arima(df, column, order=(1,1,1), steps=10):
    """
    Forecast future values using ARIMA.
    """
    try:
        model = ARIMA(df[column], order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df.index, df[column], label='Historical')
        ax.plot(pd.date_range(df.index[-1], periods=steps+1, freq='D')[1:], forecast, label='Forecast', color='tab:orange')
        ax.legend()
        st.pyplot(fig)

        st.write("### 📅 Forecasted Values")
        st.write(forecast)
    except Exception as e:
        st.error(f"ARIMA Forecasting failed: {e}")

def forecast_prophet(df, column, periods=30):
    """
    Forecast future values using Prophet.
    """
    try:
        prophet_df = df.reset_index().rename(columns={df.index.name: 'ds', column: 'y'})
        model = Prophet()
        model.fit(prophet_df)
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)

        st.write("### 📅 Prophet Forecast")
        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

        fig1 = model.plot(forecast)
        st.pyplot(fig1)
        fig2 = model.plot_components(forecast)
        st.pyplot(fig2)
    except Exception as e:
        st.error(f"Prophet Forecasting failed: {e}")
def evaluate_forecast(actual, predicted):
    """
    Evaluate forecast accuracy using MAE and RMSE.
    """

    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    st.write(f"### 📊 Forecast Evaluation")
    st.write(f"Mean Absolute Error (MAE): {mae}")
    st.write(f"Root Mean Squared Error (RMSE): {rmse}")
    
def plot_forecast_results(df, column, forecast_df):
    """
    Plot forecast results alongside actual data.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df.index, df[column], label='Actual', color='tab:blue')
    ax.plot(forecast_df['ds'], forecast_df['yhat'], label='Forecast', color='tab:orange')
    ax.fill_between(forecast_df['ds'], forecast_df['yhat_lower'], forecast_df['yhat_upper'], color='tab:orange', alpha=0.3)
    ax.set_title(f"{column} Forecast vs Actual")
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    ax.legend()
    st.pyplot(fig)
    

