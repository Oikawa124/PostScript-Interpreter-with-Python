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
    def __init__(self, Ltype=None, value=None):
        self._Ltype = Ltype
        self._value = value

    def get_Ltype(self):
        return self._Ltype

    def set_Ltype(self, Ltype):
        self._Ltype = Ltype

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    Ltype = property(get_Ltype, set_Ltype)
    value = property(get_value, set_value)




def parse_one(prev_ch):
    ch = gets() if prev_ch == Ltype.EOF else prev_ch

    if ch.isdigit():
        num = 0
        while ch.isdigit():
            num = num*10 + int(ch)
            ch = gets()
        return ch, Token(Ltype.NUMBER, num)

    elif ch.isalpha():
        word = ""
        while ch.isalpha() or ch.isalnum():
            word += ch
            ch = gets()
        return ch, Token(Ltype.NUMBER, word)

    elif ch == '/':
        word = ch
        ch = gets()
        while ch.isalpha() or ch.isdigit():
            word += ch
            ch = gets()
        return ch, Token(Ltype.NUMBER, word)

    elif ch.isspace():
        while ch.isspace(): ch = gets()
        return ch, Token(Ltype.SPACE)

    elif ch == "{":
        ch = gets()
        return ch, Token(Ltype.OPEN_CURLY)

    elif ch == "}":
        ch = gets()
        return ch, Token(Ltype.CLOSE_CURLY)

    elif ch == '\0':
        return ch, Token(Ltype.END_OF_FILE)

    else:
        return ch, Token(Ltype.UNKNOWN)


def parser_print_all():
    ch = Ltype.EOF
    while True:
        ch, token = parse_one(ch)

        if token.Ltype == Ltype.END_OF_FILE:
            break

        if token.Ltype == Ltype.NUMBER:
            print(f"num: {token.value}")
        elif token.Ltype == Ltype.SPACE:
            print("space")
        elif token.Ltype == Ltype.OPEN_CURLY:
            print("open curly brace")
        elif token.Ltype == Ltype.CLOSE_CURLY:
            print("close curly brace")
        elif token.Ltype == Ltype.EXECUTABLE_NAME:
            print(f"executable name: {token.value}")
        elif token.Ltype == Ltype.LITERAL_NAME:
            print(f"literal name {token.value}")
        else:
            print(f"Unknown type : {token.Ltype}")



def main():
    input = "123 23 11"
    gets_set_src(input)
    parser_print_all()


if __name__ == '__main__':
    main()
