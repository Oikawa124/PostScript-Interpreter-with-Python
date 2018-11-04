#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
from enum import IntEnum, auto

from gets import gets


class Ltype(IntEnum):
    EOF = -1
    NUMBER = auto()
    SPACE = auto()
    EXECUTABLE_NAME = auto()
    LITERAL_NAME = auto()
    OPEN_CURLY = auto()
    CLOSE_CURLY = auto()
    END_OF_FILE = auto()
    UNKNOWN = auto()


class Token:
    def __init__(self):
        self.Ltype = None
        self.number = 0
        self.name = ""


def parse_one(prev_ch):
    token = Token()
    ch = gets() if prev_ch == Ltype.EOF else prev_ch

    if ch.isalnum():
        num = 0
        while ch.isalnum():
            num = num*10 + int(ch)
            ch = gets()
        token.Ltype = Ltype.NUMBER
        token.number = num
        return ch, token
    elif ch.isspace():
        while ch.isspace(): ch = gets()

        token.Ltype = Ltype.SPACE
        token.name = " "
        return ch, token



def main():
    ch1, token1 = parse_one(Ltype.EOF)
    ch2, token2 = parse_one(ch1)
    ch3, token3 = parse_one(ch2)

    assert (token1.number == 123)
    assert (token2.name == " ")
    assert (token3.number == 456)

if __name__ == '__main__':
    main()
