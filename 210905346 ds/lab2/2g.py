import pandas as pd 
import numpy as np 
import openpyxl
import matplotlib.pyplot as plt 
 
df = pd.read_excel('German_Credit_for_Week2.xls', engine='openpyxl')  
 
print(df.head()) 
print(df.columns) 
 
plt.scatter(df['Creditability'],df['CreditAmount'])  
plt.xlabel('Creditability')  
plt.ylabel('CreditAmount') 
 
df['CreditAmount'].hist()  
 
plt.boxplot(df,notch=True) 
f = df['Creditability'].value_counts()  
f.plot(kind='bar') 
f.plot(kind='pie') 
f = pd.crosstab(df['Creditability'],df['DurationOfCreditInMonths'])  
f.plot(kind='bar') 
 
plt.show()