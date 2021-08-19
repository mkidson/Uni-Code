from scipy import *
from math import factorial 
from scipy.interpolate import pade
from scipy.signal import residue
import numpy as np
#import matplotlib
#matplotlib.use('tkagg')
from pylab import *
set_printoptions(precision=4)

""" ***Note: Run from terminal window. Won't work in IDE since interactive.

Pade-Laplace method for Curve-fitting sums of exponential decays. 
Automatically increases n and reports the found poles (decay constants)
and residues (amplitudes).  Also gives average error. 
As described in Hellen, AJP 73, p871 (2005).   
Should also consider varying p0.  Start with inverse of 1/e time.
"""
npts=2001
t = linspace(0,30,npts)
dt=t[1]-t[0]

#Make noisy data, 3-exponential decay with gaussian noise.  The data
#should decay to zero.  
a1=0.5; a2=0.5; a3=0.5; k1=5.0; k2=1.0; k3= 0.2
noise = 0.02
# Note, this assumes data can be negative.
f = a1*exp(-k1*t)+a2*exp(-k2*t)+a3*exp(-k3*t) + noise*(randn(len(t))-0.5)
ion()
figure(1)
plot(t,f,',k')
grid(True); title('Decay Data')
draw()

print('The only input parameter is p0 = 1/t, where t is approx half-time.')
tau = t[np.where(f<=max(f)/2)[0][0]]
# tau = float(input('Enter time used for input param, p0 = 1/time: '))
p0 = 1/tau
print('p0 = ',p0)
print('------------------------------------')

n_decays=5           # Max Number of decay constants tested for.
err=zeros(n_decays)  # To keep track of closeness of fits.

figure(2)
plot(t,f,'kx',label='data')  #Plot data. Pade-Laplace fits added below.
semilogx(); legend()
draw()

for n in arange(1,n_decays+1):  
    print('n = ',n)
    d=zeros(2*n)        #Array for coefs of Taylor Series of Pade appoximant
    for i in arange(0,2*n):
        sm = 0                #Laplace transform and its derivatives.
        for j in arange(1,len(t)-1):
            sm = sm + (-t[j])**i*exp(-p0*t[j])*f[j]
        d[i] = (1.0/factorial(i))*dt*(0.5*((-t[0])**i*exp(-p0*t[0])*f[0]+
                (-t[len(t)-1])**i*exp(-p0*t[len(t)-1])*f[len(t)-1])+sm)

    dAlt=zeros(2*n)
    for c in arange(0,2*n):
        dAlt[c]=(dt * (1/math.factorial(c)) * (0.5*((((-t[0])**c) * np.exp(-p0 * t[0]) * f[0]) + (((-t[-1])**c) * np.exp(-p0 * t[-1]) * f[-1])) + np.sum(((-t[1:-1])**c) * np.exp(-p0 * t[1:-1]) * f[1:-1])))
    
    pAlt, qAlt = pade(dAlt, n, n-1)
    
    resAlt, poleAlt, k = residue(list(pAlt), list(qAlt))

    poles = -(poleAlt+p0)

    print('------------------------------------')
    print('My method')
    print(f'poles at {poles[::-1]}')
    print(f'residues {resAlt[::-1]}')
    print(f'residue mag {abs(resAlt[::-1])}')
    print('------------------------------------')
    print('Ed\'s method')

    M=zeros([n,n])          #Create matrix of d coefficients
    for i in arange(0,n):
        for j in arange(0,n):
            M[i,j]=d[n-1+i-j]

    b=zeros(n)                   #Get the b coeffs
    b=dot(inv(M),-d[n:2*n])  

    a=zeros(n)                  #Get the a coeffs
    for i in arange(0,n):
        a[i]=d[i]
        for j in arange(0,i):    #Note b[0] is b_1 in paper's notation.
            a[i]=a[i]+d[i-j-1]*b[j]  

    #Find poles (zeroes of denominator).  Use poly1d to make polynomial. 
    # b[::-1] reverses order of b. Need to append 1 since 1 + b1 s + b2 s^2 + ...
    # poly1d needs coefficients begining with highest order.  
    denominator = poly1d(append(b[::-1],1),0)
    s=denominator.r        #Gets the roots of the polynomial.

    pole=-(s+p0)         #convert roots to variable p to get exp decay constants
    print('poles at ',pole)

    resid=zeros(n,dtype=complex)  #Get the residues (the amplitudes of exp terms)
    for i in arange(0,n):
        residue_numerator=0
        residue_denominator=b[n-1]
        for j in arange(0,n):
            residue_numerator=residue_numerator+a[j]*s[i]**j
            if j!=i:
                residue_denominator=residue_denominator*(s[i]-s[j])
        resid[i]=residue_numerator/residue_denominator
    print('residues ',resid)
    print('residue mag ',abs(resid))
    print('------------------------------------')

    print(np.round(list(pAlt),4))
    print(np.round(list(qAlt),4))
    print('---')
    print(a[::-1])
    print(b[::-1])
  
    fit=zeros(npts,dtype=complex)         #Create fit from poles and residues
    for i in arange(0,n):
        fit = fit + resid[i]*exp(-pole[i]*t)
    for i in arange(0,npts):           #Get average error from SSE
        err[n-1]=err[n-1]+sqrt((fit[i]-f[i])**2)
    err[n-1] = err[n-1]/npts
    print('error = ',err[n-1])

    figure(2)
    plot(t,fit,label='n = '+str(n),linewidth=2) #Plot each Pade-Laplace fit on data.
    semilogx(); grid(True); legend()
    ylim(-noise,1.1*(a1+a2+a3))
    draw()
    input('Press Enter to continue.')
    print('--------------------------------------------')

# Check for significant improvement in residual error. 1%
small_err = err[0]
small_n = 0
for i in arange(1,n_decays):
    if (small_err-err[i])/small_err > 0.01:
        small_n = i 
        small_err=err[i]
print('Based on error, detected # of decay constants is ',small_n+1)
text(1.5,0.9,(str(small_n+1)+' decay constants detected'),fontsize=14,color='red')
draw()

ioff()
input('Press Enter to end.')
close('all')
show()
