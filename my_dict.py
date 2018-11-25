#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by devel on 2018/11/08.


def _hash(key):
    value = 0
    for x in key.value:
        value = (value << 3) + ord(x)
    return value


class Node:
    def __init__(self, key, value, cp=None):
        self.key = key
        self.value = value
        self.next = cp


class Hashtable:
    def __init__(self):
        self.size = 0
        self.hash_size = 1024
        self.hash_table = [None] * self.hash_size
        self.hash_func = _hash

    def _hash_func(self, x):
        return self.hash_func(x) % self.hash_size

    def _search(self, key):
        n = self._hash_func(key)
        cp = self.hash_table[n]
        while cp:
            if cp.key.value == key.value:
                return True, cp
            cp = cp.next
        return False, n # ハッシュの値が返る

    def get(self, key):
        x, y  = self._search(key)
        if x:
            return True, y.value
        return False, None

    def insert(self, key, value):
        x, y = self._search(key)
        if x:
            y.value = value
        else:
            cp = Node(key, value, self.hash_table[y])
            self.hash_table[y] = cp
            self.size += 1
        return value

    def _traverse(self):
        for cp in self.hash_table:
            while cp:
                yield cp.key, cp.value
                cp = cp.next

    def __str__(self):
        if self.size == 0:
            return "Hashtable()"
        s = "Hashtable(\n"
        for key, value in self._traverse():
            s += f"key: {key}  value:{value}\n"
        return s + ")"
