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

