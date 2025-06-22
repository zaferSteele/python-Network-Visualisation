#!/usr/bin/env python3
# This line allows the script to be run as an executable with Python 3

# Import required modules
import sys      # For reading input from standard input (stdin)
import re       # For searching text using regular expressions

# Continuously read lines from standard input until EOF
for line in iter(sys.stdin.readline, ''):
    # If the line contains the word 'agent' (case-sensitive)
    if re.search('agent ', line):
        # Print the line without trailing newline or whitespace
        print(line.strip())
