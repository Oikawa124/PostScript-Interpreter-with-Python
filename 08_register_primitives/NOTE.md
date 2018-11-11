# メモ

## DIについて


```
class Evaluator:
    def __init__(self):
        self.stack = Stack()
        self.dict_ = Hashtable()
        register_primitives(self.stack, self.dict_)
```
よりも、
```
class Evaluator:
    def __init__(self, stack, dict_):
        self.stack = stack
        self.dict_ = dict_
        register_primitives(self.stack, self.dict_)
 ```

としたほうが、EvaluatorがStackやHashtableクラスの名前を知っている必要がなくなるため、
依存関係が少なくなる。
が、今回の場合はやりすぎ。
