# Green Empower (greenempower.org) static page generator script
# Python Script: gen.py

def readfl(fl):
	handle = open(fl, 'r')
	ret = handle.read()
	handle.close()
	return ret



SCHAFOLD = \
'''
{HEADER}
<html>
	<head>
		{HEAD}
	</head>

	<body>
		{BODY}
	</body>
</html>
'''

HEADER = \
'''
<!DOCTYPE html>
'''

HEAD = readfl("fragments/head.html")
BODY = readfl("fragments/body.html")

built = SCHAFOLD.format(HEADER=HEADER, HEAD=HEAD, BODY=BODY)
