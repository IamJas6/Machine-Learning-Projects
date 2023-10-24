'''Cars Dataset'''

'''Here, The data of different cars is given with their specifications.
This data is available as a CSV file. We are going to analyze this data set using the Pandas 
DataFrame.'''

import pandas as pd
car_data=pd.read_csv('Cars+Dataset.csv')
print(car_data)

'''1) Instruction ( For Data Cleaning )
• Find all Null Values in the dataset. If there is any null value in any column, then fill it with 
the mean of that column.
'''
null=car_data.isnull().sum()
print(null)
found=car_data['Cylinders'].fillna(car_data['Cylinders'].mean(), inplace=True)
print(found)

'''2) Question ( Based on Value Counts )
• Check what are the different types of Make are there in our dataset. And, what is the 
count (occurrence) of each Make in the data ?'''
value_counts=car_data['Make'].value_counts()
print(value_counts)

'''3) Instruction ( Filtering )
• Show all the records where Origin is Asia or Europe.'''
fil=car_data[car_data['Origin'].isin(['Asia','Europe'])]
print(fil)

'''4) Instruction ( Removing unwanted records )
• Remove all the records (rows) where Weight is above 4000.'''
remove=car_data[~(car_data['Weight'] > 4000)]
print(remove)

'''5) Instruction ( Apply() function is used on a column )
• Increase all the values of 'MPG_City' column by 3.'''
car_data['MPG_City']=car_data['MPG_City'].apply(lambda x:x+3)
print(car_data['MPG_City'])
