import sys

def split(word):
    return [char for char in word]

file_ = sys.argv[1]

fl = open(file_, 'r')
stream = fl.read()
fl.close()

out = split(stream)
buf = "--"
for i in range(len(stream)-1):
	buf = buf[0] + stream[i]

	print(buf)

	if buf == "h1":
		print('kewel')
		out[i-1] = 'h'
		out[i] = '2'
	elif buf == "h2":
		out[i-1] = 'h'
		out[i] = '3'
	elif buf == "h3":
		out[i-1] = 'h'
		out[i] = '4'
	elif buf == "h4":
		out[i-1] = 'h'
		out[i] = '5'
	elif buf == "h5":
		out[i-1] = 'h'
		out[i] = '6'

	buf = buf[1]

fl = open(file_, 'w')
fl.write("".join(out))
fl.close()
