# コード修正の前後を記録


## gets.py

### Before
```
_input = "123 456"
pos = 0

def gets_set_src(string):
    global _input
    input = string


def gets ():
    global pos
    if len(_input) == pos:
        return '\0'
    ch = _input[pos]
    pos += 1
    return ch
```
### After
```
input_ = "123 456"


def gets_set_src(string):
    global input_
    input_ = string


def gets():
    global input_
    return (x for x in input_)
```
一文字づつreturnで返すのではなく、ジェネレータにして返すように変更。

## my_parser.py
###Tokenの実装

###Before
```
class Token:
    def __init__(self, ltype=None, value=None):
        self._ltype = ltype
        self._value = value

    def get_ltype(self):
        return self._ltype

    def set_ltype(self, ltype):
        self._ltype = ltype

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    ltype = property(get_ltype, set_ltype)
    value = property(get_value, set_value)
```
### After
```
from collections import namedtuple
Token = namedtuple("Token", ("ltype", "value"))
```
クラスで実装するほどではないため、namedtupleを使う。