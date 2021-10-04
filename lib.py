import os

def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)
	else:
		print("mkdir(): '{path}' exists, skipping".format(path=path))

def readfl(fl):
	handle = open(fl, 'r')
	ret = handle.read()
	handle.close()
	return ret

def writefl(fl, data):
	handle = open(fl, 'w')
	handle.write(data)
	handle.close()

