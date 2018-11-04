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

def test_parse_one_empty_should_return_END_OF_FILE():
    expect = ps.Token()
    expect.Ltype = ps.Ltype.END_OF_FILE

    ps.gets_set_src("")
    ch, actualToken = ps.parse_one(ps.Ltype.EOF)

    assert expect.Ltype == actualToken.Ltype
    assert ch == ps.Ltype.EOF

test_case = [
    ["abc", "abc"],
    ["abc123", "abc123"],
    ["abc_def", "abc_def"],
    ["abc", "abc def"],
]

for i in test_case:
    def test_parser_one_executable_name():
        expect = ps.Token()
        expect.name = i[0]
        expect.Ltype = ps.Ltype.EXECUTABLE_NAME

        ps.gets_set_src(i[1])
        ch, actualToken = ps.parse_one(ps.Ltype.EOF)

        assert expect.name == actualToken.name
        assert expect.Ltype == actualToken.Ltype

def test_parse_one_literal_name():
    expect = ps.Token()
    expect.name = "/add"
    expect.Ltype = ps.Ltype.LITERAL_NAME

    ps.gets_set_src("/add")
    ch, actualToken = ps.parse_one(ps.Ltype.EOF)

    assert expect.name == actualToken.name
    assert expect.Ltype == actualToken.Ltype

def test_parse_one_open_curly():
    expect = ps.Token()
    expect.name = "{"
    expect.Ltype = ps.Ltype.OPEN_CURLY

    ps.gets_set_src("{")
    ch, actualToken = ps.parse_one(ps.Ltype.EOF)

    assert expect.Ltype == actualToken.Ltype

def test_parse_one_close_curly():
    expect = ps.Token()
    expect.name = "}"
    expect.Ltype = ps.Ltype.CLOSE_CURLY

    ps.gets_set_src("}")
    ch, actualToken = ps.parse_one(ps.Ltype.EOF)

    assert expect.Ltype == actualToken.Ltype