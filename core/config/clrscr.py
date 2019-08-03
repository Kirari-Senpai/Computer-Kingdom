
import os
import sys


def clrscr():

	if (sys.platform=="linux") or (sys.platform=="linux2"): os.system('clear');
	elif (sys.platform=="windows") or (sys.platform=="win32") or (sys.platform=="win64"): os.system('cls');
	else: os.system('clear'); 