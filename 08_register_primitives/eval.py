#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from element import *
from my_dict import *


def gets(input_): return (x for x in input_)


def add_op(stack):
    num1 = stack.pop()
    num2 = stack.pop()
    _sum = num1.value + num2.value
    stack.push(Element(etype=Etype.NUMBER, value=_sum))


def def_op(stack, mydict):
    val = stack.pop()
    key = stack.pop()
    mydict.insert(key, val)


def eval(elems, stack=None, mydict=None):



    for elem in elems:
        if elem.etype == Etype.NUMBER:
            stack.push(elem)
        elif elem.etype == Etype.EXECUTABLE_NAME:
            if elem.value == "add":
                add_op(stack)
            elif elem.value == "def":
                def_op(stack, mydict)
            elif mydict.get(elem):
                val = mydict.get(elem)
                stack.push(val)
            else:
                stack.push(elem)
        elif elem.etype == Etype.LITERAL_NAME:
            stack.push(elem)
        else:
            print("Not come here")

def main():
    stack = Stack()
    mydict = Hashtable()
    eval(to_elems(gets("1 1 add")), stack, mydict)

    print(stack)
    print(mydict)

if __name__ == '__main__':
    main()
