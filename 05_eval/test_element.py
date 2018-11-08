#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.
from element import *
import pytest

def test_elem_number():
    expect_elem = Element(Etype.NUMBER, value=123)
    actual_elem = next(to_elems(gets("123")))

    assert expect_elem.Etype == actual_elem.Etype
    assert expect_elem.value == actual_elem.value


def test_elem_executable_name():
    expect_elem = Element(Etype.EXECUTABLE_NAME, value="add")

    actual_elem = next(to_elems(gets("add")))

    assert expect_elem.Etype == actual_elem.Etype
    assert expect_elem.value == actual_elem.value


def test_elem_literal_name():
    expect_elem = Element(Etype.LITERAL_NAME, value="/add")

    actual_elem = next(to_elems(gets("/add")))

    assert expect_elem.Etype == actual_elem.Etype
    assert expect_elem.value == actual_elem.value


def test_elem_not_exist():
    with pytest.raises(StopIteration):
        next(to_elems(gets("")))
