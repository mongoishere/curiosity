import ctypes

def Main(conn):
	title = input("Enter Desired Title > ")
	conn.send((title).encode('utf-8'))
	text = input("Enter Desired Text > ")
	conn.send((text).encode('utf-8'))

class Mbox:
	#Passes the parameters to the initial method
	def __init__(self, title, text, style):
		self.text = text
		self.title = title
		self.style = style

	def create_box(self):
		#Reads the variables created in the initial method and sends them to message box
		ctypes.windll.user32.MessageBoxW(0, self.title, self.text, self.style)

if __name__ == '__main__':
	Main()