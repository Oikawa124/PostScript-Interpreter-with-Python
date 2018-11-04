#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
from enum import IntEnum, auto

from gets import gets, gets_set_src


class Status(IntEnum):
    ACTIVE = 1
    INACTIVE = 0
    CANCELED = -1


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
    pass


if __name__ == '__main__':
    main()
