#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
from enum import IntEnum, auto
from collections import namedtuple

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

Token = namedtuple("Token", ("ltype", "value"))



def parse_one(gene):
    # next()のラッパー
    def next_ch(gene):
        try:
            return next(gene)
        except StopIteration:
            return ""


    def chain(ch, gene):
        return (x for g in ([ch], gene) for x in g)

    ch = next_ch(gene)

    if ch.isdigit():
        num = int(ch)
        ch = next_ch(gene)
        while ch.isdigit():
            num = num * 10 + int(ch)
            ch = next_ch(gene)
        return Token(Ltype.NUMBER, num), chain(ch, gene)

    elif ch.isalpha():
        word = ch
        while ch.isalpha():
            word += ch
            ch = next_ch(ch)
            return Token(Ltype.EXECUTABLE_NAME, word), chain(ch, gene)

    elif ch == '/':
        word = ch
        while ch.isalpha():
            word += ch
            ch = next_ch(ch)
        return Token(Ltype.LITERAL_NAME, word), chain(ch, gene)

    elif ch == "{":
        return Token(Ltype.OPEN_CURLY, "{"), gene

    elif ch == "}":
        return Token(Ltype.CLOSE_CURLY, "}"), gene

    elif ch == ' ':
        return Token(Ltype.SPACE, ' '), gene

    elif ch == "":
        return Token(Ltype.END_OF_FILE, ""), gene
    else:
        return Token(Ltype.UNKNOWN, "UNKNOWN"), gene



def main():
    input = "1 1 add"
    gets_set_src(input)
    parser_print_all()


if __name__ == '__main__':
    main()
