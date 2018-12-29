import socket
import sys
import os

def Main():
	pass
	s = socket.socket()
	s.bind(("localhost",9998))
	s.listen(10) # Acepta hasta 10 conexiones entrantes.

	while True:
	    sc, address = s.accept()

	    print (address)
	    i=1
	    file_size = int(os.stat("C:\\Users\\anony\\Documents\\Python\\curiosity\\curiosity_univ\\file_transfer\\sniff.jpg").st_size)
	    print(file_size)
	    f = open("fucktheNSA.jpg", "wb")
	    while file_size > 0:
	    	l = sc.recv(1024)
	    	f.write(l)
	    	file_size -= len(l)
	    f.close()
	    exit()

	    sc.close()

	s.close()