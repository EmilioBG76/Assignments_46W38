import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the excel file from Exercise 2” sheet of the “Module 6 – Exercises Data

data_fileex2 = 'Module 6 - Exercises Data.xlsx'

# Reading the excel file Module 6 Exercises Data into a dataframe

df = pd.read_excel(data_fileex2, sheet_name="Exercise 3", engine='openpyxl', index_col=0)

# Assigning TSRs and pitches values following the hints provided

TSR = df.index.values.astype(float)
Pitch = df.columns.values.astype(float)
Cp = df.values

# Generate grid data for 3D surface

#x = TSR
#y = Pitch

z = Cp.T
x, y = np.meshgrid(TSR,Pitch)


fig = plt.figure(figsize=(20,16))
ax = fig.add_subplot(projection='3d')

ax.set_xlabel('Tip Speed Ratio(TSR)')
ax.set_ylabel('Blade Pitch Angle [degrees]')
ax.set_zlabel('Power Coeficient Cp')
ax.set_title('3D Surface Plot of Cp vs TSR and Blade Pitch Angle')

# Set axis limits to match the specified ranges
ax.set_xlim([2, 15])
ax.set_ylim([-5, 8])
ax.set_zlim([0, 0.6])


surf = ax.plot_surface(x,y,z, cmap='inferno', edgecolor='none')

# Customize grid appearence

ax.xaxis._axinfo['grid']['color'] = 'lightgray'
ax.xaxis._axinfo['grid']['linestyle'] = '--'

ax.yaxis._axinfo['grid']['color'] = 'lightgray'
ax.yaxis._axinfo['grid']['linestyle'] = '--'

ax.zaxis._axinfo['grid']['color'] = 'lightgray'
ax.zaxis._axinfo['grid']['linestyle'] = '--'

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, pad=0.5)
plt.show()
