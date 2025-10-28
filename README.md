
# 🕒 Time Series Data Analyzer (Python + Streamlit)

An interactive web app that helps users analyze, visualize, and forecast time series data using **Python**, **Streamlit**, and **Statsmodels**.

## 🚀 Features
- 📂 Upload and clean your own time series dataset
- 🧹 Automatic preprocessing and handling of missing/non-numeric values
- 📊 Visualize trends, seasonal decomposition, ACF/PACF, and correlations
- 🔮 Perform forecasting with ARIMA and Prophet models
- 🧠 Built with modular Python code (`src/` folder)

## 🧱 Project Structure
```
Time-Series-Analyser/ 
│
├── app.py # Main Streamlit app
├── src/
│ ├── init.py
│ ├── preprocessing.py # Data cleaning and formatting
│ ├── visualization.py # All plotting functions
│ ├── modeling.py # Forecasting models (ARIMA, Prophet etc.)
│ └── utils.py # Helper functions
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

## 🧩 File Descriptions

| File | Description |
|------|--------------|
| **app.py** | The main entry point — runs the Streamlit web app that connects all modules. |
| **src/preprocessing.py** | Contains data preprocessing functions: CSV loading, missing value handling, normalization, resampling, etc. |
| **src/visualization.py** | Handles all data visualization — line plots, seasonal decomposition, correlation heatmap, ACF/PACF, and model diagnostics. |
| **src/forecasting.py** | Includes forecasting model implementations such as ARIMA, and can be extended with Prophet or LSTM later. |
| **src/utils.py** | Contains miscellaneous helper functions to support other modules. |
| **requirements.txt** | Specifies all the libraries needed to run the app. |
| **README.md** | Provides project introduction, setup guide, and usage instructions. |

---

## 🧠 Design Principles

- **Modular** → Each Python file handles one key functionality (preprocessing, visualization, forecasting).  
- **Scalable** → Easy to add new models or visualizations in the future.  
- **Maintainable** → Clean, readable structure with minimal code duplication.  
- **Reproducible** → Anyone can clone, install dependencies, and run the app immediately.

---

## 🧩 Installation

```bash
# Clone this repository
git clone https://github.com/<your-username>/Time_Series_Analyser.git

# Navigate to project folder
cd Time_Series_Analyser

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📸 Preview
