#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.

_input = "123 456 1203"
pos = 0

def parse_one():
    num = ""
    global pos

    for i in range(pos, len(_input)):
        ch = _input[i]
        pos = i+1

        if ch.isalnum():
            num += ch
        if ch.isspace() or i == len(_input)-1:
            return int(num)


def main():
    answer1 = parse_one()
    answer2 = parse_one()
    answer3 = parse_one()

    assert (answer1 == 123)
    assert (answer2 == 456)
    assert (answer3 == 1203)

if __name__ == '__main__':
    main()
