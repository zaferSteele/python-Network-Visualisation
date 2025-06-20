#!/usr/bin/env python3

# Import the pygal library to create SVG-based charts
import pygal

# Create a Pie chart object
line_chart = pygal.Pie()

# Set the title of the chart
line_chart.title = "Protocol Breakdown"

# Add each protocol and its corresponding value to the chart
# These values could represent packet counts or traffic volume
line_chart.add('TCP', 15)
line_chart.add('UDP', 30)
line_chart.add('ICMP', 45)
line_chart.add('Others', 10)

# Render the pie chart to an SVG file for viewing in a browser or graphics app
line_chart.render_to_file('protocol_distribution_pie_chart.svg')
