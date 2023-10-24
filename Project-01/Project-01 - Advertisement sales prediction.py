import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

#Collecting Dataset
dataset=pd.read_csv("DigitalAd_dataset.csv")
print(dataset.shape)
print(dataset.head(10))
print(dataset.tail(10))

#Segragating data into X and Y
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(x)
print(y)

#splitting data to train and test
X_train, X_test, Y_train, Y_test =  train_test_split(x,y,test_size=0.25,random_state=0)


#Feature scaling
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
print(X_train)
print(X_test)

#Training model
model=LogisticRegression(random_state=0)
model.fit(X_train,Y_train)
print(model)

#Prediction, new data
age=int(input("enter new age = "))
sal=int(input("enter new salary = "))
new_data=[[age,sal]]
new_pred=model.predict(sc.transform(new_data))
print(new_pred)
if new_data == 1:
    print("customer buys product")
else:
    print("not interested to buy")


#Predict all Test data
y_pred=model.predict(X_test)
#reshaoing array to 1
print(np.concatenate((y_pred.reshape(len(y_pred),1),Y_test.reshape(len(Y_test),1)),1))

#Evaluate model, conclusion matrix(accuracy)
cm=confusion_matrix(Y_test, y_pred)
print(cm)
print(f"Accuracy of the test model is {(accuracy_score(Y_test, y_pred)*100)}")