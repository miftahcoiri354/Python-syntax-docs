import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline

#Import dataframe from csv file
shampoo = pd.read_csv('shampoo.csv', index_col=[0], parse_dates=True, squeeze=True)
shampoo.head()
shampoo.plot(style='k.')
shampoo.size 
shampoo.describe()

#moving average with windown 10.
shampoo_ma = shampoo.rolling(window=10).mean() 
shampoo.plot()

#shift the base model into 1 line down 
shampoo_base = pd.concat([shampoo, shampoo.shift(1)], axis=1)
shampoo_base.columns = ['Actual_sales', 'Forecast_Sales']
shampoo_base.dropna(inplace=True)

from sklearn.metrics import mean_squared_error
import numpy as np 

shampoo_error = mean_squared_error(shampoo_base.Actual_Sales, shampoo_base.Forecast_Sales)
np.sqrt(shampoo_error) 
#Output: 108.237 --> baseline error

#ARIMA(p,d,q)
#ARIMA(2,0,0) #Autoregresive

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(shampoo)       # Q
# Q = 3, p = 2, d = 0-2
plot_pacf(shampoo)      # P

from statsmodels.tsa.arima_model import ARIMA

shampoo_train = shampoo[0:25]
shampoo_test  = shampoo[25:50]

shampoo_model = ARIMA(shampoo_train, order=(3,1,2))
shampoo_model_fit = shampoo_model.fit()
shampoo_model_fit.aic       #272.3891 --> lower == better
shampoo_forecast = shampoo_model_fit.forecast(steps=11)[0]
np.sqrt(mean_squared_error(shampoo_test, shampoo_forecast))
#130.92 --> error that my arima model
#108.237 --> compare to this baseline error
#It show that baseline model much more beter rather than our arima model

p_values = range(0,5)
d_values = range(0,3)
q_values = range(0,5)

import warnings
warnings.filterwarnings("ignore")
for p in p_values:
    for d in d_values:
        for d in q_values:
            order = (p,d,q)
            train, test = shampoo[0:25], shampoo[25:36]
            predictions = list()
            for i in range(len(test)):
                try:
                    model = ARIMA(train, order)
                    model_fit = model.fit(disp=0)
                    pred_y = model_fit.forecast()[0]
                    predictions.append(pred_y)
                    error = mean_squared_error(test, predictions)
                    print("ARIMA%s RMSE = %.2f" %(order, error))
                except:
                    continue   

# The best model
# ARIMA(3,2,3) RMSE = 144492.29
# sqrt(144492) = 120
# so we keep naif model 


