#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.
from my_parser import Ltype, parse_one, gets_set_src, gets
from stack import *


def to_elems(gene):
    token, words = parse_one(gene)

    while token.ltype != Ltype.END_OF_FILE:
        if token.ltype == Ltype.NUMBER:
            yield Element(Etype=Etype.NUMBER, value=token.value)
        elif token.ltype == Ltype.EXECUTABLE_NAME:
            yield Element(Etype=Etype.EXECUTABLE_NAME, value=token.value)
        elif token.ltype == Ltype.LITERAL_NAME:
            yield Element(Etype=Etype.LITERAL_NAME, value=token.value)

        token, words = parse_one(words)

def main():
    gets_set_src("abc")
    elem = next(to_elems(gets()))
    print(elem)

if __name__ == '__main__':
    main()
