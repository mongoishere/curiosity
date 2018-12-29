import socket
import sys

def Main():
	q = socket.socket()
	q.connect(('127.0.0.1', 9998))
	f = open('C:\\Users\\anony\\Documents\\Python\\curiosity\\curiosity_univ\\file_transfer\\sniff.jpg', 'rb')
	l = f.read(1024)
	while (l):
		print('sending')
		q.send(l)
		l = f.read(1024)
	f.close()
	print("Finished")
	q.shutdown(socket.SHUT_WR)
