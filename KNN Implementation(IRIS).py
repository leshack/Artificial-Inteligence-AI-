#!/usr/bin/env python
# coding: utf-8

# In[10]:


#importing the required libraries
import sklearn
import numpy as np #working with arrays. 
import pandas as pd #data manipulation library that is necessary for every aspect of data analysis or machine learning.


# In[2]:


#Loading the dataset
dataset = pd.read_csv("C:/Users/Admin/OneDrive - Strathmore University/school work/STRATHMORE UNIVERSITY(BBIT)/BBIT EXEMPT 3.2/Artificial Intelligencence (AI)/project/KNN/Iris.csv")


# In[3]:


#Exploratory Data Analysis
dataset.shape #returns the orientation of the dataset i.e number of columns and rows.


# In[4]:


dataset.head(5) #returns part of the dataset with agiven number of colums


# In[5]:


dataset.describe() #returns some statistical information for the data


# In[6]:


#Number of rows belonging to each class
dataset.groupby('Species').size()


# The dataset contain six columns: Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm and Species. 
# The actual features are described by columns 1-4. Last column contains labels of samples.
# There is need to split data into two arrays: X (features) and y (labels).

# In[7]:


feature_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm','PetalWidthCm']
X = dataset[feature_columns].values
y = dataset['Species'].values
# Alternative way of selecting features and labels arrays:
# X = dataset.iloc[:, 1:5].values
# y = dataset.iloc[:, 5].values


# The labels here are categorical. The KNeighborsClassifier does not accept string labels. We need to use LabelEncoder to transform them into numbers. Iris-setosa correspond to 0, Iris-versicolor correspond to 1 and Iris-virginica correspond to 2.

# In[8]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)


# In[12]:


#Spliting dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[13]:


#Data Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


plt.figure()
dataset.drop("Id", axis=1).boxplot(by="Species", figsize=(15, 10))
plt.show()


# In[15]:


#KNN Predicions
# Fitting clasifier to the Training set
# Loading libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score

# Instantiate learning model (k = 3)
classifier = KNeighborsClassifier(n_neighbors=3)

# Fitting the model
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)


# In[16]:


#Model Evaluation
#Building a Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
cm


# In[17]:


#Calculating Model Accuracy
accuracy = accuracy_score(y_test, y_pred)*100
print('Accuracy of our model is equal ' + str(round(accuracy, 2)) + ' %.')


# In[21]:


#Predict Output
x1=float(input("Enter Sepal Lenth in CM:"))
x2=float(input("Enter Sepal Width in CM:"))
x3=float(input("Enter Petal Lenth in CM:"))
x4=float(input("Enter Petal Lenth in CM:"))
predicted_class= classifier.predict([[x1,x2,x3,x4]])#x1,x2,x3,x4 are the different values entered by users for the features
#print(predicted)
if predicted_class==0:
    print("...The Species is: Iris-setosa...")
elif predicted_class==1:
     print("...The Species is: Iris-versicolor...")
elif predicted_class==2: 
    print("...The Species is: Iris-virginica...")
else:
    print("...Class out of Range...")


# *Conclusions
# The KNN algorithm is very intuitive and easy to understand
# Its versatile-Can be used for classification or regression. 
# The training time is minimal, the model doesn’t actually learns or generalizes
# The testing time can be very long, because the algorithm loops over the whole training dataset and calculates the distances (distance calculation can be a hard work, based on the type of distance metric and based on the type of the dataset)
# For small K values the algorithm can be noise sensitive and easy to overfit
# The data set should numeric or a distance metrics should exist to calculate distances between points
# Doesn’t perform too well on unbalanced data
# Sensitive to irrelevant features and the scale of the data.

# In[ ]:




