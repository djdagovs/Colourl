#!/usr/bin/python

import sys
import random
import subprocess
import os

filename = sys.argv[1]
sample = int(sys.argv[2])

# Read in file
file_contents = open(filename).readlines();

# Calculate random lines
print 'Picking ' + str(sample) + ' random sites...'
seeks = random.sample(xrange(len(file_contents)), sample)
print 'Done.\n'

# Process random lines
for i in enumerate(seeks):
    line = file_contents[i[1]]
    ranking = line.split(',')[0]
    site = line.split(',')[1].split('\n')[0]
    print 'Processing ' + site + ' (' + str(ranking) + ')...'
    subprocess.call(['python', os.getcwd() + '/webkit2png.py', 'http://' + site, '-o', 'out.png', '-F', 'javascript', '-F', 'plugins', '-w', '5', '-x', '1280', '768'])
    subprocess.call(['python', os.getcwd() + '/statisticalize.py', 'out.png', str(ranking), site])
