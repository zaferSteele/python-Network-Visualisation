# Import modules for CGI (Common Gateway Interface) web scripting
import cgi        # For handling form data (e.g., input from URL or web form)
import cgitb      # For debugging CGI scripts (shows detailed error messages)
import ntop       # Custom module (likely internal) that provides system info and HTML helpers

# Enable CGI traceback for detailed error reporting in browser
cgitb.enable()

# Parse the form data submitted via GET or POST (e.g., from a web form)
form = cgi.FieldStorage()

# Get the value of the 'Name' parameter from the URL or form; use "Eric" as default if not provided
name = form.getvalue('Name', default="Eric")

# Retrieve system-level information using functions from the 'ntop' module
version = ntop.version()    # Get version of the system or application
os = ntop.os()              # Get the operating system name
uptime = ntop.uptime()      # Get how long the system has been running

# Start the HTML page with a custom title
ntop.printHTMLHeader('Mastering Pyton Networking', 1, 0)

# Send a greeting message including the user's name
ntop.sendString("Hello, " + name + "<br>")

# Send a string with collected system info: version, OS, and uptime
ntop.sendString("Ntop Information: %s %s %s" % (version, os, uptime))

# Close the HTML page properly
ntop.printHTMLFooter()
