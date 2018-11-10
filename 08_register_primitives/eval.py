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

class Evaluator():
    def __init__(self):
        self.stack = Stack()
        self.dict = Hashtable()

    def eval(self, elems):
        for elem in elems:
            if elem.etype == Etype.NUMBER:
                self.stack.push(elem)
            elif elem.etype == Etype.EXECUTABLE_NAME:
                if elem.value == "add":
                    add_op(self.stack)
                elif elem.value == "def":
                    def_op(self.stack, self.dict)
                elif self.dict.get(elem):
                    val = self.dict.get(elem)
                    self.stack.push(val)
                else:
                    self.stack.push(elem)
            elif elem.etype == Etype.LITERAL_NAME:
                self.stack.push(elem)
            else:
                print("Not come here")

def main():

    evaluator = Evaluator()
    elems = to_elems(gets("1 1 add /a 100 def"))
    evaluator.eval(elems)

    print(evaluator.stack)
    print(evaluator.dict)

if __name__ == '__main__':
    main()
