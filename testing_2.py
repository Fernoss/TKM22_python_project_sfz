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

# Slicing to select specific rows
sliced_salaries = df['salary'][5:15]
print("\nSliced Salaries:")
print(sliced_salaries)

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


# FIGURES (figures everwhere...)
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

# Ambitious piechart for salary.
# Define salary ranges
salary_ranges = {
    'Low Salary': (1500, 2250),
    'Moderate Salary': (2251, 3200),
    'High Salary': (3201, 10000)
}

# Create a function to categorize salaries


def categorize_salary(salary):
    for category, (min_salary, max_salary) in salary_ranges.items():
        if min_salary <= salary <= max_salary:
            return category
    return 'Unknown'


# Apply the categorization to create a new column 'Salary Category'
df['Salary Category'] = df['salary'].apply(categorize_salary)

# Count the distribution of employees in each salary range
salary_distribution = df['Salary Category'].value_counts()

# Create a pie chart to visualize the distribution
plt.figure(figsize=(8, 6))
plt.pie(salary_distribution, labels=None, autopct='%1.1f%%', startangle=140)

# Add annotations for salary ranges
# Create a white circle at the center
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

# Define the positions for annotations
positions = [(-0.15, -0.45), (1, 0.45), (-1.12, 0.75)]

for i, (category, (min_salary, max_salary)) in enumerate(salary_ranges.items()):
    plt.annotate(f'{category}\n({min_salary}-{max_salary})',
                 xy=positions[i],
                 fontsize=10,
                 ha='left', va='center')

plt.title('Salary Range Distribution')
plt.axis('equal')  # For a circle

# Show the pie chart
plt.show()


# KEYWORD ARGUMENTS (EXERCISE 2):
# "Keyword arguments are a feature in Python that allows you to pass arguments to
# a function using the parameter names as keywords. This provides clarity and flexibility
# when calling functions, especially when functions have multiple parameters. It allows
# you to specify values for specific parameters by name, rather than relying on their
#  positional order."

# Function with keyword arguments
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")


# Using keyword arguments in function call
# greet(name="Alice", message="Hi")
# greet(message="Hey", name="Bob")
