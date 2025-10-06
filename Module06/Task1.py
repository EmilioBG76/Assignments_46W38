# Module 06 - task 1 - Pie Chart

import matplotlib as plt

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot()

# Generate pie chart with values provided
pie_labels = ['Crude Oil', 'Natural gas', 'Renew. Energy', 'Solid fuels', 'Nuclear Energy']
pie_sizes = [37.7, 20.4, 19.5, 10.6, 11.8]
pie_colors = ['red', 'blue', 'green', 'orange', 'yellow']

plt.show()
