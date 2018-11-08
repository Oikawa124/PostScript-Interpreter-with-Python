#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from element import *


def gets(input_): return (x for x in input_)


def eval(elems, stack):

    def add_op():
        num1 = stack.pop()
        num2 = stack.pop()
        _sum = num1.value + num2.value
        stack.push(Element(etype=Etype.NUMBER, value=_sum))

    for elem in elems:
        if elem.etype == Etype.NUMBER:
            stack.push(elem)
        elif elem.etype == Etype.EXECUTABLE_NAME:
            if elem.value == "add":
                add_op()
            else:
                stack.push(elem)
        elif elem.etype == Etype.LITERAL_NAME:
            stack.push(elem)
        else:
            print("Not come here")

def main():
    stack = Stack()
    eval(to_elems(gets("1 1 add 1 3 /a")), stack)

    stack.print_all()


if __name__ == '__main__':
    main()
