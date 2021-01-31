import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline

f_birth = pd.read_csv("daily-total-female-births-in-cal.csv", index_col=[0], parse_dates=[0], squeeze=True)
f_birth.head()
f_birth.size 
f_birth.tail() 
f_birth.describe()
f_birth.plot()

#try to doing moving average in 20 windows
f_birth_mean = f_birth.rolling(window=20).mean()
f_birth.plot()
f_birth_mean.plot()

#create base dataset by shift the value column into 1 row down
value = pd.DataFrame(series_value)
birth_df = pd.concat([value, value.shift(1)], axis=1)
birth_df.columns = ['actual_birth', 'forecast_birth']
birth_test = birth_test[1:365]
birth_df.head()

#find th mean_squared_error from base data
from sklearn.metrics import mean_squared_error
import numpy as np

birth_error = mean_squared_error(birth_test.Actual_birth, birth_test.Forecast_birth)
np.sqrt(birth_error)
#Output: 9.177 You need to find any model with MsE less than base mse

#ARIMA - Auto-Regresive (p) Integrated (d) Moving Average (q)
from statsmodels.graphics.tsaplots import plot_act, plot_pacf

#plot_acf is to identify parameter q (ARIMA-p,d,q)
plot_acf(f_birth) 
#plot_pacf is to identify parameter p 
plot_pacf(f_birth) 
# p = 2,3     d = 0     q = 3,4
birth_train = f_birth[0:330]
birth_test = f_birth[330:365]

#Build model using ARIMA statsmodel
from statsmodels.tsa,arima_model import ARIMA

birth_model = ARIMA(birth_train, order=(2,1,3))
birth_model_fit = birth_model.fit()
np.sqrt(birth_model_fit.aic)
#Output: 47.22 (Not Good)

birth_forecast = birth_model_fit.forecast(steps=35)[0]
np.sqrt(mean_squared_error(birth_test,birth_forecast))
#output: 6.860 if we compare with the base mse, it looks better




