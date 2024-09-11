import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

dataset = pd.read_excel("Superstore_USA.xlsx")
"""printing 2 rows of the datasets"""
print(dataset.head(2))
"""Displaying total row and columns of the dataset"""
print(dataset.shape)
"""checking missing values in the data sets"""
print(dataset.isnull().sum())
"""Filling the missing value with mean of specific column"""
dataset['Product Base Margin']= dataset['Product Base Margin'].fillna(dataset['Product Base Margin'].mean())

print(dataset.isnull().sum())

dataset_value_cnt= dataset['Order Priority'].value_counts()
print(dataset_value_cnt)
"""Data cleaning"""
# print(dataset['Order Priority'].unique())

dataset['Order Priority']= dataset['Order Priority'].replace("Critical ","Critical")
print(dataset['Order Priority'].unique())
dataset_value_cnt= dataset['Order Priority'].value_counts()
print(dataset_value_cnt)

# Order Priority

plt.figure(figsize=(5,3))
sns.countplot(x='Order Priority',data=dataset)
plt.title("Count of Order Priority")
plt.show()

# Ship Mode
ship_mode_cnt = dataset['Ship Mode'].value_counts()
print(ship_mode_cnt)
x = dataset['Ship Mode'].value_counts().index
print(x)
y = dataset['Ship Mode'].value_counts().values
print(y)
plt.figure(figsize=(5,4))
plt.pie(y,labels=x,startangle=60,autopct="%0.2f%%")
plt.legend(loc = 0)
plt.show()

sns.countplot(x= 'Ship Mode', data=dataset , hue='Product Category')
plt.show()

# Customer Segment

plt.figure(figsize=(6,4))
sns.countplot(x= 'Customer Segment', data=dataset)
plt.show()

# Product Category

plt.figure(figsize=(6,4))
sns.countplot(x= 'Product Category', data=dataset)
plt.show()

dataset.info()

dataset['Order Year']= dataset['Order Date'].dt.year
dataset.info()

order_year_value_count =dataset['Order Year'].value_counts()
print(order_year_value_count)

"""Year wise orders"""
plt.figure(figsize=(6,4))
sns.countplot(x= 'Order Year', data=dataset)
plt.show()

# """Product category wise profit """
sns.barplot(x='Product Category', y='Profit', data=dataset,estimator='sum')
plt.title("Product category wise profit")
plt.show()

"""Top 5 states on the basis of products order"""
top_five_states_cnt= dataset['State or Province'].value_counts()[:5]
print(top_five_states_cnt)


"""Product category wise Product Base Margin """
sns.barplot(x='Product Category', y='Product Base Margin', data=dataset,estimator='sum')
plt.title("Product category wise Product Base Margin")
plt.show()
















