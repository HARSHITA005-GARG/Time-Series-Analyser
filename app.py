from src import load_data, plot_time_series, basic_analysis, plot_decomposition, forecast_arima, forecast_prophet
import streamlit as st

st.title("Time Series Analyser")
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    # Ask user which column is the date column
    st.markdown("### ⚙️ Data Settings")
    date_col = st.text_input("Enter the name of the date/time column:")

    if date_col:
        # ✅ Pass both arguments
        df = load_data(uploaded_file, date_col)

        st.success("✅ Data loaded successfully!")
        st.write("### 🧾 Preview of Data:")
        st.dataframe(df.head())
    else:
        st.info("👉 Please enter the name of the date column.")

    st.sidebar.header("Analysis Options")
    if st.sidebar.checkbox("Show Basic Analysis"):
        basic_analysis(df)

    if st.sidebar.checkbox("Plot Time Series"):
        column = st.sidebar.selectbox("Select Column to Plot", df.columns)
        plot_time_series(df, column)

    if st.sidebar.checkbox("Decompose Time Series"):
        column = st.sidebar.selectbox("Select Column to Decompose", df.columns)
        period = st.sidebar.number_input("Seasonal Period", min_value=1, value=12)
        plot_decomposition(df, column, period)

    if st.sidebar.checkbox("Forecast with ARIMA"):
        column = st.sidebar.selectbox("Select Column for ARIMA Forecast", df.columns)
        forecast_arima(df, column)

    if st.sidebar.checkbox("Forecast with Prophet"):
        column = st.sidebar.selectbox("Select Column for Prophet Forecast", df.columns)
        forecast_prophet(df, column)
        
else:
    st.info("Please upload a CSV file to get started.")
            
