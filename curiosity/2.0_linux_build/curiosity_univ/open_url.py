import webbrowser

def server(conn):
	input_url = input("Enter Web Address > ")
	conn.send((input_url).encode('utf-8'))

def client(y):
	open_url = ((y.recv(1024)).decode('utf-8'))
	webbrowser.open(open_url)