'''Police Dataset'''

import pandas as pd
data=pd.read_csv('Police Data.csv')
print(data)

'''Instruction ( For Data Cleaning )
1. Remove the column that only contains 
missing values'''
missing=data.isnull().sum()
print(missing)
remove=data.drop(columns='country_name', inplace=True)
print(remove)

'''Question ( Based on Filtering + Value Counts )
2. For Speeding , were Men or Women stopped 
more often ?'''
value=data[data['violation'] == 'Speeding'].driver_gender.value_counts()
print(value)

'''Question ( Groupby )
3. Does gender affect who gets searched during
a stop ?'''
group=data.groupby('driver_gender').search_conducted.sum()
print(group)

'''Question ( mapping + data-type casting )
4. What is the mean of stop_duration ?'''
data['stop_duration']=data['stop_duration'].map({'0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' : 45 })
print(data['stop_duration'])
mean=data['stop_duration'].mean()
print(mean)

'''Question ( Groupby , Describe )
5. Compare the age distributions for each 
violation'''
group=data.groupby('violation').driver_gender.describe()
print(group)