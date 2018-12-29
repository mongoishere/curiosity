import platform

def Main(conn):
	platform_input = raw_input("Select Platform Option > ")
	string_to_send = str(platform_input)
	print(string_to_send)
	conn.send((string_to_send).encode('utf-8'))
	recieved = (conn.recv(1024).decode('utf-8'))
	print(recieved)