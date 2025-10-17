#Complete Python Pandas Data Science Tutorial! (2025 Updated Edition)
#https://www.youtube.com/watch?v=2uvysYbKdjM

#Info: Can use VSCode, Cursor, PyCharm
#GitHub PUBLIC Path (Keith Galli) https://github.com/KeithGalli/complete-pandas-tutorial

#------------------
#Installation Steps
#------------------
#python -m venv venv
#.\venv\Scripts\activate
#pip install numpy
#pip install openpyxl
#pip install pandas
#pip install pyarrow
#pip install pyjanitor
#pip install ipykernel

import pandas as pd
import openpyxl

'''
#df = pd.read_csv('orders.csv') #Reading CSV file
#df = pd.read_excel('orders.xlsx') #Reading Excel file   
df = pd.read_json('orders.json') #Reading JSON file
print(df)   
print(df.head())  #First 5 rows
print(df.tail())  #Last 5 rows  
print(df.shape)  #Rows and Columns
print(df.columns)  #Column Names    
print(df.info())  #Info about data
print(df.describe())  #Statistical Summary of numerical columns
print(df['OrderID'])  #Accessing a column (Case Sensitive)
print(df[['OrderID','Quantity']])  #Accessing multiple columns (Case Sensitive)
print(df.iloc[0])  #Accessing a row by index    
'''

'''
data ={
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)
'''

