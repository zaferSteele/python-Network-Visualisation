#!/usr/bin/env/python3

# Import SNMP command generator from the pysnmp library
from pysnmp.entity.rfc3413.oneliner import cmdgen

# Create an SNMP command generator instance
cmdGen = cmdgen.CommandGenerator()

# Define the OIDs (Object Identifiers) for system information
# system_name: retrieves the name assigned to the device
# system_uptime: retrieves how long the device has been running
system_name = '1.3.6.1.2.1.1.5.0'
system_uptime = '1.3.6.1.2.1.1.3.0'

# Send SNMP GET request to the target device
errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData('secret'),                      # Community string for SNMP authentication
    cmdgen.UdpTransportTarget(('192.168.255.18', 161)),  # Target device IP and SNMP port
    system_name,                                         # OID for system name
    system_uptime                                        # OID for system uptime
)

# Handle the SNMP response
if errorIndication:
    # If there's a communication or configuration error, print it
    print(errorIndication)
else:
    if errorStatus:
        # If SNMP responds with an error, print the message and problematic OID (if known)
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
        ))
    else:
        # If no errors, print each OID name and its corresponding value
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), str(val)))
