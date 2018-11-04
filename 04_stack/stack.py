#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from enum import IntEnum, auto
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Etype(IntEnum):
    NUMBER = auto()
    EXECUTABLE_NAME = auto()
    LITERAL_NAME = auto()
    NOT_EXIST = auto()

class ELEMENT:
    def __init__(self):
        self.Etype = None
        self.number = 0
        self.name = ""

class Stack:
    def __init__(self, stack = None):
        if type(stack) is type([]):
            self.stack = stack
        elif stack is None:
            self.stack = []
        else:
            print("There is Not list type")

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        try:
            pop_elem = self.stack.pop()
            return pop_elem
        except IndexError as ex:
            logger.error(ex)
            raise

    def print_all(self):
        for i, v in enumerate(self.stack):
            if v.Etype == Etype.NUMBER:
                print(f"{i} || Type: {v.Etype}, value: {v.number}")
            elif v.Etype == Etype.LITERAL_NAME:
                print(f"{i} || Type: {v.Etype}, value: {v.name}")
            elif v.Etype == Etype.EXECUTABLE_NAME:
                print(f"{i} || Type: {v.Etype}, value: {v.name}")
            else:
                print("{i} || UNKNOWN")