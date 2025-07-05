# Sales_prediction
# Walmart Sales Forecasting

A time series forecasting solution to predict weekly sales for Walmart stores using the SARIMA model. This project includes exploratory data analysis, statistical modeling, and an interactive web application for real-time forecasting.

## Project Overview

This solution performs univariate time series forecasting on historical Walmart sales data. Starting with comprehensive exploratory data analysis, we preprocess the data to handle date formats, missing values, and seasonal patterns. The SARIMA model is applied with weekly seasonality to capture trends and fluctuations in sales data. An interactive Streamlit web application provides a user-friendly interface for generating forecasts.

## Features

- Interactive weekly sales forecasting by store
- SARIMA time series modeling with confidence intervals
- Visualization of actual vs forecasted sales
- Expandable forecast data tables
- Web-based interface built with Streamlit
- Support for forecasting up to 20 weeks

## Model Details

The solution uses SARIMA (Seasonal AutoRegressive Integrated Moving Average) for time series forecasting:

- **Model Type**: SARIMA with weekly seasonality
- **Seasonal Parameters**: Automatically optimized based on data characteristics
- **Stationarity**: Automatically detected and adjusted
- **Forecast Horizon**: Up to 20 weeks

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/walmart-sales-forecasting.git
cd walmart-sales-forecasting
```
2. Ensure your data file is placed in the correct location:
```
data/walmart.csv
```

## Usage

### Running the Streamlit Application

1. Navigate to the project directory
2. Run the Streamlit app:
```bash
streamlit run app/streamlit_app.py
```

3. Open your web browser and go to `http://localhost:8501`

### Using the Web Interface

1. Select a Walmart store from the dropdown menu
2. Choose the forecast duration (1-20 weeks) using the slider
3. Click "Generate Forecast" to run the SARIMA model
4. View the results in the interactive chart and expandable data table


## Data Requirements

The application expects a CSV file with the following columns:
- `Store`: Store identifier
- `Date`: Date in DD/MM/YYYY format
- `Weekly_Sales`: Weekly sales figures

## Dependencies

- Python 3.7+
- streamlit
- pandas
- matplotlib
- numpy
- scipy
- statsmodels
- jupyter (for notebooks)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Walmart sales dataset
- Streamlit framework for web application development
- SARIMA implementation using statsmodels library