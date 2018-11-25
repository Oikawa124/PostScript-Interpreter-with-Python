#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
import pytest

from stack import Stack
from element import Etype, Element

def test_stack_pop_when_stack_has_no_elements():
    with pytest.raises(IndexError):
        stack = Stack()
        stack.pop()


def test_stack_push_and_pop_one_time():
    expect = Element(etype=Etype.NUMBER, value=3)

    stack = Stack()
    elem = Element(etype=Etype.NUMBER, value=3)
    stack.push(elem)

    actual = stack.pop()

    assert actual.etype == expect.etype
    assert actual.value == expect.value


def test_stack_push_and_pop_two_time():
    expect = Element(etype=Etype.EXECUTABLE_NAME, value="add")

    stack = Stack()
    elem = Element(etype=Etype.NUMBER, value=3)
    elem2 = Element(etype=Etype.EXECUTABLE_NAME, value="add")
    stack.push(elem)
    stack.push(elem2)

    actual = stack.pop()

    assert actual.etype == expect.etype
    assert actual.value == expect.value
