import platform

def Main(y):
	sent = False
	platform_list = [('all'), (platform.uname()),
	('system'), (platform.system()), 
	('platform'), (platform.platform()),
	('release'), (platform.release()),
	('processor'), (platform.processor()),
	('node'), (platform.node()),
	('machine'), (platform.machine())]

	recieved = (y.recv(1024).decode('utf-8'))
	print(str(recieved))
	i = 0
	while i < len(platform_list):
		if (platform_list[i]) == recieved:
			y.send(bytes(platform_list[i + 1]))
			sent = True
		i += 2
	if (sent == False):
		y.send(bytes('No Attribute Found', 'utf-8'))
