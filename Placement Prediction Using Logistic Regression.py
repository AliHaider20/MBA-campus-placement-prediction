#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score,precision_score
from sklearn.linear_model import LogisticRegression
import pickle


# In[89]:


# Loading the preprocessed Dataset


# In[90]:


df = pd.read_csv('cleaned_placement.csv')


# In[91]:


df.head()


# In[154]:


df.shape


# In[144]:


X = df.drop('status',axis=1) 
Y = df['status']
print(X.columns) # Features the Model will Train upon.
print(Y.head()) 
# spliting the data into 
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.9)


# In[155]:


# We will use Logistic Regression Classification  model which will fit an S-curve i.e probability curve.


# In[145]:


clf = LogisticRegression()


# In[ ]:


# Training  the Data 
clf.fit(x_train,y_train)


# In[146]:


# Predicting the value of Y i.e status on the test data.
y_pred = clf.predict(x_test)


# In[147]:


#pd.DataFrame({'Y Actual':y_test,'Y Pred':y_pred})


# In[148]:


# Hypothesis of Prediction vs Actual
pd.crosstab(y_test,y_pred)


# In[150]:


print("Accuracy\t",accuracy_score(y_test,y_pred))
print('Recall\t',recall_score(y_test,y_pred))
print('Precision\3t',precision_score(y_test,y_pred))


# In[176]:


print(pd.DataFrame({'Columns':x_test.columns,"Coefficient":model.coef_[0]}))


# In[156]:


# Pickle is used to save the model to be used for further use.
pickle.dump(clf,open('Model','wb'))

