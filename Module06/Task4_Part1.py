import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the excel file from Exercise 2” sheet of the “Module 6 – Exercises Data

data_fileex2 = 'Module 6 - Exercises Data.xlsx'

# Reading the excel file Module 6 Exercises Data into a dataframe

df = pd.read_excel(data_fileex2, sheet_name="Exercise 4 - Baseline", engine='openpyxl')
df_A = pd.read_excel(data_fileex2, sheet_name="Exercise 4 - A", engine='openpyxl')
df_B = pd.read_excel(data_fileex2, sheet_name="Exercise 4 - B", engine='openpyxl')

x1 = df["Time (s)"]
y1 = df["Rotor speed (rpm)"]

x2 = df_A["Time (s)"]
y2 = df_A["Rotor speed (rpm)"]

x3 = df_B["Time (s)"]
y3 = df_B["Rotor speed (rpm)"]


plt.figure(figsize=(12,6))

plt.plot(x1, y1, color='red', label='Turbine #1 (Baseline)')
plt.plot(x2, y2, color='blue', label='Turbine #2 (A)')
plt.plot(x3, y3, color='green', label='Turbine #3 (B)')

plt.xlabel('Time [seconds]')
plt.ylabel('Rotor speed [rpm]')
plt.title('Rotor speed vs time turbines comparison')

plt.legend()
plt.grid(True)
plt.show()