# assembler
import re
import sys
import os
import time
from tables import *

'''
# reading and parsing commands

1) start reading a file with a given name
- constructor for a parser object that accepts a string specifying a file name

2) move to next command
- boolean hasMoreCommands(); == TRUE (are we finished?)
- get next command:' void advance();
- read one line at a time
- skip whitespace including comments
- get fields of current command (A-Command', C-Command', Label)', easy access to the fields. dest() comp() jump() label()
- translate every field into binary code (dest() into 010101 whatever)


# C-command',
# syntax:' dest=comp;jump
# binary:' 111 ac1c2c3c4c5c6 d1d2d3 j1j2j3
# if C-command than three 111 bits at the beginning

'''

COMMENT_PREFIX = "//"

lines = [] # add every asm line to the list

def read_file(asm_file):
    for line in open(asm_file, 'r'): # read file
        line = line.strip()  # strip whitespace
        line = line.split(COMMENT_PREFIX)[0].strip()  # strip comment
        lines.append(line)




if __name__ == '__main__':
	hack_file = open(sys.argv[0].split('.')[0]+".hack", 'w')
	file = read_file(sys.argv[1])