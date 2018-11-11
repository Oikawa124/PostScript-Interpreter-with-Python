#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
from eval import *

def test_eval_add():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 1 1 add add")))
    actual = evaluator.stack_ex_arr.pop()

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

    actual = evaluator.stack_ex_arr.pop()

    assert expect.value == actual.value

def test_eval_sub():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("4 1 sub")))
    actual = evaluator.stack_ex_arr.pop()

    assert expect.value == actual.value

def test_eval_mul():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("3 1 mul")))
    actual = evaluator.stack_ex_arr.pop()

    assert expect.value == actual.value

def test_eval_div():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("9 3 div")))
    actual = evaluator.stack_ex_arr.pop()

    assert expect.value == actual.value