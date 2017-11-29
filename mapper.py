#!/usr/bin/env python

import sys
import os


for line in sys.stdin:
    line = line.strip()
    datas = line.split()
    url = datas[3]
    # url = url[1:-1]
    if ".jpg" in datas[3] or ".JPG" in datas[3]:
        filename = os.environ['mapreduce_map_input_file']
        splitfilename = filename.split('/')
        filename = splitfilename[-1]
        splitfilename = filename.split('.')
        user = splitfilename[0]
        print '%s\t%s' % (user, 1)
    print '%s\t%s' % (datas[3], 1)
