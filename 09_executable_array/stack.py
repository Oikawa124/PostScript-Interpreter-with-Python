#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from enum import IntEnum, auto
from collections import namedtuple

class Etype(IntEnum):
    NUMBER = auto()
    EXECUTABLE_NAME = auto()
    LITERAL_NAME = auto()
    FUNCTION = auto()
    EXECUTABLE_ARRAY = auto()
    OPEN_CURLY = auto()
    CLOSE_CURLY = auto()
    NOT_EXIST = auto()


Element = namedtuple("Element", ("etype", "value"))


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise

    def __str__(self):
        if self.stack is None:
            return "Stack()"
        s = "stack(\n"
        for i, v in enumerate(self.stack):
            s += f"{i}:{v}\n"
        return s + ")"

