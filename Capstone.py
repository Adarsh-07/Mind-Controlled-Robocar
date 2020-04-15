#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split,GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.svm import SVR
from sklearn import preprocessing
from sklearn import utils


# In[2]:


cap_train=pd.read_csv("capstone.csv",low_memory=False)
cap_test=pd.read_csv("cap_test.csv",low_memory=False)


# In[3]:


cap_train.head()


# In[4]:


cap_train.shape,cap_test.shape


# In[5]:


cap_train.isnull().sum()


# In[6]:


cap_test.isnull().sum()


# In[7]:


cap_train['action'].value_counts()


# In[8]:


le1 = LabelEncoder()
le2 = LabelEncoder()


# In[9]:


X_Train = cap_train.iloc[:,[1,2]].values


# In[10]:


print(X_Train)


# In[11]:


Y_Train= cap_train.iloc[:,4].values


# In[12]:


print(Y_Train)


# In[13]:


X_Test=cap_test.iloc[:,[1,2]].values


# In[14]:


print(X_Test)


# In[15]:


pd.DataFrame(Y_Train).head(100)


# In[16]:


pd.DataFrame(X_Train).head(100)


# In[17]:


pd.DataFrame(X_Test).head(100)


# In[18]:


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion = 'entropy')


# In[19]:


print(Y_Train)
print(utils.multiclass.type_of_target(Y_Train))
print(utils.multiclass.type_of_target(Y_Train))


# In[20]:


clf.fit(X_Train, Y_Train)


# In[21]:


Y_pred =  clf.predict(X_Test)


# In[22]:


Y_pred


# In[23]:


pd.DataFrame(Y_pred,columns=['Movement']).to_excel('Output_RF.xlsx',index=False)


# In[24]:


X_Train[:,0] = le1.fit_transform(X_Train[:,0])


# In[25]:


X_Train[:,1] = le1.fit_transform(X_Train[:,1])


# In[26]:


X_Test[:,0] = le2.fit_transform(X_Test[:,0])


# In[27]:


X_Test[:,1] = le2.fit_transform(X_Test[:,1])


# In[28]:


sc = StandardScaler()


# In[29]:


X_Train = sc.fit_transform(X_Train)


# In[30]:


X_Test = sc.transform(X_Test)


# In[31]:


Y_Train = Y_Train.reshape((len(Y_Train)),1)


# In[32]:


Y_Train[:,0] = le1.fit_transform(Y_Train[:,0])


# In[33]:


Y_Train = sc.fit_transform(Y_Train)


# In[34]:


Y_Train = Y_Train.ravel()


# In[35]:


pd.DataFrame(X_Train).head(100)


# In[36]:


pd.DataFrame(Y_Train).head(100)


# In[37]:


pd.DataFrame(X_Test).head(100)


# In[38]:


n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
max_features = ['auto', 'sqrt']
max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]
min_samples_split = [2, 5, 10, 15, 100]
min_samples_leaf = [1, 2, 5, 10]


# In[39]:


rf_grid={'n_estimators':n_estimators,'max_features':max_features,'max_depth':max_depth,
         'min_samples_split':min_samples_split,'min_samples_leaf':min_samples_leaf}


# In[40]:


rf =RandomForestRegressor()


# In[41]:


best_rf_tree=RandomizedSearchCV(estimator=rf,param_distributions=rf_grid,n_jobs=-1,cv=3,scoring='neg_mean_squared_error')


# In[42]:


best_rf_tree.fit(X_Train,Y_Train)


# In[43]:


rf_predict =sc.inverse_transform(best_rf_tree.predict(X_Test))


# In[44]:


rf_predict


# In[45]:


rf.fit(X_Train,Y_Train)


# In[46]:


rf_predict1=sc.inverse_transform( rf.predict(X_Test))


# In[47]:


rf_predict1


# In[ ]:




