# in amu
m_p = 1.007276
m_n = 1.008665
m_e = 0.0005486
a_v = 16.92e-3
a_s = 19.12e-3
a_c = 0.76e-3
a_AS = 25.45e-3
a_0E = 36.50e-3

def delta(A,Z):
    if (A%2 == 0) and (Z%2 == 0):
        return -a_0E*(A**(-3/4))
    elif (A%2 == 0) and (Z%2 == 1):
        return a_0E*(A**(-3/4))
    elif (A%2 == 1):
        return 0

A = int(input('A: '))
Z = int(input('Z: '))

def M(A,Z):
    return Z*m_p + (A-Z)*m_n + Z*m_e - a_v*A + a_s*(A**(2/3)) + a_c*((Z**2)/(A**(1/3))) + a_AS*(((A-2*Z)**2)/A) + delta(A,Z)

print(f'M({A},{Z}) = {M(A,Z)} u')
