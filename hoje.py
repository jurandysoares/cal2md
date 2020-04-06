#!/usr/bin/env python3
'''
Open the file of today for annotations
'''

from datetime import datetime
from pathlib import Path, PurePath

home = Path.home()
now = datetime.now()
date = now.strftime("%Y %m %d").split()
fname = "README.md"

path = PurePath(home, *date, fname)
print(path)