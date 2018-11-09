#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.
from my_dict import *

def test_dict_put_one_time():
    expect = "add"
    mydict = MyDict()
    mydict.put(KeyValue(1, "add"))

    actual = mydict.get(1)

    assert expect == actual

def test_dict_put_same_key():
    expect = "plus"
    mydict = MyDict()
    mydict.put(KeyValue(1, "add"))
    mydict.put(KeyValue(1, "plus"))

    actual = mydict.get(1)

    assert expect == actual