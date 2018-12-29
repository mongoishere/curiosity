import ctypes

def Main():
	title = input("Enter Desired Title > ")
	text = input("Enter Desired Text > ")
	style = 1
	box = Mbox(title, text, style)
	Mbox.create_box(box)

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