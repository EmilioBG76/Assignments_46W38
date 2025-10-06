import pandas as pd
import matplotlib.pyplot as plt

# Loading the excel file from Exercise 2” sheet of the “Module 6 – Exercises Data

data_fileex2 = 'Module 6 - Exercises Data.xlsx'

# Reading the excel file Module 6 Exercises Data into a dataframe

df = pd.read_excel(data_fileex2, sheet_name="Exercise 2", engine='openpyxl')

# Displaying the first few rows

#print(data_frame)

# Defining variables
x = df["Wind speed (m/s)"]
y1 = df["Power (kW)"]
y2 = df["Thrust (kN)"]
y3 = df["Rotor speed (rpm)"]
y4 = df["Blade pitch (degrees)"]

# Plotting figure with provided values within excel file
fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=(8,10))

ax1.plot(x,y1, color='red', label='Power')
ax1.set_title("Power vs Wind speed")
ax1.set_xlabel("Wind Speed [m/s]")
ax1.set_ylabel("Power [kW]")
ax1.legend()

ax2.plot(x,y2, color='blue', label='Thrust')
ax2.set_title("Thurst vs Wind speed")
ax2.set_xlabel("Wind Speed [m/s]")
ax2.set_ylabel("Thurst [kN]")
ax2.legend()

ax3.plot(x,y3, color='orange', label='Rotor speed')
ax3.set_title("Rotor speed vs Wind speed")
ax3.set_xlabel("Wind Speed [m/s]")
ax3.set_ylabel("Rotor speed [rpm]")
ax3.legend()

ax4.plot(x,y4, color='brown', label='Blade pitch')
ax4.set_title("Blade pitch vs Wind speed")
ax4.set_xlabel("Wind Speed [m/s]")
ax4.set_ylabel("Blade pitch [degrees]")
ax4.legend()
                

fig.tight_layout()
plt.show()
