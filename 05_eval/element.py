#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.
from my_parser import Ltype, parse_one, gets_set_src, gets
from stack import *

def next_token(gene):
    try:
        next(gene)
    except StopIteration:
        raise

def to_elems(gene):
    token, words = parse_one(gene)

    while token.ltype != Ltype.END_OF_FILE:
        if token.ltype == Ltype.NUMBER:
            yield Element(etype=Etype.NUMBER, value=token.value)
        elif token.ltype == Ltype.EXECUTABLE_NAME:
            yield Element(etype=Etype.EXECUTABLE_NAME, value=token.value)
        elif token.ltype == Ltype.LITERAL_NAME:
            yield Element(etype=Etype.LITERAL_NAME, value=token.value)

        token, words = parse_one(words)

def main():
    gets_set_src("abc　def g h 11")
    elems = to_elems(gets())

    for i in elems:
        print(i)

if __name__ == '__main__':
    main()
