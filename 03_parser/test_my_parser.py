#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
import my_parser as ps

def test_parse_one_number():
    expect = ps.Token()
    expect.number = 123
    expect.Ltype = ps.Ltype.NUMBER

    ps.gets_set_src("123")
    ch, actualToken = ps.parse_one(ps.Ltype.EOF)

    assert expect.number == actualToken.number
    assert expect.Ltype == actualToken.Ltype
