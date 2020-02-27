"""
>>> import timeutil
>>> timeutil.validate("130 p.m.")
False
>>> timeutil.validate("111:30 p.m")
False
>>> timeutil.validate("01:30 p.m.")
False
>>> timeutil.validate("1:30 pm")
False
>>> timeutil.validate("1:321 p.m.")
False
>>> timeutil.validate("1:30 p.m.")
True

"""
import doctest
doctest.testmod(verbose=True)