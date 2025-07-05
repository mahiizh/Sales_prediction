from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd

def forecast_sarima(store_df, steps=20):
    store_df = store_df.sort_index()
    train = store_df.iloc[:-steps]
    test = store_df.iloc[-steps:]

    model = SARIMAX(train['Weekly_Sales'],
                    order=(1, 0, 1),
                    seasonal_order=(1, 1, 1, 52),
                    enforce_stationarity=False,
                    enforce_invertibility=False)
    results = model.fit(disp=False)

    forecast = results.get_forecast(steps=steps)
    pred = forecast.predicted_mean
    conf_int = forecast.conf_int()
    return pred, conf_int, test['Weekly_Sales']
