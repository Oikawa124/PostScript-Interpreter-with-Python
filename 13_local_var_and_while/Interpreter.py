#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/22.
from eval import *


def main():
    with open("test.ps") as f:
        s = f.read()
        evaluator = Evaluator()
        elems = to_elems(to_char_gen(s))
        evaluator.eval(elems)
        print(evaluator.stack)


if __name__ == '__main__':
    main()
