#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.

input = "123 456"
pos = 0

def gets_set_src(string):
    input = string

def gets ():
    global pos
    if len(input) == pos:
        return '\0'
    ch = input[pos]
    pos += 1
    return ch


def main():
    pass

if __name__ == '__main__':
    main()
