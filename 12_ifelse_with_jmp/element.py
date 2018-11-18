#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.
from enum import IntEnum, auto
from collections import namedtuple

from my_parser import Ltype, parse_one


class Etype(IntEnum):
    NUMBER = auto()
    EXECUTABLE_NAME = auto()
    LITERAL_NAME = auto()
    FUNCTION = auto()
    EXECUTABLE_ARRAY = auto()
    OPEN_CURLY = auto()
    CLOSE_CURLY = auto()
    OP_EXEC = auto()
    OP_JMP = auto()
    OP_JMP_NOT_IF = auto()
    NOT_EXIST = auto()


Element = namedtuple("Element", ("etype", "value"))


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
            if token.value == "exec":
                yield Element(etype=Etype.OP_EXEC, value=token.value)
            else:
                yield Element(etype=Etype.EXECUTABLE_NAME, value=token.value)
        elif token.ltype == Ltype.LITERAL_NAME:
            yield Element(etype=Etype.LITERAL_NAME, value=token.value)
        elif token.ltype == Ltype.OPEN_CURLY:
            yield Element(etype=Etype.OPEN_CURLY, value=token.value)
        elif token.ltype == Ltype.CLOSE_CURLY:
            yield Element(etype=Etype.CLOSE_CURLY, value=token.value)
        token, words = parse_one(words)
