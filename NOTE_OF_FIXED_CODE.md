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


## parse_one()
### Before その1
```
def parse_one(prev_ch):
    ch = gets() if prev_ch == '' else prev_ch
    if not ch: return '', Token(ltype=Ltype.END_OF_FILE)

    if ch.isdigit():
        num = 0
        while ch.isdigit():
            num = num*10 + int(ch)
            ch = gets()
        return ch, Token(ltype=Ltype.NUMBER, value=num)

    elif ch.isalpha():
        word = ""
        while ch.isalpha() or ch.isalnum():
            word += ch
            ch = gets()
        return ch, Token(ltype=Ltype.EXECUTABLE_NAME, value=word)

    elif ch == '/':
        word = ch
        ch = gets()
        while ch.isalpha() or ch.isdigit():
            word += ch
            ch = gets()
        return ch, Token(ltype=Ltype.LITERAL_NAME, value=word)

    elif ch.isspace():
        while ch.isspace(): ch = gets()
        return ch, Token(ltype=Ltype.SPACE)

    elif ch == "{":
        ch = gets()
        return ch, Token(ltype=Ltype.OPEN_CURLY)

    elif ch == "}":
        ch = gets()
        return ch, Token(ltype=Ltype.CLOSE_CURLY)

    elif not ch:
        return ch, Token(ltype=Ltype.END_OF_FILE)

    else:
        return ch, Token(ltype=Ltype.UNKNOWN)


def parser_print_all():
    ch = ""
    while True:
        ch, token = parse_one(ch)

        if token.ltype == Ltype.END_OF_FILE:
            break

        if token.ltype == Ltype.NUMBER:
            print(f"num: {token.value}")
        elif token.ltype == Ltype.SPACE:
            print("space")
        elif token.ltype == Ltype.OPEN_CURLY:
            print("open curly brace")
        elif token.ltype == Ltype.CLOSE_CURLY:
            print("close curly brace")
        elif token.ltype == Ltype.EXECUTABLE_NAME:
            print(f"executable name: {token.value}")
        elif token.Ltype == Ltype.LITERAL_NAME:
            print(f"literal name {token.value}")
        else:
            print(f"Unknown type : {token.ltype}")
```
### Before その2

```
def parse_one(gene):

    # next()のラッパー
    def next_ch(gene):
        try:
            return next(gene)
        except StopIteration:
            return ""

    def return_token_and_gene(Ltype, value, gene, ch=None):
        token = Token(ltype=Ltype, value=value)
        if ch: gene = (x for g in ([ch], gene) for x in g)

        return token, gene

    ch = next_ch(gene)

    if ch.isdigit():
        num = int(ch)
        ch = next_ch(gene)
        while ch.isdigit():
            num = num * 10 + int(ch)
            ch = next_ch(gene)
        return return_token_and_gene(Ltype.NUMBER, num, gene, ch=ch)

    elif ch.isalpha():
        word = ch
        while ch.isalpha():
            word += ch
            ch = next_ch(ch)
        return return_token_and_gene(Ltype.EXECUTABLE_NAME, word, gene, ch=ch)

    elif ch == '/':
        word = ch
        while ch.isalpha():
            word += ch
            ch = next_ch(ch)
        return return_token_and_gene(Ltype.LITERAL_NAME, word, gene, ch=ch)

    elif ch == "{":
        return return_token_and_gene(ch, Ltype.OPEN_CURLY, "{", gene)

    elif ch == "}":
        return return_token_and_gene(Ltype.CLOSE_CURLY, "}", gene)

    elif ch == ' ':
        return return_token_and_gene(Ltype.SPACE, ' ', gene)

    elif ch == "":
        return_token_and_gene(Ltype.END_OF_FILE, "", gene)
    else:
        return return_token_and_gene(ch, Ltype.UNKNOWN, "UNKNOWN", gene)
```
・returnの処理が分かりにくい  
・ラッパー関数が大げさかもしれない?  
・関数に複数の機能を持たせるのは良くないのかもしれない。

### After
```
def parse_one(gene):
    # next()のラッパー
    def next_ch(gene):
        try:
            return next(gene)
        except StopIteration:
            return ""


    def chain(ch, gene):
        return (x for g in ([ch], gene) for x in g)

    ch = next_ch(gene)

    if ch.isdigit():
        num = int(ch)
        ch = next_ch(gene)
        while ch.isdigit():
            num = num * 10 + int(ch)
            ch = next_ch(gene)
        return Token(Ltype.NUMBER, num), chain(ch, gene)

    elif ch.isalpha():
        word = ch
        while ch.isalpha():
            word += ch
            ch = next_ch(ch)
            return Token(Ltype.EXECUTABLE_NAME, word), chain(ch, gene)

    elif ch == '/':
        word = ch
        while ch.isalpha():
            word += ch
            ch = next_ch(ch)
        return Token(Ltype.LITERAL_NAME, word), chain(ch, gene)

    elif ch == "{":
        return Token(Ltype.OPEN_CURLY, "{"), gene

    elif ch == "}":
        return Token(Ltype.CLOSE_CURLY, "}"), gene

    elif ch == ' ':
        return Token(Ltype.SPACE, ' '), gene

    elif ch == "":
        return Token(Ltype.END_OF_FILE, ""), gene
    else:
        return Token(Ltype.UNKNOWN, "UNKNOWN"), gene
```
・return 部分が分かりやすくなった。  
・ヘルパー関数を小さくした。

# stack.py

## Elementの実装
クラスの実装からnamedtupleへ  
Tokenと同じような実装

# Stackの実装
### Before
```
class Stack:
    def __init__(self, stack = None):
        if type(stack) is type([]):
            self.stack = stack
        elif stack is None:
            self.stack = []
        else:
            print("There is Not list type")

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        try:
            pop_elem = self.stack.pop()
            return pop_elem
        except IndexError as ex:
            logger.error(ex)
            raise

    def print_all(self):
        for i, v in enumerate(self.stack):
            if v.Etype == Etype.NUMBER:
                print(f"{i} || Type: {v.Etype}, value: {v.number}")
            elif v.Etype == Etype.LITERAL_NAME:
                print(f"{i} || Type: {v.Etype}, value: {v.name}")
            elif v.Etype == Etype.EXECUTABLE_NAME:
                print(f"{i} || Type: {v.Etype}, value: {v.name}")
            else:
                print("{i} || UNKNOWN")
```


### After
```
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

    def print_all(self):
        for i, v in enumerate(self.stack):
            if v.etype == Etype.NUMBER:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            elif v.etype == Etype.LITERAL_NAME:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            elif v.etype == Etype.EXECUTABLE_NAME:
                print(f"{i} || Type: {v.etype}, value: {v.value}")
            else:
                print("{i} || UNKNOWN")
```
・Stackの引数にlistを渡す必要がないため削除  
・pop()のところで、ローカル変数が必要がないために削除  
・使わない機能を残しておくのは、良くないことだと思う。