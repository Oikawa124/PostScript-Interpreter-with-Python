#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from enum import IntEnum, auto
from collections import namedtuple

class Etype(IntEnum):
    NUMBER = auto()
    EXECUTABLE_NAME = auto()
    LITERAL_NAME = auto()
    NOT_EXIST = auto()


Element = namedtuple("Element", ("Etype", "value"))


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

    def print_all(self):
        for i, v in enumerate(self.stack):
            if v.etype == Etype.NUMBER:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            elif v.etype == Etype.LITERAL_NAME:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            elif v.etype == Etype.EXECUTABLE_NAME:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            else:
                print("{i} || UNKNOWN")