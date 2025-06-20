#!/usr/bin/env python3

# Import necessary libraries
import matplotlib.pyplot as plt               # For plotting graphs
import matplotlib.dates as dates             # For working with date/time on x-axis

# Initialize empty lists to store time and packet data
x_time = []      # This will hold the converted timestamp values
y_value = []     # This will hold the corresponding unicast packet values

# Open the file 'results.txt' which contains data in dictionary format (one per line)
with open('results.txt', 'r') as f:
    for line in f.readlines():
        # Convert each line from string to dictionary
        line = eval(line)

        # Convert the 'Time' string to matplotlib's internal float format
        x_time.append(dates.datestr2num(line['Time']))

        # Extract the value for 'Gig0-0_Out_uPackets' and append to y_value
        y_value.append(line['Gig0-0_Out_uPackets'])

# Adjust layout so x-axis labels don't overlap with each other
plt.subplots_adjust(bottom=0.3)

# Rotate the x-axis labels by 80 degrees for better readability
plt.xticks(rotation=80)

# Plot the data using date values on x-axis
plt.plot_date(x_time, y_value)

# Add title and axis labels to the graph
plt.title('Router1 G0/0')
plt.xlabel('Time in UTC')
plt.ylabel('Output Unicast Packets')

# Save the plot as a PNG image file
plt.savefig('router1_gig0_output_packets.png')

# Display the plot on the screen
plt.show()
