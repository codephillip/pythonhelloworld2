>>> x = [1,2,4,5,6,67]
>>> x
[1, 2, 4, 5, 6, 67]
>>> x[0]
1
>>> print(x[0])
1
>>> print(x[1])
2
>>> x[0] + x[1]
3
>>> y = ['test', 'hello', true]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> y = ['test', 'hello', True]
>>> y
['test', 'hello', True]
>>> z = x + y
>>> z
[1, 2, 4, 5, 6, 67, 'test', 'hello', True]
>>> len(z)
9
>>> z[len(z)-1]
True
>>> del z[len(z)-1]
>>> z
[1, 2, 4, 5, 6, 67, 'test', 'hello']
>>> del z[len(z)-1]
>>> z
[1, 2, 4, 5, 6, 67, 'test']
>>> z[:3]
[1, 2, 4]
>>> z[3:]
[5, 6, 67, 'test']
>>> z[2:]
[4, 5, 6, 67, 'test']
>>> z[:-3]
[1, 2, 4, 5]
>>> z[3:]
[5, 6, 67, 'test']
>>> z[5:]
[67, 'test']
>>> z[6:]
['test']
>>> z[4:]
[6, 67, 'test']
>>> z[:3]
[1, 2, 4]
>>> z[2:3]
[4]
>>> z[2:6]
[4, 5, 6, 67]
>>> z[-3]
6
>>> z[-1]
'test'

