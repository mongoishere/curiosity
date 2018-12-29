import pyautogui
import sys

def client(y):
	src1 = pyautogui.screenshot()
	y.send(bytes('Screenshot Successful', 'utf-8'))
	retrieved_name = (y.recv((1024)).decode('utf-8'))
	src1.save((retrieved_name + ".png"))

def server(conn):
	result = (conn.recv(1024).decode('utf-8'))
	print(result)
	sent_name = input("Enter Screenshot Name > ")
	conn.send((sent_name).encode('utf-8'))