import socket
import sys

def Main():
	q = socket.socket()
	q.connect(('127.0.0.1', 9998))
	f = open('C:\\Users\\anony\\Documents\\Python\\curiosity\\debug\\file_tranfer\\CrashN3t_Ultimat3.vbs', 'rb')
	l = f.read(1024)
	while (l):
		q.send(l)
		l = f.read(1024)
	q.close()