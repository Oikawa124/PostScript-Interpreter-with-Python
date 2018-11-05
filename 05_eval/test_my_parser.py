#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
from my_parser import Token, Ltype, parse_one, gets_set_src

def test_parse_one_number():
    expect = Token(ltype=Ltype.NUMBER, value=123)

    gets_set_src("123")
    ch, actualToken = parse_one('')

    assert expect.value == actualToken.value
    assert expect.ltype == actualToken.ltype

def test_parse_one_empty_should_return_END_OF_FILE():
    expect = Token(ltype=Ltype.END_OF_FILE)

    gets_set_src('')
    ch, actualToken = parse_one('')

    assert expect.ltype == actualToken.ltype
    assert ch == ''

test_case = [
    ["abc", "abc"],
    ["abc123", "abc123"],
    ["abc_def", "abc_def"],
    ["abc", "abc def"],
]

for i in test_case:
    def test_parser_one_executable_name():
        expect = Token(ltype=Ltype.EXECUTABLE_NAME, value=i[0])

        gets_set_src(i[1])
        ch, actualToken = parse_one('')

        assert expect.value == actualToken.value
        assert expect.ltype == actualToken.ltype

def test_parse_one_literal_name():
    expect = Token(ltype=Ltype.LITERAL_NAME, value="/add")

    gets_set_src("/add")
    ch, actualToken = parse_one('')

    assert expect.value== actualToken.value
    assert expect.ltype == actualToken.ltype

def test_parse_one_open_curly():
    expect = Token(ltype=Ltype.OPEN_CURLY, value="{")

    gets_set_src("{")
    ch, actualToken =parse_one('')

    assert expect.ltype == actualToken.ltype

def test_parse_one_close_curly():
    expect = Token(ltype=Ltype.CLOSE_CURLY, value="}")

    gets_set_src("}")
    ch, actualToken = parse_one('')

    assert expect.ltype == actualToken.ltype