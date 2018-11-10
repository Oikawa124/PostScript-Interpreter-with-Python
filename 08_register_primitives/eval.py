#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from element import *
from my_dict import *


def to_char_gen(input_): return (x for x in input_)


class Evaluator:
    def __init__(self):
        self.stack = Stack()
        self.dict = Hashtable()
        register_primitives(self.stack, self.dict)

    def eval(self, elems):
        for elem in elems:
            if elem.etype == Etype.NUMBER:
                self.stack.push(elem)
            elif elem.etype == Etype.EXECUTABLE_NAME:
                is_exist, dict_value = self.dict.get(elem)
                if is_exist:
                    if dict_value.etype == Etype.FUNCTION:
                        dict_value.value()
                else:
                    self.stack.push(elem)
            elif elem.etype == Etype.LITERAL_NAME:
                self.stack.push(elem)
            else:
                print("Not come here")


def register_primitives(stack, mydict):
    def add():
        num1 = stack.pop()
        num2 = stack.pop()
        _sum = num1.value + num2.value
        stack.push(Element(etype=Etype.NUMBER, value=_sum))

    def def_():
        val = stack.pop()
        key = stack.pop()
        mydict.insert(key, val)

    def sub():
       val1 = stack.pop()
       val2 = stack.pop()
       stack.push(val1-val2)

    list_ = [add, def_, sub]
    for i in list_:
        mydict.insert(
            Element(etype=Etype.EXECUTABLE_NAME, value=f"{i.__name__}"),
            Element(etype=Etype.FUNCTION, value=i)
        )


def main():
    evaluator = Evaluator()
    elems = to_elems(to_char_gen("1 1 add "))
    evaluator.eval(elems)

    print(evaluator.stack)
    print(evaluator.dict)


if __name__ == '__main__':
    main()
