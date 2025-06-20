#!/usr/bin/env python3

# Import the pygal library for creating SVG-based charts
import pygal

# Initialize empty lists to store time and interface metric values
x_time = []         # Timestamps (ISO format strings)
out_octets = []     # Outgoing octets (bytes sent)
out_packets = []    # Outgoing unicast packets
in_octets = []      # Incoming octets (bytes received)
in_packets = []     # Incoming unicast packets

# Open the file where router metrics are logged (one dictionary per line)
with open('results.txt', 'r') as f:
    for line in f.readlines():
        # Convert each line from string to dictionary using eval()
        line = eval(line)

        # Append each metric to its respective list
        x_time.append(line['Time'])  # Use the time string as-is
        out_packets.append(float(line['Gig0-0_Out_uPackets']))
        out_octets.append(float(line['Gig0-0_Out_Octet']))
        in_packets.append(float(line['Gig0-0_In_uPackets']))
        in_octets.append(float(line['Gig0-0_In_Octet']))

# Create a line chart using pygal
line_chart = pygal.Line()

# Set the title of the chart
line_chart.title = "Router 1 Gig0/0"

# Set x-axis labels (timestamps)
line_chart.x_labels = x_time

# Add each data series to the chart
line_chart.add('out_octets', out_octets)
line_chart.add('out_packets', out_packets)
line_chart.add('in_octets', in_octets)
line_chart.add('in_packets', in_packets)

# Render the chart to an SVG file
line_chart.render_to_file('router1_gig0_traffic.svg')
