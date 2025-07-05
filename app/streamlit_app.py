import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from models import forecast_sarima

warnings.filterwarnings("ignore")
st.set_page_config(page_title="Walmart Sales Forecast",layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\mahil\OneDrive\Desktop\projects\walmart-sales-forecasting\data\walmart.csv")
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    return df

df = load_data()
st.title("Walmart Weekly Sales Forecast (SARIMA)")

store_ids = sorted(df['Store'].unique())
selected_store = st.selectbox("Select Store ID", store_ids)
steps = st.slider("Select Forecast Duration (Weeks)", min_value=1, max_value=20, value=10)
if st.button(" Generate Forecast"):
    store_df = df[df['Store'] == selected_store]
    weekly = store_df.groupby('Date')['Weekly_Sales'].sum().reset_index()
    weekly.set_index('Date', inplace=True)
    try:
        pred, conf_int, actual = forecast_sarima(weekly, steps=steps)
        result_df = pd.DataFrame({
            'Date': pred.index,
            'Actual': actual.values,
            'Forecast': pred.values,
            'Lower CI': conf_int.iloc[:, 0].values,
            'Upper CI': conf_int.iloc[:, 1].values
        })

        st.subheader(f" Forecast for Store {selected_store}")
        fig, ax = plt.subplots(figsize=(16, 8)) 
        ax.plot(result_df['Date'], result_df['Actual'], label='Actual', color='blue')
        ax.plot(result_df['Date'], result_df['Forecast'], label='Forecast', color='red')
        ax.fill_between(result_df['Date'], result_df['Lower CI'], result_df['Upper CI'], 
                        color='pink', alpha=0.3, label='Confidence Interval')
        ax.set_xlabel("Date")
        ax.set_ylabel("Weekly Sales")
        ax.set_title(f"Store {selected_store} - SARIMA Forecast")
        ax.legend()
        st.pyplot(fig)

        with st.expander(" View Forecast Table"):
            st.dataframe(result_df)

    except Exception as e:
        st.error(f" Forecasting failed: {e}")
