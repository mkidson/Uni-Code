# Modules messing around with Gumatj (base 5) numbers
# KDSMIL001
# 25 March 2019

def gumatj_to_decimal(a):
    final = 0
    for i in range(len(str(a))+1):
        b = a % 10
        a //= 10
        final += b*5**i
    return final

def decimal_to_gumatj(a):
    final = 0
    for i in range(len(str(a))+1):
        b = a % 5
        a //= 5
        final += b*10**i
    return final

def gumatj_add(a, b):
    final = gumatj_to_decimal(a) + gumatj_to_decimal(b)
    return decimal_to_gumatj(final)

def gumatj_multiply(a, b):
    final = gumatj_to_decimal(a) * gumatj_to_decimal(b)
    return decimal_to_gumatj(final)

