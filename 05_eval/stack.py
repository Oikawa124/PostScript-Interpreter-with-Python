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

class Element:
    def __init__(self, etype=None, value=None):
        self._etype = etype
        self._value = value

    def get_etype(self):
        return self._etype

    def set_etype(self, etype):
        self._etype = etype

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    etype = property(get_etype, set_etype)
    value = property(get_value, set_value)


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
            if v.etype == Etype.NUMBER:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            elif v.etype == Etype.LITERAL_NAME:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            elif v.etype == Etype.EXECUTABLE_NAME:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            else:
                print("{i} || UNKNOWN")