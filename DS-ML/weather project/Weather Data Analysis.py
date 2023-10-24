import pandas as pd

'''The Weather Dataset'''
data=pd.read_csv('Weather+Dataset.csv')
print(data)

#How to Analyze DataFrames ?
#.head()
#It shows the first N rows in the data (by default, N=5).
head=data.head()
print(head)

#.shape
#It shows the total no. of rows and no. of columns of the dataframe
shape=data.shape
print(shape)

#.index
#This attribute provides the index of the dataframe
index=data.index
print(index)

#.columns
#It shows the name of each column
each_column_name=data.columns
print(each_column_name)

#.dtypes
#It shows the data-type of each column
datatype=data.dtypes
print(datatype)

#.unique()
#In a column, it shows all the unique values. It can only be applied on a single column, not on the whole dataframe.
unique_values=data['Weather'].unique()
print(unique_values)

#.nunique()
#It shows the total no. of unique values in each column. It can be applied on a single column as well as on a whole dataframe.
unique_values_each_column=data.nunique()
print(unique_values_each_column)

#.count()
#It shows the total no. of non-null values in each column. It can be applied on a single column as well as on a whole dataframe.
non_null_values=data.count()
print(non_null_values)

#.value_counts()
#In a column, it shows all the unique values how many times it has been repeated. It can only be applied on single column.
value_counts=data['Weather'].value_counts()
print(value_counts)

#.info()
#Provides basic information about the dataframe.
info=data.info()
print(info)

'''questions:'''

#Q) 1. Find all the unique 'Wind Speed' values in the data.
#Ans
unique=data['Wind Speed_km/h'].unique()
print(unique)

#Q) 2. Find the number of times when the 'Weather is exactly Clear'.
#we can do it by 3 methods
#1.value_counts()
clear=data['Weather'].value_counts()
print(clear)

#2.Filtering
filter=data[data['Weather'] == 'Clear']
print(filter)

#3.groupby()
grouping=data.groupby('Weather').get_group('Clear')
print(grouping)

#Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.
wind=data[data['Wind Speed_km/h'] == 4]
print(wind)

#Q. 4) Find out all the Null Values in the data.
null=data.isnull().sum()
print(null)
#or
null=data.isna().sum()
print(null)
#or
null=data.notnull().sum()
print(null)

#Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
rename=data.rename(columns={'Weather' : 'Weather Condition'}, inplace=True)
print(data.head())

#Q.6) What is the mean 'Visibility' ?
mean_visib=data.Visibility_km.mean()
print(mean_visib)

#Q. 7) What is the Standard Deviation of 'Pressure' in this data?
std=data.Press_kPa.std()
print(std)

#Q. 8) Whats is the Variance of 'Relative Humidity' in this data ?
var=data['Rel Hum_%'].var()
print(var)

#Q. 9) Find all instances when 'Snow' was recorded.
#3 methods
#1.value_counts()
snow=data['Weather Condition'].value_counts()
print(snow)

#2.Filtering
fil=data[data['Weather Condition'] == 'Snow']
print(fil)

# str.contains
str=data[data['Weather Condition'].str.contains('Snow')]
print(str)

#Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
ins=data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
print(ins)

#Q. 11) What is the Mean value of each column against each 'Weather Conditon' ?
#mean=data.groupby('Weather Condition').mean()
#print(mean)

#Q. 12) What is the Minimum & Maximum value
#of each column against each 'Weather
#Conditon' ?
min=data.groupby('Weather Condition').min()
print(min)
max=data.groupby('Weather Condition').max()
print(max)

#. 13) Show all the Records where Weather Condition is Fog.
fog=data[data['Weather Condition'] == 'Fog']
print(fog)

#Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
inst=data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]
print(inst)

#Q. 15) Find all instances when :
#A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
#                      or
#B. 'Visibility is above 40
inst=data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]
print(inst)

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 9000)