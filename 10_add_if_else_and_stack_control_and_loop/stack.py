#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise

    def gene(self): # listの要素を返すジェネレータ
        for val in self.stack:
            yield val

    def seek(self, index):
        return self.stack[len(self.stack) - index -1]

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
            if type(v.value) is list:
                print("#EXECUTABLE ARRAY#")
                for j, v in enumerate(v.value):
                    print(f"::{j}:{v.value}")
                print("################")
            else:
                print(f"{i}:{v.value}")
