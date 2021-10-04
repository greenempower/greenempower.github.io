import os

from lib import *

mkdir("external")
mkdir("gen")

os.system("git clone git@gitlab.com:greenempower/greenempower.org-rendered.git external/rendered")
