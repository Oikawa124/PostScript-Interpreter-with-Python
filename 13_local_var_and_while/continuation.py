#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/14.

class CoStack:
    def __init__(self):
        self.stack = []
        self.local_var = {}
        self.counter = self.counter()
        self.cnt = 0

    def push(self, exec_array, pc):
        self.stack.append((exec_array, pc, self.local_var))
        self.cnt = 0
        self.local_var = {}

    def pop(self):
        try:
            _, _, local_var = self.stack[-1]
            if local_var:
                self.local_var = local_var
            return self.stack.pop()
        except IndexError:
            raise

    def store(self, var):
        num = next(self.counter)
        self.local_var[num] = var
        print(self.local_var)

    def load(self, num):
        return self.local_var[num]

    def counter(self):
        while True:
            yield self.cnt
            self.cnt += 1

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
            if type(v.value) is list:
                print("#EXECUTABLE ARRAY#")
                for j, v in enumerate(v.value):
                    print(f"::{j}:{v.value}")
                print("################")
            else:
                print(f"{i}:{v.value}")


def main():
    pass


if __name__ == '__main__':
    main()
