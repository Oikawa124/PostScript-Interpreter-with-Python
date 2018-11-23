#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/14.

class CoStack:
    def __init__(self):
        self.stack = []

    def push(self, exec_array, pc):
        self.stack.append((True, (exec_array, pc)))

    def pop_till_next_ex_arr(self):
        try:
            is_cont, cont_or_val = self.stack.pop()
            while not is_cont:
                if self.is_empty():
                    return ([], 0)
                is_cont, cont_or_val = self.stack.pop()
            return cont_or_val
        except IndexError:
            raise

    def one_pop(self):
        try:
            self.stack.pop()
        except IndexError:
            raise

    def store(self, val):
        self.stack.append((False, val))

    def load(self, index):
        return self.stack[-index][1]

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def __str__(self):
        if self.stack is None:
            return "Stack()"
        s = "stack(\n"
        for i, v in enumerate(self.stack):
            s += f"{i}:{v}\n"
        return s + ")"

    def debug_print(self):
        if self.stack is None:
            print("Stack()")
        for i, v in enumerate(self.stack):
            if type(v) is tuple:
                print("#EXECUTABLE ARRAY#")
                for j, v in enumerate(v.value):
                    print(f"::{j}:{v}")
                print("################")
            else:
                print(f"{i}:{v.value}")
