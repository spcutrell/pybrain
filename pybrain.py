#!/usr/bin/env python3

import sys

MAX = 30000

def get_input(argv):
    with open(argv[1]) as f:
        data = f.read()
    return list(data)

def get_bf_instr(bf_code):
    valid_instr = {'>','<','+','-','.',',','[',']'}
    return [c for c in bf_code if c in valid_instr]

def interpret(instr):
    res_ptr = 0
    instr_ptr = 0;
    res_arr = [0] * MAX
    brackets = list()
    while instr_ptr < len(instr):
        if instr[instr_ptr] == '>':
            res_ptr += 1
        elif instr[instr_ptr] == '<':
            res_ptr -= 1
        elif instr[instr_ptr] == '+':
            res_arr[res_ptr] = (res_arr[res_ptr] + 1) % 256
        elif instr[instr_ptr] == '-':
            res_arr[res_ptr] = (res_arr[res_ptr] - 1) % 256
        elif instr[instr_ptr] == '.':
            print(chr(res_arr[res_ptr]), end='')
        elif instr[instr_ptr] == ',':
            res_arr[res_ptr] = ord(input())
        elif instr[instr_ptr] == '[':
            brackets.append(instr_ptr)
            if not res_arr[res_ptr]:
                instr_ptr += 1
                bal = 1
                while bal:
                    if instr[instr_ptr] == '[':
                        bal +=1
                    elif instr[instr_ptr] == ']':
                        bal -= 1
        elif instr[instr_ptr] == ']':
            if res_arr[res_ptr]:
                instr_ptr = brackets.pop()
                continue;
            else:
                brackets.pop()
        instr_ptr += 1

def main():
    inpt = get_input(sys.argv)
    instr = get_bf_instr(inpt)
    interpret(instr)

if __name__ == "__main__":
    main()
