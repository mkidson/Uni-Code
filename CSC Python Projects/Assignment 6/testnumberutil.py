"""

>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(15)
'fifteen'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(32)
'thirty two'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(115)
'one hundred and fifteen'
>>> numberutil.aswords(130)
'one hundred and thirty'
>>> numberutil.aswords(132)
'one hundred and thirty two'

"""

import doctest
doctest.testmod(verbose=True)