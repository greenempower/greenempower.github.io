# Green Empower (greenempower.org) static page generator script
# Python Script: gen.py

import os.path, time
#from pygit2 import Repository
from pathlib import Path
from shutil import copyfile

from lib import *

from macros import *


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

COPY_NO_PROCESS = readfl("copy-no-process")
copy_no_process = COPY_NO_PROCESS.split('\n')

paths = list(Path("./src/").rglob('*'))
paths = [fl for fl in paths if fl.is_file()]
html_paths = list(Path("./src/").rglob("*.[hH][tT][mM][lL]"))
pathstrs = [str(fl) for fl in paths]

for path in paths:
	print(path)
	cutoff = "./src/"
	rel_path = os.path.relpath(path, cutoff)
	if rel_path in copy_no_process:
		print(" - copying without processing")
		continue

	new_path = "./external/rendered/public/" + rel_path


	if(rel_path.lower().endswith(".html")):
		raw = readfl(path)
		rendered_page = raw.format(**vars())
		writefl(new_path, rendered_page)
		print(" - rendered")
	else:
		copyfile(path, new_path)
		print(" - copied")

#print(vars())
