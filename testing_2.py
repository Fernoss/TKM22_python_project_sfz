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
print("Top 10 largest salaries:")
print(df.nlargest(n=10, columns='salary'))

print("\nTop 10 smallest salaries:")
print(df.nsmallest(n=10, columns='salary'))

# Salary count
print("Salary count:")
df1 = pd.crosstab(df['salary'], 'Count')
print(df1)

# Cross-referencing
# Sort 'salary' in descending order'
sorted_df = df.sort_values(by='salary', ascending=False)

# Display 'salary' and 'sat_salary' side-by-side
print("Cross-referencing salary and sat_salary:")
print(sorted_df[['salary', 'sat_salary']])


# FIGURES (everywhere figures...)
# Create a scatter plot for 'salary' vs. 'sat_salary'
plt.figure(figsize=(8, 6))
plt.scatter(df['salary'], df['sat_salary'], alpha=0.5, color='purple')
plt.xlabel('Salary')
plt.ylabel('Sat_salary')
plt.title('Scatter Plot: Salary vs. Sat_salary')
plt.show()

# Salary x Education comparison
education_labels = {
    1: 'Primary School',
    2: 'Secondary School Graduate',
    3: 'Bachelor Level',
    4: 'Master Level'
}

# Create a box plot for 'salary' vs. 'education' with correct labels
plt.figure(figsize=(12, 6))
plt.boxplot([df['salary'][df['education'] == 1],
             df['salary'][df['education'] == 2],
             df['salary'][df['education'] == 3],
             df['salary'][df['education'] == 4]],
            labels=[education_labels[1], education_labels[2], education_labels[3], education_labels[4]])
plt.ylabel('Salary')
plt.xlabel('Education Level')
plt.title('Salary Distribution by Education Level')
plt.show()

# Create a histogram for 'salary'
plt.figure(figsize=(8, 6))
plt.hist(df['salary'], bins=10, edgecolor='k', alpha=0.65, color='blue')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.show()

# Create a histogram for 'sat_salary'
plt.figure(figsize=(8, 6))
plt.hist(df['sat_salary'], bins=10, edgecolor='k', alpha=0.65, color='green')
plt.xlabel('Sat_salary')
plt.ylabel('Frequency')
plt.title('Sat_salary Distribution')
plt.show()
