#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from element import *
from my_dict import *


def gets(input_): return (x for x in input_)


def eval(elems, stack=None, mydict=None):

    def add_op():
        num1 = stack.pop()
        num2 = stack.pop()
        _sum = num1.value + num2.value
        stack.push(Element(etype=Etype.NUMBER, value=_sum))

    def def_op():
        val = stack.pop()
        key = stack.pop()
        mydict.put(KeyValue(key, val))

    for elem in elems:
        if elem.etype == Etype.NUMBER:
            stack.push(elem)
        elif elem.etype == Etype.EXECUTABLE_NAME:
            if elem.value == "add":
                add_op()
            elif elem.value == "def":
                def_op()
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
    mydict = MyDict()
    eval(to_elems(gets("/a 1 def a")), stack, mydict)

    mydict.print_all()
    stack.print_all()

if __name__ == '__main__':
    main()
