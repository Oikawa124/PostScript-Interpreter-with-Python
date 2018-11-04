#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
from enum import IntEnum, auto

class LexicalType(IntEnum):
    NUMBER = auto()
    SPACE = auto()
    EXECUTABLE_NAME = auto()
    LITERAL_NAME = auto()
    OPEN_CURLY = auto()
    CLOSE_CURLY = auto()
    END_OF_FILE = auto()
    UNKNOWN = auto()

def main():
    pass

if __name__ == '__main__':
    main()
