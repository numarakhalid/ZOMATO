#!/usr/bin/env python
# coding: utf-8

# 
# # exploratory data analysis(EDA)

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#file_encoding= 'utf8'

#input_fd=open(input_file_and_path, encoding=file_encoding, errors='blackslashreplace')
#pd.read_csv(input_fd, "C:\Users\mujjj\AppData\Local\Temp\Rar$DIa10856.37308.csv" )


# In[3]:


#df=pd.read_csv('C:\Users\mujjj\AppData\Local\Temp\Rar$DIa10856.37308.csv')


# In[4]:


#import csv
#df=pd.read_csv('C:\Users\mujjj\AppData\Local\Temp\Rar$DIa10856.37308.csv')


# In[5]:


df=pd.read_csv('zomato.CSV.csv', encoding='latin-1')


# In[6]:


df.head()


# In[7]:


df.columns


# In[8]:


df.info


# # we find in Data analysis
# 
# 1.  missing values
# 2.  explore about the numerical variables
# 3.  explore about categorical variables
# 4.  finding relation between feature

# In[9]:


df.isnull().sum()


# In[10]:


df.shape


# In[11]:


df.describe()


# In[12]:


[features for features in df.columns if df[features].isnull().sum()>0]
                                


# In[13]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[14]:



df_country=pd.read_excel('country-code.xlsx')


# In[15]:


df_country.head()


# In[16]:


df.columns


# In[17]:


final_df=pd.merge(df,df_country,on='Country Code', how='left')


# In[18]:


final_df


# In[19]:


final_df.dtypes


# In[20]:


final_df.columns


# In[21]:


country_names=final_df.Country.value_counts().index


# In[22]:


country_names


# In[23]:


country_val=final_df.Country.value_counts().values


# In[24]:


country_val


# In[25]:


## pie chart


# In[26]:


#from matplotlib import pyplt as plt
#%matplotlib inline
#for top three country
plt.pie(country_val[:3],labels=country_names[:3],autopct="%1.2f%%")


# In[27]:


final_df.columns


# In[28]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[29]:


ratings


# In[30]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x="Aggregate rating",y="Rating count",data=ratings)


# In[31]:


sns.barplot(x="Aggregate rating",y="Rating count",hue='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])


# Observation
# 
# 1. Not rated Is very high
# 2.  2.1 to 2.5 rating is maximum
# 

# In[35]:


sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[34]:


ratings


# In[38]:


final_df.columns


# In[43]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# In[46]:


#find which currancy is used in which country
final_df.groupby(['Country','Currency']).size().reset_index()


# In[47]:


#which country do have online deliveries
final_df.columns


# In[48]:


final_df.groupby(['Country','Has Online delivery']).size().reset_index()


# In[55]:


final_df[final_df['Has Online delivery']=='yes'].Country.value_counts()


# OBSERVATION
# 1. online delivery is in UAE and India

# In[64]:


#creating pie chart for cities distribution


# In[67]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[69]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# In[70]:


final_df.columns


# In[71]:


# find top 10 cuisines


# In[79]:


final_df.Cuisines.value_counts().head(10)


# In[ ]:




