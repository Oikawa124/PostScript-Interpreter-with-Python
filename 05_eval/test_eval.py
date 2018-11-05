#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from my_parser import gets_set_src
from stack import Stack, Etype, Element
from eval import eval


def test_eval_add():
    expect = Element(etype=Etype.NUMBER, value=3)

    _input = "1 1 1 add add"
    gets_set_src(_input)
    stack = Stack()
    eval(stack)
    actual = stack.pop()

    assert expect.value == actual.value