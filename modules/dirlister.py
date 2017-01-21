import os

def run(**args):
	print "[*] Executing dirlister module"
	files = os.listdir(".")

	return str(files)

