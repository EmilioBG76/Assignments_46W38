# Importing necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Loading excel file from Exercise 4” sheet of the “Module 6 – Exercises Data

data_fileex4 = 'Module 6 - Exercises Data.xlsx'

# Reading the excel file Module 6 Exercises Data into a dataframe

df = pd.read_excel(data_fileex4, sheet_name="Exercise 4 - Baseline", engine='openpyxl')
df_A = pd.read_excel(data_fileex4, sheet_name="Exercise 4 - A", engine='openpyxl')
df_B = pd.read_excel(data_fileex4, sheet_name="Exercise 4 - B", engine='openpyxl')

# Selecting the relevant output metrics for standard deviation calculation
output_metrics = ['Blade pitch (degrees)', 'Rotor speed (rpm)', 'Platform pitch\
 (degrees)', 'Thrust (kN)', 'Tower base moment (kNm)']

# Calculating the standard deviations for every single wind turbine and their data
std_devs = {}

std_devs['Baseline'] = df[output_metrics].std()
std_devs['Turbine A'] = df_A[output_metrics].std()
std_devs['Turbine B'] = df_B[output_metrics].std()

# Creating a DataFrame with the dictionary for absolute standard deviations of WTs
std_devs_df = pd.DataFrame(std_devs).T

# Printing absolute standard deviations for each WT
print("The absolute standard deviations calculated for each wind turbine are:")
print(f'{std_devs_df}')

# Calculating normalized standard deviations for each WT data provided
norm_std_devs = {}
baseline_std_devs = std_devs_df.loc['Baseline']

norm_std_devs['Turbine A'] = std_devs_df.loc['Turbine A'] / baseline_std_devs
norm_std_devs['Turbine B'] = std_devs_df.loc['Turbine B'] / baseline_std_devs

# Creating a new DataFrame to hold normalized WTs standard deviations calculated
norm_std_devs_df = pd.DataFrame(norm_std_devs).T

# Printing the normalized standard deviations
print("The normalized standard deviations calculated for each wind turbine are:")
print(f'{norm_std_devs_df}')

# Plotting absolute and normalized standard deviations in separate subplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

# Plotting absolute standard deviations
std_devs_df.plot(kind='bar', ax=axes[0])
axes[0].set_title('Absolute Standard Deviations of Output Metrics for Three Turbines')
axes[0].set_xlabel('Turbine')
axes[0].set_ylabel('Standard Deviation')
axes[0].tick_params(axis='x', rotation=0)
axes[0].legend(title='Metric')

# Plotting normalized standard deviations for all WTs compared to WT Baseline

norm_std_devs_df.plot(kind='bar', ax=axes[1])
axes[1].set_title('Normalized Standard Deviations of Output Metrics for the 3 WTs')
axes[1].set_xlabel('Turbine')
axes[1].set_ylabel('Normalized Standard Deviation')
axes[1].tick_params(axis='x', rotation=0)
axes[1].legend(title='Metric')

plt.tight_layout()
plt.show()
