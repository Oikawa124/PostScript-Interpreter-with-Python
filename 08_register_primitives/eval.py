#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from element import *
from my_dict import *


def to_char_gen(input_): return (x for x in input_)


class Evaluator:
    def __init__(self):
        self.stack = Stack()
        self.dict_ = Hashtable()
        register_primitives(self.stack, self.dict_)

    def eval(self, elems):
        for elem in elems:
            if elem.etype == Etype.NUMBER:
                self.stack.push(elem)
            elif elem.etype == Etype.EXECUTABLE_NAME:
                is_exist, dict_value = self.dict_.get(elem)
                if is_exist:
                    if dict_value.etype == Etype.FUNCTION:
                        dict_value.value()
                    else:
                        self.stack.push(dict_value)
                else:
                    self.stack.push(elem)
            elif elem.etype == Etype.LITERAL_NAME:
                self.stack.push(elem)
            else:
                print("Not come here")


def register_primitives(stack, mydict):
    def _pre_process():
        num1 = stack.pop()
        num2 = stack.pop()
        return num1, num2

    def add_op():
        num1, num2 = _pre_process()
        ans = num1.value + num2.value
        stack.push(Element(etype=Etype.NUMBER, value=ans))

    def def_op():
        val = stack.pop()
        key = stack.pop()
        mydict.insert(key, val)

    def sub_op():
        num1, num2 = _pre_process()
        ans = num2.value - num1.value
        stack.push(Element(etype=Etype.NUMBER, value=ans))

    def mul_op():
        num1, num2 = _pre_process()
        ans = num1.value * num2.value
        stack.push(Element(etype=Etype.NUMBER, value=ans))

    def div_op():
        num1, num2 = _pre_process()
        ans = num2.value / num1.value
        stack.push(Element(etype=Etype.NUMBER, value=ans))

    list_ = [add_op, def_op, sub_op, mul_op, div_op]
    for i in list_:
        mydict.insert(
            Element(etype=Etype.EXECUTABLE_NAME, value=f"{i.__name__[:-3]}"),
            Element(etype=Etype.FUNCTION, value=i)
        )


def main():
    evaluator = Evaluator()
    elems = to_elems(to_char_gen("1 1 add"))
    evaluator.eval(elems)

    print(evaluator.stack)
    print(evaluator.dict_)


if __name__ == '__main__':
    main()
