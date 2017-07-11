#!/usr/bin/env python3

import sys

def get_input(argv):
    if len(argv) > 1:
        if argv[1] == '-':
            f = sys.stdin
        else:
            f = open(argv[1])
    else:
        f = sys.stdin
    with f:
        data = f.read()

    return list(data)

def get_bf_instr(bf_code):
    valid_instr = {
        '>'
        ,'<',
        '+',
        '-',
        '.',
        ',',
        '[',
        ']'
    }
    return [c for c in bf_code if c in valid_instr]

def interpret(instr):
    res_ptr = 0
    instr_ptr = 0;
    res_arr = [0]*len(instr)
    
    while instr_ptr < len(instr):
        if instr[instr_ptr] == '>':
            res_ptr +=1
            instr_ptr += 1
        elif instr[instr_ptr] == '<':
            res_ptr -=1
            instr_ptr += 1
        elif instr[instr_ptr] == '+':
            res_arr[res_ptr] = (res_arr[res_ptr] + 1) % 255
            instr_ptr += 1
        elif instr[instr_ptr] == '-':
            res_arr[res_ptr] = (res_arr[res_ptr] - 1) % 255
            instr_ptr += 1
        elif instr[instr_ptr] == '.':
            print(chr(res_arr[res_ptr]), end='')
            instr_ptr += 1
        elif instr[instr_ptr] == ',':
            res_arr[res_ptr] = ord(input())
            instr_ptr += 1
        elif instr[instr_ptr] == '[':
            pass
        elif instr[instr_ptr] == ']':
            pass

if __name__ == "__main__":
    inpt = get_input(sys.argv)
    instr = get_bf_instr(inpt)
    interpret(instr)
