# Green Empower (greenempower.org) static page generator script
# Python Script: gen.py

import os.path, time
#from pygit2 import Repository
from pathlib import Path

from lib import *


#repo = Repository("../greenempower.org.test/.git")

#print(repo.path)

#diff = repo.diff()

#print(diff.stats.files_changed)

#for delta in diff.deltas:
#	print(delta.new_file.path)


#pairs = []

#for fl in paths:
#	pairs.append(str(fl) + ' ' + str(os.path.getmtime(fl)))


#writefl("./gen/files.txt", '\n'.join(pairs))




"""
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
"""



paths = list(Path("./src/").rglob("*.[hH][tT][mM][lL]"))
pathstrs = [str(fl) for fl in paths]

print(vars())
