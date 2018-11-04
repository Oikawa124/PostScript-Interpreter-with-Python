#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
import pytest
from stack import Stack, Etype

def test_test_stack_pop_when_stack_has_no_elements():
    with pytest.raises(IndexError):
        stack = Stack()
        stack.pop()
