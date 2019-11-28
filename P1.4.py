Python 3.9.0a1 (v3.9.0a1:fd757083df, Nov 19 2019, 10:51:29) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)
{'orange', 'apple', 'pear', 'banana'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'b', 'd', 'r', 'c', 'a'}
>>> a-b
{'d', 'b', 'r'}
>>> a|b
{'b', 'z', 'm', 'l', 'd', 'r', 'c', 'a'}
>>> a&b
{'c', 'a'}
>>> a^b
{'l', 'd', 'z', 'b', 'r', 'm'}
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'d', 'r'}
>>> 