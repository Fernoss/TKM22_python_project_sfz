import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# data = {
#     "gender": ["Male", "Female", "Male", "Female", "Female", "Female", "Female", "Male", "Female", "Female",
#                "Female", "Female", "Female", "Male", "Female", "Female", "Female", "Female", "Male", "Male", "Female", "Male", "Female"],
#     # Extend with 0
#     "age": [76, 55, 67, 18, 73, 59, 75, 54, 59, 69, 23, 77, 67, 69, 56, 49, 21, 31, 58, 36, 54] + [0] * 2,
#     "marital_status": ["Separated", "Divorced", "Married", "Single", "Married", "Divorced", "Divorced", "Married", "Divorced",
#                        "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Married", "Married", "Single",
#                        "Married", "Married"] + [""] * 3,  # Extend with empty strings
#     "education": ["Doctoral degree", "Bachelor’s degree", "Less than high school", "Master’s degree",
#                   "Some college, no degree", "Some college, no degree", "Some college, no degree", "Master’s degree",
#                   "Bachelor’s degree", "Doctoral degree", "High school diploma or equivalent",
#                   "High school diploma or equivalent", "Bachelor’s degree", "Associate degree",
#                   "High school diploma or equivalent", "High school diploma or equivalent", "High school diploma or equivalent",
#                   "Bachelor’s degree", "Master’s degree", "High school diploma or equivalent", "Master’s degree"] + [""] * 2,  # Extend with empty strings
#     # Extend with 0
#     "years_of_service": [88, 114, 138, 158, 85, 158, 230, 38, 61, 49, 38, 65, 2, 101, 35, 215, 77, 12, 211, 6, 54] + [0] * 2,
#     "salary": [24453, -1686, 5174, -31339, -22505, -22434, -25075, -28169, 8985, -16103, -13753, 15392, -24696,
#                19917, -23498, 21886, -29634, 30908, 21770, 32351, -6725] + [0] * 2  # Extend with 0
# }

# Trying to generate random data for testing
# Generate random data for "gender" column
gender_options = ["Male", "Female"]
gender = [random.choice(gender_options) for _ in range(23)]

# Generate random data for "marital_status" column
marital_status_options = ["Separated", "Divorced", "Married", "Single"]
marital_status = [random.choice(marital_status_options) for _ in range(23)]

# Generate random data for "education" column
education_options = ["Doctoral degree", "Bachelor’s degree",
                     "Less than high school", "Master’s degree", "High school diploma or equivalent"]
education = [random.choice(education_options) for _ in range(23)]

# Generate random data for "years_of_service" column
years_of_service = [random.randint(0, 35) for _ in range(23)]

# Generate random data for "age" column
age = [random.randint(18, 65) for _ in range(23)]

# Generate random data for "salary" column
salary = [random.randint(2000, 10000) for _ in range(23)]

# Your data dictionary
data = {
    "gender": gender,
    "age": age,
    "marital_status": marital_status,
    "education": education,
    "years_of_service": years_of_service,
    "salary": salary
}

# Create the DataFrame
df = pd.DataFrame(data)

# Check the lengths of each data list (should be 23)
data_lengths = {key: len(value) for key, value in data.items()}
print(data_lengths)

# Summary statistics
summary_stats = df.describe()

# # Visualize age distribution
# plt.figure(figsize=(10, 6))
# plt.hist(df['age'], bins=10, edgecolor='k', alpha=0.65)
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.title('Age Distribution')
# plt.show()

# # Visualize salary distribution
# plt.figure(figsize=(10, 6))
# plt.hist(df['salary'], bins=10, edgecolor='k', alpha=0.65)
# plt.xlabel('Salary')
# plt.ylabel('Frequency')
# plt.title('Salary Distribution')
# plt.show()

# Adding both age and salary distributions in the same figure using subplots
plt.figure(figsize=(12, 6))

# Age distribution subplot
plt.subplot(1, 2, 1)
plt.hist(df['age'], bins=10, edgecolor='k', alpha=0.65)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Salary distribution subplot
plt.subplot(1, 2, 2)
plt.hist(df['salary'], bins=10, edgecolor='k', alpha=0.65)
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')

plt.tight_layout()  # Ensure proper spacing between subplots
plt.show()

# Group data by education and calculate average salary
education_salary = df.groupby('education')['salary'].mean().reset_index()
