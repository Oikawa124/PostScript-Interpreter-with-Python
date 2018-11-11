#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from eval import *


def test_eval_add():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 1 1 add add")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value


def test_eval_dict():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("/a 1 def")))

    key = Element(Etype.LITERAL_NAME, "a")
    actual = evaluator.dict_.get(key)

    assert expect.value == actual.value


def test_eval_dict_stack_pop():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("/a 1 def　a")))

    actual = evaluator.stack.pop()

    assert expect.value == actual.value


def test_eval_sub():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("4 1 sub")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value


def test_eval_mul():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("3 1 mul")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value


def test_eval_div():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("9 3 div")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_exec_arr_number():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("/a {3} def a")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_exec_arr_two_numbers():
    expect1 = Element(etype=Etype.NUMBER, value=3)
    expect2 = Element(etype=Etype.NUMBER, value=5)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("/a {3 5} def a")))

    actual2 = evaluator.stack.pop()
    actual1 = evaluator.stack.pop()

    assert expect1.value == actual1.value
    assert expect2.value == actual2.value


def test_eval_exec_arr_literal_name():
    expect = Element(etype=Etype.LITERAL_NAME, value="abc")

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("/a {/abc} def a")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value


def test_eval_exec_arr_executable_name():
    expect = Element(etype=Etype.EXECUTABLE_NAME, value="abc")

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("/a {abc} def a")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

