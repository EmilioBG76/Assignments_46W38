# Importing necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Loading excel file from Exercise 4” sheet of the “Module 6 – Exercises Data

data_fileex4 = 'Module 6 - Exercises Data.xlsx'

# Reading the excel file Module 6 Exercises Data into a dataframe

df = pd.read_excel(data_fileex4, sheet_name="Exercise 4 - Baseline", engine='openpyxl')
df_A = pd.read_excel(data_fileex4, sheet_name="Exercise 4 - A", engine='openpyxl')
df_B = pd.read_excel(data_fileex4, sheet_name="Exercise 4 - B", engine='openpyxl')

# Calculating the standar deviations for every single wind turbine and their data
std_dev_Baseline = df.std()
std_dev_A = df_A.std()
std_dev_B = df_B.std()

# Printing the standar deviation results for all wind turbine datas

#print("Standard deviations:")
#print(f'For turbine "Baseline" the standard deviation are {std_dev_Baseline}')
#print(f'For turbine "A" the standard deviation are {std_dev_A}')
#print(f'For turbine "B" the standard deviation are {std_dev_B}')

# Creating a dictionary to hold the standard deviations calculated for each WT

std_dev_WTdata = {'Baseline': std_dev_Baseline,
                'Turbine A': std_dev_A,
                'Turbine B': std_dev_B}

# Creating a DataFrame with the dictionary

std_dev_df = pd.DataFrame(std_dev_WTdata)

# Printing the results in DataFrame format
#print("The standard deviations calculated for each wind turbine are:")
#print(std_dev_df)

# Calculating normalized standard deviations for each WT data provided

norm_std_dev_A = std_dev_A / std_dev_Baseline
#print(f'The normalized st. deviation values for Turbine A are: {norm_std_dev_A}')

norm_std_dev_B = std_dev_B / std_dev_Baseline
#print(f'The normalized st. deviation values for Turbine B are: {norm_std_dev_B}')

# Creating a new dictionary to hold normalized WTs standard deviations calculated 

norm_std_dev_WTdata = {'Baseline': std_dev_Baseline,
                    'Turbine A': norm_std_dev_A,
                    'Turbine B': norm_std_dev_B}

# Creating another DataFrame with this new dictionary from here above
norm_std_dev_df = pd.DataFrame(norm_std_dev_WTdata)

# Printing the results in DataFrame format
print("The normalized standard deviations calculated for each wind turbine are:")
print(norm_std_dev_df)