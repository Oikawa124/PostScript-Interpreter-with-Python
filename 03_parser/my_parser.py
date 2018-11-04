#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
from enum import IntEnum, auto

from gets import gets, gets_set_src


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

    if ch.isdigit():
        num = 0
        while ch.isdigit():
            num = num*10 + int(ch)
            ch = gets()

        token.Ltype = Ltype.NUMBER
        token.number = num
        return ch, token

    elif ch.isalpha():
        word = ""
        while ch.isalpha() or ch.isalnum():
            word += ch
            ch = gets()

        token.Ltype = Ltype.EXECUTABLE_NAME
        token.name = word
        return ch, token

    elif ch == '/':
        word = ch
        ch = gets()
        while ch.isalpha() or ch.isdigit():
            word += ch
            ch = gets()

        token.Ltype = Ltype.LITERAL_NAME
        token.name = word
        return ch, token

    elif ch.isspace():
        while ch.isspace(): ch = gets()

        token.Ltype = Ltype.SPACE
        return ch, token

    elif ch == "{":
        ch = gets()

        token.Ltype = Ltype.OPEN_CURLY
        return ch, token

    elif ch == "}":
        ch = gets()

        token.Ltype = Ltype.CLOSE_CURLY
        return ch, token

    elif ch == '\0':
        token.Ltype = Ltype.END_OF_FILE
        return ch, token

    else:
        token.Ltype = Ltype.UNKNOWN
        return Ltype.END_OF_FILE


def parser_print_all():
    ch = Ltype.EOF
    while True:
        ch, token = parse_one(ch)

        if token.Ltype == Ltype.END_OF_FILE:
            break

        if token.Ltype == Ltype.NUMBER:
            print(f"num: {token.number}")
        elif token.Ltype == Ltype.SPACE:
            print("space")
        elif token.Ltype == Ltype.OPEN_CURLY:
            print("open curly brace")
        elif token.Ltype == Ltype.CLOSE_CURLY:
            print("close curly brace")
        elif token.Ltype == Ltype.EXECUTABLE_NAME:
            print(f"executable name: {token.name}")
        elif token.Ltype == Ltype.LITERAL_NAME:
            print(f"literal name {token.name}")
        else:
            print(f"Unknown type : {token.Ltype}")



def main():
    input = "123 23 11"
    gets_set_src(input)
    parser_print_all()


if __name__ == '__main__':
    main()
