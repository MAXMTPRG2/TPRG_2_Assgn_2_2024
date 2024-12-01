# Max Molnar 100746162
# TPRG 2131 CRN 02 -Assignment 2
# Nov 28, 2024

# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

#Server_vcgencmds_MM.py
import socket
import os, time
import json

s = socket.socket()
host = '10.102.13.135' # Localhost
port = 5000
s.bind((host, port))
s.listen(5)


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
v = os.popen('vcgencmd measure_volts ain1').readline() #gets from the os, using vcgencmd - the core-voltage, ref https://www.nicm.dev/vcgencmd/
t = os.popen('vcgencmd measure_temp').readline() #gets from the os, using vcgencmd - the core temperature, ref https://www.nicm.dev/vcgencmd/
c = os.popen('vcgencmd measure_clock core').readline() #gets from the os, using vcgencmd - the core clock frequency, ref https://www.nicm.dev/vcgencmd/
vp = os.popen('vcgencmd measure_volts sdram_p').readline() #gets from the os, using vcgencmd - the SDRAM voltage, ref https://www.nicm.dev/vcgencmd/
mem = os.popen('vcgencmd get_mem gpu').readline() #gets from the os, using vcgencmd - the GPU Memory, ref https://www.nicm.dev/vcgencmd/

# initialising json object string
ini_string = {"Core Voltage": v,"Core Temperature": t, "Core Clock Freq": c, "SDRAM Voltage": vp, "GPU Memory": mem}
# Convert to JSON format using dumps
f_dict = json.dumps(ini_string)

while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  res = bytes(str(f_dict), 'utf-8') # needs to be a byte
  c.send(res) # sends data as a byte type
  c.close()