import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score,precision_score
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('cleaned_placement.csv')
df.head()
df.shape

X = df.drop('status',axis=1) 
Y = df['status']
print(X.columns) # Features the Model will Train upon.
print(Y.head()) 
# spliting the data into 
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.9)

clf = RandomForestClassifier()

# Training Phase 
clf.fit(x_train,y_train)

# Testing Phase
y_pred = clf.predict(x_test)

# Hypothesis of Prediction vs Actual
pd.crosstab(y_test,y_pred)

print("Accuracy\t",accuracy_score(y_test,y_pred))
print('Recall\t',recall_score(y_test,y_pred))
print('Precision\3t',precision_score(y_test,y_pred))
print(pd.DataFrame({'Columns':x_test.columns,"Coefficient":model.coef_[0]}))

pickle.dump(clf,open('Model','wb'))
