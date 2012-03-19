Python 2.7.2 (default, Jun 12 2011, 15:08:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(int)
<type 'type'>
>>> type(type)
<type 'type'>
>>> type(lambda:None)
<type 'function'>
>>> def g(xxxxx):
	return jdfhkhkjfhdskjfskd

>>> lambda xxxxx: jdfhkhkjfhdskjfskd
<function <lambda> at 0x02A4F070>
>>> g
<function g at 0x02A49BF0>
>>> d = lambda xxxxx: jdfhkhkjfhdskjfskd
>>> d
<function <lambda> at 0x02A4F070>
>>> def g(xxxxx):
	a = 1
	return jdfhkhkjfhdskjfskd

>>> class X(object):
	pass

>>> type(X)
<type 'type'>
>>> X() == None
False
>>> int()
0
>>> float()
0.0
>>> str()
''
>>> list()
[]
>>> X()
<__main__.X object at 0x02A526B0>
>>> x = X()
>>> x.asdf = int()
>>> x.asdf
0
>>> def test():
	x = X()
	assert x.machwas() == 0

	
>>> assert True
>>> assert False

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    assert False
AssertionError
>>> assert True, 'was bedeutet der fehler'
>>> assert False, 'was bedeutet der fehler'

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    assert False, 'was bedeutet der fehler'
AssertionError: was bedeutet der fehler
>>> def test():
	x = X()
	assert x.machwas() == 0

	
>>> test()

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    test()
  File "<pyshell#34>", line 3, in test
    assert x.machwas() == 0
AttributeError: 'X' object has no attribute 'machwas'
>>> class X(object):
	
	def machwas(self):
		return 0

	
>>> test()
>>> class X(object):

	def machwas(self):
		print 'machwas'
		return 0

	
>>> test()
machwas
>>> class X(object):

	def machwas(self):
		print self
		return 0

	
>>> x =
SyntaxError: invalid syntax
>>> x = X()
>>> x
<__main__.X object at 0x02A738D0>
>>> x.machwas()
<__main__.X object at 0x02A738D0>
0
>>> X
<class '__main__.X'>
>>> X.machwas
<unbound method X.machwas>
>>> X.machwas(x)
<__main__.X object at 0x02A738D0>
0
>>> x.machwas()
<__main__.X object at 0x02A738D0>
0
>>> 
