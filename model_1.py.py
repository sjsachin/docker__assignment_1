from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
linreg=LinearRegression()
model_1=linreg.fit(x_train,y_train)
predict_values_1=model_1.predict(x_test)
model_1_score=r2_score(y_test,predicted_values_1)
