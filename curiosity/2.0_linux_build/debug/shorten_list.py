import platform

def Main():
	select = input("Enter Platform > ")
	platform_list = [('uname'), (platform.uname()),
	('system'), (platform.system()), ('platform'), 
	(platform.platform())]
	i = 0
	while i < len(platform_list):
		if (platform_list[i]) == select:
			print(platform_list[i + 1])
			break
		i += 2
Main()