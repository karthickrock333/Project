#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/DELL/Downloads/tnq.csv')
df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[8]:


df.shape


# In[9]:


df.size


# In[10]:


df.ndim


# In[12]:


df.describe()


# In[14]:


df.sample()


# In[16]:


df.isnull().sum() #return no of null values in each columns


# In[17]:


df.nunique()


# In[19]:


df.index


# In[20]:


df.columns


# In[21]:


df.memory_usage()


# In[25]:


a=df.dropna()
a.shape


# In[30]:


df.nlargest(5,'Growth Rate')


# In[31]:


duplicates=df.duplicated()
duplicates.sum()


# In[36]:


df['Continent'].value_counts()


# In[37]:


df.dtypes


# In[ ]:




