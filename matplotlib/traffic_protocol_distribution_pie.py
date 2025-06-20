#!/usr/bin/env python3

# Example from http://matplotlib.org/2.0.0/examples/pie_and_polar_charts/pie_demo_features.html

import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Define labels for each section of the pie chart
labels = 'TCP', 'UDP', 'ICMP', 'Others'

# Define corresponding values (sizes) for each label
sizes = [15, 30, 45, 10]  # These could represent traffic distribution or packet counts

# Define which slice to "explode" or offset from the center (highlighted)
explode = (0, 0.1, 0, 0)  # Only the UDP slice will be offset for emphasis

# Create a pie chart
fig1, ax1 = plt.subplots()  # Create figure and axis objects
ax1.pie(
    sizes,
    explode=explode,         # Highlight selected slice(s)
    labels=labels,           # Add labels to slices
    autopct='%1.1f%%',       # Display percentage value on slices
    shadow=True,             # Add shadow for 3D effect
    startangle=90            # Rotate chart to start from the top
)

# Set axis to be equal so the pie is a circle (not oval)
ax1.axis('equal')

# Save the pie chart to a PNG file
plt.savefig('traffic_pie_chart.png')

# Show the chart on the screen
plt.show()
