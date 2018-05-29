import numpy as np
import pandas as pd
data1=pd.read_csv("Ex03_SystolicBP_Regreesion.csv")
from sklearn.model_selection import train_test_split
X=data1.iloc[:,0:-1]
Y=data1.iloc[:,-1]
plt.figure(figsize=(15,10.5))
plot_count = 1
for feature in list(data1.columns)[:-1]:
        plt.subplot(3,3,plot_count)
        plt.scatter(data1[feature], data1["SystolicBP"])
        plt.xlabel(feature.replace('_',' ').title())
        plt.ylabel('SystolicBP')
        plot_count+=1
plt.show() 
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.4,random_state=4)
