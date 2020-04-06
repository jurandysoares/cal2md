#!/usr/bin/env python3
'''
Open the file of today for annotations
'''

import argparse
from datetime import datetime, timedelta
from pathlib import Path, PurePath
import sys

# Python tutorial: Python Command Line Arguments by 
# @realpython https://realpython.com/python-command-line-arguments/

parser = argparse.ArgumentParser(description='Retorna caminho do arquivo das atividades do dia de hoje')
parser.add_argument('rel_days', nargs='*')
args = parser.parse_args()

if not args.rel_days:
    days_from_today = [0]
else:
    days_from_today = map(int, args.rel_days)

fplist = [] # File paths list
for rel_day in days_from_today:
    home = Path.home()
    now = datetime.now()
    date = now + timedelta(days=rel_day)
    year,month,day = date.strftime("%Y %m %d").split()
    fname = "README.md"
    path = PurePath(home, year, month, day, fname)
    fplist.append(path)

print(' '.join([str(p) for p in fplist]))
