#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    line = line.lower()
    # split the line into words; splits on any whitespace
    stopwords = set(['the','and'])
    
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        print '%s\t%s' % (word, "1")
