#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/04.
input_ = "123 456"


def gets_set_src(string):
    global input_
    input_ = string


def gets():
    global input_
    return (x for x in input_)
