# Green Empower (greenempower.org) static page generator script
# Python Script: gen.py

import os
import os.path, time
#from pygit2 import Repository
from pathlib import Path
from shutil import copyfile

import minify_html

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

def render(raw, varz=vars()):
	ret = raw.format(**varz)
	#ret = minify_html.minify(ret, minify_js=False)
	return ret
	

dirs = [x[0] for x in os.walk("./src")]
for path in dirs:
	cutoff = "./src/"
	rel_path = os.path.relpath(path, cutoff)
	new_path = "./external/rendered/" + rel_path

	mkdirs(new_path)

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

	new_path = "./external/rendered/" + rel_path


	if(rel_path.lower().endswith(".html")):
		raw = readfl(path)
		rendered_page = render(raw)
		writefl(new_path, rendered_page)
		print(" - rendered")
	else:
		copyfile(path, new_path)
		print(" - copied")

#print(vars())
