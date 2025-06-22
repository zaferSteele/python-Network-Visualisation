# Import required modules
import ntop         # Custom/internal module for HTML output and system info
import interface    # Another internal module, likely for getting network interface details
import json         # For converting Python data to JSON-formatted strings

# Initialize a list to hold interface names
ifnames = []

# Try to retrieve the names of all available interfaces
try:
    # Loop through number of interfaces, get their names, and add to list
    for i in range(interface.numInterfaces()):
        ifnames.append(interface.name(i))

# Catch and print any exception that occurs while retrieving interface names
except Exception as inst:
    print(type(inst))     # Print the type of exception
    print(inst.args)      # Print the arguments associated with the exception
    print(inst)           # Print a human-readable representation of the exception

# Begin HTML output using ntop module
ntop.printHTMLHeader('Mastering Python Networking', 1, 0)

# Display a header message
ntop.sendString("Here are my interfaces: <br>")

# Convert the interface names list to a pretty-printed JSON string and send it
ntop.sendString(json.dumps(ifnames, sort_keys=True, indent=4))

# Close the HTML output
ntop.printHTMLFooter()
