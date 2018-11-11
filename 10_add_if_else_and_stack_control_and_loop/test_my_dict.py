#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.
from my_dict import *
from element import *

def test_dict_put_one_time():
    expect = Element(etype=Etype.EXECUTABLE_NAME, value="add")

    mydict = Hashtable()
    key = Element(etype=Etype.LITERAL_NAME, value="/plus")
    value = Element(etype=Etype.EXECUTABLE_NAME, value="add")
    mydict.insert(key, value)

    actual = mydict.get(key)

    assert expect == actual

def test_dict_put_same_key():
    expect = Element(etype=Etype.EXECUTABLE_NAME, value="add2")

    mydict = Hashtable()
    key = Element(etype=Etype.LITERAL_NAME, value="/plus")
    value = Element(etype=Etype.EXECUTABLE_NAME, value="add")
    value2 = Element(etype=Etype.EXECUTABLE_NAME, value="add2")

    mydict.insert(key, value)
    mydict.insert(key, value2)

    actual = mydict.get(key)

    assert expect == actual