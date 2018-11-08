#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from eval import *

def test_eval_add():
    expect = Element(etype=Etype.NUMBER, value=3)

    stack = Stack()
    eval(to_elems(gets("1 1 1 add add")), stack)
    actual = stack.pop()

    assert expect.value == actual.value

def test_eval_dict():
    expect = Element(etype=Etype.NUMBER, value=1)

    stack = Stack()
    mydict = MyDict()
    eval(to_elems(gets("/a 1 def")), stack, mydict)

    key = Element(Etype.LITERAL_NAME, "a")
    actual = mydict.get(key)

    assert expect.value == actual.value