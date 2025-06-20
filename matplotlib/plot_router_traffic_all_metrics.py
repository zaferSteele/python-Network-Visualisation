#!/usr/bin/env python3

# Import required libraries for plotting
import matplotlib.pyplot as plt               # For creating plots
import matplotlib.dates as dates             # For handling and formatting datetime values on x-axis

# Initialize empty lists to store time and interface metric values
x_time = []          # Time values (converted to matplotlib's float format)
out_octets = []      # Outgoing octets (bytes sent)
out_packets = []     # Outgoing unicast packets
in_octets = []       # Incoming octets (bytes received)
in_packets = []      # Incoming unicast packets

# Open the file containing the router metrics (each line is a dictionary)
with open('results.txt', 'r') as f:
    for line in f.readlines():
        # Convert each line from string to dictionary using eval
        line = eval(line)

        # Convert 'Time' string to matplotlib's date float format
        x_time.append(dates.datestr2num(line['Time']))

        # Extract and store each metric from the dictionary
        out_packets.append(line['Gig0-0_Out_uPackets'])
        out_octets.append(line['Gig0-0_Out_Octet'])
        in_packets.append(line['Gig0-0_In_uPackets'])
        in_octets.append(line['Gig0-0_In_Octet'])

# Adjust layout to make space for x-axis labels
plt.subplots_adjust(bottom=0.3)

# Rotate x-axis labels for better readability
plt.xticks(rotation=80)

# Plot each metric as a time series
plt.plot_date(x_time, out_packets, '-', label='Out Packets')   # Outgoing packets
plt.plot_date(x_time, out_octets, '-', label='Out Octets')     # Outgoing bytes
plt.plot_date(x_time, in_packets, '-', label='In Packets')     # Incoming packets
plt.plot_date(x_time, in_octets, '-', label='In Octets')       # Incoming bytes

# Add plot title and labels
plt.title('Router1 G0/0')
plt.legend(loc='upper left')         # Display legend in the top-left corner
plt.grid(True)                       # Enable grid lines for better readability
plt.xlabel('Time in UTC')           # X-axis label
plt.ylabel('Values')                # Y-axis label

# Save the plot as a PNG image file
plt.savefig('all_router_traffic_metrics.png')

# Display the plot window
plt.show()
