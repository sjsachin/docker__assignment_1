from exploratory import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X2=data1[["Age","Treated","Weight","Height","ScaledBMI"]]
Y2=data1["SystolicBP"]

x_train_2,x_test_2,y_train_2,y_test_2=train_test_split(X2,Y2,test_size=0.4,random_state=4)
linreg=LinearRegression()
test_model=linreg.fit(x_train_2,y_train_2)
predict_values_2=test_model.predict(x_test_2)
model_2_score=r2_score(y_test,predict_values_2)
print(model_2_score)
