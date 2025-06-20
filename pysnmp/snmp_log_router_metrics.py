#!/usr/bin/python3

# Import SNMP command generator and datetime module
from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime

# Create an SNMP command generator object
cmdGen = cmdgen.CommandGenerator()

# Define the target device and SNMP community string
host = '192.168.255.18'
community = 'secret'

# Define SNMP OIDs (Object Identifiers) for the desired metrics
# Each OID represents a specific piece of data from the router
system_name = '1.3.6.1.2.1.1.5.0'              # System hostname
gig0_0_in_oct = '1.3.6.1.2.1.2.2.1.10.1'       # Bytes received on Gig0/0
gig0_0_in_uPackets = '1.3.6.1.2.1.2.2.1.11.1'  # Packets received on Gig0/0
gig0_0_out_oct = '1.3.6.1.2.1.2.2.1.16.1'      # Bytes sent on Gig0/0
gig0_0_out_uPackets = '1.3.6.1.2.1.2.2.1.17.1' # Packets sent on Gig0/0

# Define a function to query a single OID from a host via SNMP
def snmp_query(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),              # Community string for SNMP auth
        cmdgen.UdpTransportTarget((host, 161)),       # IP and SNMP port
        oid                                            # The OID to request
    )
    
    # Check for and handle errors in the response
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
            ))
        else:
            # Return the value from the SNMP response
            for name, val in varBinds:
                return str(val)

# Create a dictionary to store the collected metrics
result = {}
result['Time'] = datetime.datetime.utcnow().isoformat()               # Timestamp in UTC
result['hostname'] = snmp_query(host, community, system_name)        # Hostname
result['Gig0-0_In_Octet'] = snmp_query(host, community, gig0_0_in_oct)
result['Gig0-0_In_uPackets'] = snmp_query(host, community, gig0_0_in_uPackets)
result['Gig0-0_Out_Octet'] = snmp_query(host, community, gig0_0_out_oct)
result['Gig0-0_Out_uPackets'] = snmp_query(host, community, gig0_0_out_uPackets)

# Append the result as a line in the results.txt file
with open('results.txt', 'a') as f:
    f.write(str(result))  # Convert dictionary to string and write
    f.write('\n')         # New line for next entry
