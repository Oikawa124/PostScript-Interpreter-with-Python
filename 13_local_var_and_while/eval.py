#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.
import operator as op
from functools import partial
from collections import deque

from element import to_elems, Element, Etype
from my_dict import Hashtable
from stack import Stack
from continuation import *


def to_char_gen(input_): return (x for x in input_)


class Evaluator:
    def __init__(self):
        self.stack = Stack()
        self.dict_ = Hashtable()
        self.dict_of_compile = {}
        self.co_stack = CoStack()
        register_compile_primitives(self.dict_of_compile)
        register_primitives(self.stack, self.dict_, self)

    def eval(self, elems):
        for elem in elems:
            if elem.etype in {Etype.NUMBER, Etype.LITERAL_NAME, Etype.EXECUTABLE_ARRAY}:
                self.stack.push(elem)
            elif elem.etype == Etype.EXECUTABLE_NAME:
                if elem.value == "if":
                    proc = self.stack.pop()
                    bool_ = self.stack.pop()

                    if bool_.value:
                        self.eval_exec_array(proc.value)
                elif elem.value == "ifelse":
                    proc2 = self.stack.pop()
                    proc1 = self.stack.pop()
                    bool_ = self.stack.pop()

                    if bool_.value:
                        self.eval_exec_array(proc1.value)
                    else:
                        self.eval_exec_array(proc2.value)
                elif elem.value == "exec":
                    self.eval_exec_array(self.stack.pop().value)
                elif elem.value == "while":
                    body = self.stack.pop()
                    cond = self.stack.pop()

                    self.eval_exec_array(cond.value)

                    val = self.stack.pop()

                    while val.value:
                        self.eval_exec_array(body.value)
                        self.eval_exec_array(cond.value)
                        val = self.stack.pop()
                elif elem.value == "repeat":
                    proc = self.stack.pop()
                    n = self.stack.pop()
                    cnt = n.value
                    for _ in range(cnt):
                        self.eval_exec_array(proc.value)

                else:
                    is_exist, dict_value = self.dict_.get(elem)
                    if is_exist:
                        if dict_value.etype == Etype.FUNCTION:
                            dict_value.value()
                        elif dict_value.etype == Etype.EXECUTABLE_ARRAY:
                            self.eval_exec_array(dict_value.value)
                        else:
                            self.stack.push(dict_value)
                    else:
                        self.stack.push(elem)
            elif elem.etype == Etype.OPEN_CURLY:
                ex_arr = self.compile_exec_array(elems)
                if ex_arr:
                    self.stack.push(
                        Element(
                            etype=Etype.EXECUTABLE_ARRAY,
                            value=ex_arr
                        )
                    )
                else:
                    raise Exception("NO ELEMENT IN EXECUTABLE_ARRAY")
            else:
                raise Exception("NOT COME HERE")

    def compile_exec_array(self, elems):
        ex_arr = []
        for elem in elems:
            if elem.etype in {Etype.NUMBER, Etype.LITERAL_NAME}:
                ex_arr.append(elem)
            elif elem.etype == Etype.EXECUTABLE_NAME:
                try:
                    func = self.dict_of_compile[elem]
                    if func.etype == Etype.FUNCTION:
                        ex_arr += func.value()
                except:
                    ex_arr.append(elem)
            elif elem.etype == Etype.OPEN_CURLY:
                rec_ex_arr = self.compile_exec_array(elems)
                if rec_ex_arr:
                    ex_arr.append(Element(
                            etype=Etype.EXECUTABLE_ARRAY,
                            value=rec_ex_arr)
                    )
                else:
                    raise Exception("NO ELEMENT IN EXECUTABLE_ARRAY")
            elif elem.etype == Etype.CLOSE_CURLY:
                break
            else:
                raise Exception("NOT COME HERE")
        return ex_arr



    def eval_exec_array(self, ex_arr):
        self.co_stack.push(exec_array=ex_arr, pc=0)

        while not self.co_stack.is_empty():
            is_cont, cont_or_val = self.co_stack.pop()
            try:
                while not is_cont:
                    is_cont, cont_or_val = self.co_stack.pop()
                exec_array, pc = cont_or_val
            except IndexError:
                break

            while pc < len(exec_array):
                if exec_array[pc].etype in {Etype.NUMBER, Etype.LITERAL_NAME, Etype.EXECUTABLE_ARRAY}:
                    self.stack.push(exec_array[pc])
                elif exec_array[pc].etype == Etype.EXECUTABLE_NAME:
                    is_exist, dict_value = self.dict_.get(exec_array[pc])
                    if is_exist:
                        if dict_value.etype == Etype.FUNCTION:
                            dict_value.value()
                        elif dict_value.etype == Etype.EXECUTABLE_ARRAY:
                            self.co_stack.push(exec_array=exec_array, pc=pc+1)
                            self.co_stack.push(exec_array=dict_value.value, pc=0)
                            break
                        else:
                            self.stack.push(dict_value)
                    else:
                        self.stack.push(exec_array[pc])
                elif exec_array[pc].etype == Etype.OP_EXEC:
                    self.co_stack.push(exec_array=exec_array, pc=pc+1)
                    self.co_stack.push(exec_array=self.stack.pop().value, pc=0)
                    break
                elif exec_array[pc].etype == Etype.OP_JMP:
                    num = self.stack.pop().value
                    pc = pc + num - 1
                    if pc >= len(exec_array):
                        break
                elif exec_array[pc].etype == Etype.OP_JMP_NOT_IF:
                    num = self.stack.pop().value
                    cond = self.stack.pop().value
                    if cond == 0:
                        pc = pc + num - 1
                    if pc >= len(exec_array):
                        break
                elif exec_array[pc].etype == Etype.OP_STORE:
                    self.co_stack.store(self.stack.pop())

                elif exec_array[pc].etype == Etype.OP_LOAD:
                    num = self.stack.pop().value
                    self.stack.push(self.co_stack.load(num))
                elif exec_array[pc].etype == Etype.OP_LPOP:
                    self.co_stack.pop()
                else:
                    raise Exception("NOT COME HERE")
                pc += 1


def register_primitives(stack, mydict, evaluator):
    def _pop_two_elems():
        num1 = stack.pop()
        num2 = stack.pop()
        return num1, num2

    def _binary_op(binop):
        elem1, elem2 = _pop_two_elems()

        ans = binop(elem2.value, elem1.value)

        ans = ans if type(ans) != bool else int(ans)

        stack.push(Element(etype=Etype.NUMBER, value=ans))

    add_ = partial(_binary_op, op.add)
    sub_ = partial(_binary_op, op.sub)
    mul_ = partial(_binary_op, op.mul)
    div_ = partial(_binary_op, op.floordiv)
    eq_  = partial(_binary_op, op.eq)
    neq_ = partial(_binary_op, op.ne)
    gt_  = partial(_binary_op, op.gt)
    ge_  = partial(_binary_op, op.ge)
    lt_  = partial(_binary_op, op.lt)
    le_  = partial(_binary_op, op.le)

    def def_op():
        val, key = _pop_two_elems()
        mydict.insert(key, val)

    def pop_op(): stack.pop()

    def exch_op():
        val1, val2 = _pop_two_elems()
        stack.push(val1)
        stack.push(val2)

    def dup_op():
        val = stack.pop()
        stack.push(val)
        stack.push(val)

    def index_op():
        val = stack.pop()
        index = val.value
        stack.push(stack.seek(index))

    def roll_op():
        j = stack.pop().value
        n = stack.pop().value

        queue = deque([stack.pop()for _ in range(n)])

        for _ in range(j):
            tmp = queue.popleft()
            queue.append(tmp)

        for elem in reversed(queue):
            stack.push(elem)

    func_list = [def_op, roll_op, pop_op, exch_op, dup_op, index_op]
    for func in func_list:
        mydict.insert(
            key=Element(etype=Etype.EXECUTABLE_NAME, value=f"{func.__name__[:-3]}"),
            value=Element(etype=Etype.FUNCTION, value=func)
        )

    func_list_partial = [v for v in locals().keys() if v.endswith("_")]

    for func in func_list_partial:
        mydict.insert(
            key=Element(etype=Etype.EXECUTABLE_NAME, value=f"{func[:-1]}"),
            value=Element(etype=Etype.FUNCTION, value=eval(func))
        )


def register_compile_primitives(dict_):
    def ifelse_compile():
        exec_array_ifelse = [
            Element(etype=Etype.NUMBER, value=3),
            Element(etype=Etype.NUMBER, value=2),
            Element(etype=Etype.EXECUTABLE_NAME, value="roll"),
            Element(etype=Etype.NUMBER, value=5),
            Element(etype=Etype.OP_JMP_NOT_IF, value="jmp_not_if"),
            Element(etype=Etype.EXECUTABLE_NAME, value="pop"),
            Element(etype=Etype.OP_EXEC, value="exec"),
            Element(etype=Etype.NUMBER, value=4),
            Element(etype=Etype.OP_JMP, value="jmp"),
            Element(etype=Etype.EXECUTABLE_NAME, value="exch"),
            Element(etype=Etype.EXECUTABLE_NAME, value="pop"),
            Element(etype=Etype.OP_EXEC, value="exec"),
        ]
        return exec_array_ifelse

    def exec_compile():
        return [Element(etype=Etype.OP_EXEC, value="exec")]

    def lpop_complile():
        return [Element(etype=Etype.OP_LPOP, value="lpop")]

    def if_compile():
        exec_array_if = [
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.NUMBER, value=1),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.NUMBER, value=4),
            Element(etype=Etype.OP_JMP_NOT_IF, value="jmp_not_if"),
            Element(etype=Etype.NUMBER, value=2),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.OP_EXEC, value="exec"),
        ]
        return exec_array_if

    def while_compile():
        exec_array_while = [
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.NUMBER, value=1),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.OP_EXEC, value="exec"),
            Element(etype=Etype.NUMBER, value=6),
            Element(etype=Etype.OP_JMP_NOT_IF, value="jmp_not_if"),
            Element(etype=Etype.NUMBER, value=0),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.OP_EXEC, value="exec"),
            Element(etype=Etype.NUMBER, value=-9),
            Element(etype=Etype.OP_JMP, value="jmp"),
        ]
        return exec_array_while

    def repeat_compile():
        exec_array_repeat = [
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.NUMBER, value=1),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.NUMBER, value=12),
            Element(etype=Etype.OP_JMP_NOT_IF, value="jmp_not_if"),
            Element(etype=Etype.NUMBER, value=2),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.OP_EXEC, value="exec"),
            Element(etype=Etype.NUMBER, value=1),
            Element(etype=Etype.OP_LOAD, value="load"),
            Element(etype=Etype.NUMBER, value=1),
            Element(etype=Etype.EXECUTABLE_NAME, value="sub"),
            Element(etype=Etype.OP_LPOP, value="lpop"),
            Element(etype=Etype.OP_STORE, value="store"),
            Element(etype=Etype.NUMBER, value=-14),
            Element(etype=Etype.OP_JMP, value="jmp"),
        ]
        return exec_array_repeat

    func_list = [ifelse_compile, exec_compile, while_compile, if_compile, repeat_compile, lpop_complile]  # while_compile

    for func in func_list:
        key = Element(etype=Etype.EXECUTABLE_NAME, value=f"{func.__name__[:-8]}")
        value = Element(etype=Etype.FUNCTION, value=func)
        dict_[key] = value


def main():
    evaluator = Evaluator()
    elems = to_elems(to_char_gen("{1 {1 1 1 add add} if} exec"))
    evaluator.eval(elems)

    evaluator.stack.debug_print()
    #print(evaluator.dict_)



if __name__ == '__main__':
    main()
