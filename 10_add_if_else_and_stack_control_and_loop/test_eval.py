#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
import pytest

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

def test_eval_exec_arr_add():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 /a {2 add} def a")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_exec_arr_void():
    with pytest.raises(Exception):
        evaluator = Evaluator()
        evaluator.eval(to_elems(to_char_gen("{}")))

def test_eval_exec_arr_nested():

    expect = []
    expect_nums = [1, 2, 4, 6, 5, 3]
    for i in expect_nums:
        expect.append(Element(etype=Etype.NUMBER, value=i))

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen(
        "/ZZ {6} def /YY {4 ZZ 5} def /XX {1 2 YY 3} def XX"
    )))

    actual = []
    for i in evaluator.stack.gene():
        actual.append(i)

    for ex, ac in zip(expect, actual):
        assert ex.value == ac.value

def test_eval_exec_arr_nested_conpile():

    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("{{3} exec} exec")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_eq():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 1 eq")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_neq():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 0 neq")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_gt():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 0 gt")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_ge():
    expect1 = Element(etype=Etype.NUMBER, value=1)
    expect2 = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 1 ge 1 0 ge")))
    actual1 = evaluator.stack.pop()
    actual2 = evaluator.stack.pop()

    assert expect1.value == actual1.value
    assert expect2.value == actual2.value

def test_eval_lt():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("0 3 lt")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_le():
    expect1 = Element(etype=Etype.NUMBER, value=1)
    expect2 = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("3 3 le 0 4 le")))
    actual1 = evaluator.stack.pop()
    actual2 = evaluator.stack.pop()

    assert expect1.value == actual1.value
    assert expect2.value == actual2.value

def test_eval_pop():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 10 pop")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_exch():
    expect = Element(etype=Etype.NUMBER, value=1)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 4 exch")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_dup():
    expect = Element(etype=Etype.NUMBER, value=4)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 4 dup")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_index():
    expect = Element(etype=Etype.NUMBER, value=2)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 4 2 5 1 index")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_exec():
    expect = Element(etype=Etype.NUMBER, value=4)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("{4} exec")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_if():
    expect = Element(etype=Etype.NUMBER, value=4)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 {2 4} if")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_ifelse():
    expect = Element(etype=Etype.NUMBER, value=4)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 {2 4} {3 10} ifelse")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

def test_eval_repeat():
    expect = Element(etype=Etype.NUMBER, value=3)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen("1 2 {1 add} repeat")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value

# テスト失敗
def test_eval_while():
    expect = Element(etype=Etype.NUMBER, value=4)

    evaluator = Evaluator()
    evaluator.eval(to_elems(to_char_gen(
                                        "5 dup {dup 1 gt} {1 sub exch 1 index mul exch} while pop")))
    actual = evaluator.stack.pop()

    assert expect.value == actual.value
