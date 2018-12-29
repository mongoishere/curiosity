import platform

def Main(conn):
	platform_input = input("Select Platform Option > ")
	conn.send((platform_input).encode('utf-8'))
	recieved = (conn.recv(1024).decode('utf-8'))
	print(recieved)