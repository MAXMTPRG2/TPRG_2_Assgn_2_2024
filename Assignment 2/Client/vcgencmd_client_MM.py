# Max Molnar 100746162
# TPRG 2131 CRN 02 -Assignment 2
# Nov 28, 2024

# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

#vcgencmd_json_client_MM.py

import socket
import json
s = socket.socket()
host = '10.102.13.135' #IP of raspberry Pi
port = 5000
s.connect((host, port))

# Receive from the server data in JSON Format
jsonReceived = s.recv(1024)
print(jsonReceived.decode(), "\n") # Decode and print the information/data
data = json.loads(jsonReceived)
ret = json.dumps(data, indent=4)

# Split up data from dictionary by vcgencmd command
ret1 = data["Core Voltage"]
ret2 = data["Core Temperature"]
ret3 = data["Core Clock Freq"]
ret4 = data["SDRAM Voltage"]
ret5 = data["GPU Memory"]

# Print all vcgencmd commands
print(ret1)
print(ret2)
print(ret3)
print(ret4)
print(ret5)

s.close()