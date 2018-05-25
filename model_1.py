from sklearn.linear_model import LinearRegression
from exploratory import *
from sklearn.metrics import r2_score
linreg=LinearRegression()
model_1=linreg.fit(x_train,y_train)
predict_values_1=model_1.predict(x_test)
model_1_score=r2_score(y_test,predict_values_1)
