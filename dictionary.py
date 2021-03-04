>>> x = dict()
>>> x
{}
>>> len(x)
0
>>> x.append({'time':24})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'append'
>>> x.update({'time':24})
>>> x
{'time': 24}
>>> x
{'time': 24}
>>> x['time']
24
>>> x['time'] = 49
>>> x
{'time': 49}

