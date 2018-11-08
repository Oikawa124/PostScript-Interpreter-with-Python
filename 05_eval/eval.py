#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from my_parser import parse_one, parser_print_all, Token, Ltype, gets_set_src
from stack import Stack, Element, Etype


def eval(stack: Stack):
    ch, token = parse_one('')

    def add_op():
        num1 = stack.pop()
        num2 = stack.pop()
        _sum = num1.value + num2.value
        stack.push(Element(etype=Etype.NUMBER, value=_sum))

    while True:
        if token.ltype == Ltype.NUMBER:
            stack.push(Element(etype=Etype.NUMBER, value=token.value))
        elif token.ltype.EXECUTABLE_NAME:
            if token.value == "add":
                add_op()

        ch, token = parse_one(ch)

        if token.ltype == Ltype.END_OF_FILE: break

def main():
    _input = "1 1 1 add add"
    gets_set_src(_input)
    stack = Stack()
    eval(stack)
    stack.print_all()

    #todo いままでのことを省みて実装していく。


if __name__ == '__main__':
    main()
