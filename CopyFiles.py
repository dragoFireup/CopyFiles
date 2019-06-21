'''
	Automatically copies any files or folders inside a Folder named Test from a new USB

'''
from ctypes import windll
import os
import time
import string
from glob import glob

def copyDir(dirname, path):
	global copydirname
	files = glob(dirname+'\\*')
	for file in files:
		if os.path.isdir(file):
			dirname = file.split('\\')[-1]
			newdir = path+'\\'+dirname
			os.mkdir(newdir)
			copyDir(file, newdir)
		else:
			os.system('copy '+file+' '+path)

def getdrives():

	drives = []
	bitmask = windll.kernel32.GetLogicalDrives()
	for i in string.ascii_uppercase:
		if bitmask&1:
			drives.append(i)
		bitmask>>=1
	return drives

if __name__ == "__main__":
	global copydirname
	print('Please make sure that all the contents that you want to copy are in the test folder in the USB drive')
	while 1:
		before = set(getdrives())
		time.sleep(1)
		after = set(getdrives())
		drives = after - before

		delta = len(drives)

		if delta:
			for drive in drives:
				files = glob(drive+":\\test\\*")
				if len(files) == 0:
					print('No folder named Test in '+drive+' drive')
					continue
				copydirname = input('Enter the absolute path of the destination for '+drive+':\\test contents: ')
				for file in files:
					if os.path.isdir(file):
						dirname = file.split('\\')[-1]
						newdir = copydirname+'\\'+dirname
						os.mkdir(newdir)
						copyDir(file, newdir)
					else:
						os.system('copy '+file+' '+copydirname)
				