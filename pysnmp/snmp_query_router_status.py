#!/usr/bin/env/python3

# Import SNMP command generator from pysnmp library
from pysnmp.entity.rfc3413.oneliner import cmdgen

# Create an SNMP command generator object
cmdGen = cmdgen.CommandGenerator()

# Define the OIDs (Object Identifiers) to retrieve:
#  - system_up_time_oid: The uptime of the device
#  - cisco_contact_info_oid: Cisco-specific contact information
system_up_time_oid = "1.3.6.1.2.1.1.3.0"
cisco_contact_info_oid = "1.3.6.1.4.1.9.2.1.61.0"

# Send SNMP GET request to device at 192.168.255.18 using community string 'secret'
errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData('secret'),                      # SNMP community string
    cmdgen.UdpTransportTarget(('192.168.255.18', 161)),  # Target device IP and SNMP port
    system_up_time_oid,                                  # First OID to fetch
    cisco_contact_info_oid                               # Second OID to fetch
)

# Handle SNMP response:
if errorIndication:
    # Print any network or SNMP-level error
    print(errorIndication)
else:
    if errorStatus:
        # If there's an error in the response, print details
        print('%s at %s' % (
            errorStatus.prettyPrint(),                       # Error message
            errorIndex and varBinds[int(errorIndex)-1] or '?'  # Problematic OID if known
        ))
    else:
        # If no errors, print each OID and its returned value
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), str(val)))
