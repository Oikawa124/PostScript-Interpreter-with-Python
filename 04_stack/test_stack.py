#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
import pytest
from stack import Stack, Etype, Element

def test_stack_pop_when_stack_has_no_elements():
    with pytest.raises(IndexError):
        stack = Stack()
        stack.pop()

def test_stack_push_and_pop():
    expect = Element(etype=Etype.NUMBER, value=3)

    stack = Stack()
    elem = Element(etype=Etype.NUMBER, value=3)
    stack.push(elem)

    actual = stack.pop()

    assert actual.etype == expect.etype

#todo テストを実装していく