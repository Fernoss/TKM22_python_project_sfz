import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Rest of your code
df = pd.read_excel(
    'WorkPlaceSatisfactionSurveyData.xlsx')

# To list the first few lines
print(df.head())

# To see if there are any missing values in the data
print(df.isnull().sum())

# To delete 'number', 'healthcare', 'gym' and 'muscleCare'
columns_to_drop = ['number', 'healtcare', 'gym', 'muscleCare', 'holidayCabin']
df = df.drop(columns_to_drop, axis=1)
# Check the change
print(df.head())  # WORKS!

# Summary of the data so far
print(df.info())

# Testing begins ->
print('************* Testing begins here! *************')

for var in df:
    print(var, df[var].unique())

# Testing salaries
print("Top 3 largest salaries:")
print(df.nlargest(n=3, columns='salary'))

print("\nTop 3 smallest salaries:")
print(df.nsmallest(n=3, columns='salary'))
