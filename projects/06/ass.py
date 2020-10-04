# assembler project 06 - nand2tetris
import re
import sys
import os
import time
from tables import *

#filename = sys.argv[1]

COMMENT_PREFIX = "//"
DEFAULT_PROG_ADDR = 0
DEFAULT_MEM_ADDR = 16
SPACE = ' '


symbol_table = {}
# symbol_table.update(predef_table)
labels = {}
variables_table = {}  # user defined

# global next_program_addr = 0
next_memory_addr = DEFAULT_MEM_ADDR

lines = []
tmp = []


def read_file(asm_file):
    for line in open(asm_file, 'r'):
        line = line.strip()  # strip whitespace
        line = line.split(COMMENT_PREFIX)[0].strip()  # strip comment
        lines.append(line)

# first iteration


def generate_symbol_table(line):
    next_program_addr = 0
    for line in lines:
        if not line.startswith(SPACE):
            if line.startswith('('):
                label = line[1:].split(')')[0]
                labels[label] = next_program_addr
                continue
            next_program_addr += 1


# second iteration
def assemble(lines):
    next_program_addr = 0
    next_memory_addr = 16
    for line in lines:
        if not line.startswith(SPACE):
            if line.startswith('('):
                label = line[1:].split(')')[0]
                symbol_table[label] = next_memory_addr
                next_memory_addr += 1

            # A-COMMAND
            if line.startswith('@'):
                symbol = line[1:].split('@')[0]
                if symbol.isdigit():
                    continue
                else:
                    if symbol not in predef_table:
                        predef_table[symbol] = next_memory_addr
                        next_memory_addr += 1
                    symbol = predef_table[symbol]
                    fw.write("0{0:015b}\n".format(symbol))
                next_program_addr += 1
                continue

            # C-COMMAND
            comp = dest = jump = ""
            if '=' in line:
                symbol = line.split('=')
                dest = dest_table[symbol[0]]
                line = symbol[1]
            else:
                dest = dest_table['null']
            symbol = line.split(';')
            comp = comp_table[symbol[0]]
            if ';' in line:
                jump = jump_table[symbol[1].strip()]
            else:
                jump = jump_table['null']
            fw.write('111'+comp+dest+jump+'\n')
            next_program_addr += 1

    fw.close()


def generate_code():
    pass


if __name__ == '__main__':
    fw = open(sys.argv[0].split('.')[0]+".hack", 'w')

    file = read_file(sys.argv[1])
    print(lines)
    assemble(lines)
    generate_symbol_table(lines)
    print(labels)
    print(symbol_table)

    # assembler.assemble() # run code
    # print(Assembler.lines)
    # print(assembler.assemble())
    # print(Assembler.tmp)
    # print(Assembler.symbol_table)


'''
def prep_file(filename):
    file = open(filename)
    a = file.readlines()
    a = map(filter_line, a) #map remove comments    
    a = [i.strip() for i in [ x for x in a ] ] #remove white space
    a = filter(lambda x : x != '', a) #remove empty elements    
    return a


def filter_line(a, op="//"):
  idx = a.find(op)
  if idx == -1:
    return a
  elif idx == 0:
    return ''
  else:
    if op == "//":
      a = a[:(idx-1)]
    else:
      a = a[:idx]
  return a  


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

#filter_line(filename, op=".")
'''
