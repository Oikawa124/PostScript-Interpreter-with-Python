#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/05.

class A:
    def __init__(self, etype=None, value=None):
        self._etype = etype
        self._value = value

    def get_etype(self):
        return self._etype

    def set_etype(self, etype):
        self._etype = etype

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    etype = property(get_etype, set_etype)
    value = property(get_value, set_value)

def main():
    a = A("a", 1)
    print(a.etype)
    print(a.value)


if __name__ == '__main__':
    main()
