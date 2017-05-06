#!/usr/bin/env python

import sys
import csv

# input comes from STDIN (standard input)
flag = True
for row in csv.reader(iter(sys.stdin.readline, '')):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if(flag):
                flag = False
                continue
        if(row[24]):
                print '%s\t%s' % (row[24], 1)
        if(row[25]):
                print '%s\t%s' % (row[25], 1)
        if(row[26]):
                print '%s\t%s' % (row[26], 1)
        if(row[27]):
                print '%s\t%s' % (row[27], 1)
        if(row[28]):
                print '%s\t%s' % (row[28], 1)
