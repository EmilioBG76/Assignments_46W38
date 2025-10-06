# Module 06 - task 1 - Pie Chart

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot()

# Generate pie chart with values provided
pie_labels = ['Crude Oil', 'Natural gas', 'Renew. Energy', 'Solid fuels', 'Nuclear Energy']
pie_sizes = [37.7, 20.4, 19.5, 10.6, 11.8]
pie_colors = ['red', 'blue', 'green', 'orange', 'yellow']

plt.pi(pie_sizes, labels=pie_labels, colors=pie_colors, autopct='%1.1f%%', startangle=90)
plt.title('Energy generation sources within the EU in 2023')

plt.show()
