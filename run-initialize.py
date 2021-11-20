import os

from lib import *

mkdir("external")
mkdir("gen")
mkdir("log")

os.system("git clone git@github.com:greenempower/rendered.git external/rendered")
