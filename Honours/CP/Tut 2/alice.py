#SPI using Gaussian kernal function
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

#Functions we want to interpolate
def f(x):
    return 3*(x**4)-3*(x**2)
def d1_f(x):
    return 12*(x**3)-6*(x)
def d2_f(x):
    return 36*(x**2)-6

def spi(N, h):
    #Our initial "data":
    x_data = np.linspace(-10,10,2*N)
    y_data = f(x_data)
    #y_d1 = d1_f(x_data)
    #y_d2 = d2_f(x_data)

    #Interpolation values:
    #Only on the interval [-5,5], a subset of the total data interval
    x_int = np.linspace(-5,5,N)
    y_int = np.zeros(N)
    #y_1 = np.zeros(N)
    #y_2 = np.zeros(N)

    for j in range(N):
        y = 0
        y_dash = 0
        y_ddash = 0
        for i in np.arange(1,N): #Begin at second data point
            #Gaussian Kernal
            W = (1/(h*np.sqrt(np.pi)))*np.exp(-(((x_data[i]-x_int[j])/h)**2))
            #W_dash = (1/((h**3)*np.sqrt(np.pi)))*np.exp(-(((x_data[i]-x_int[j])/h)**2))*(-2*x_data[i]+2*x_int[j])
            #W_ddash = (1/((h**5)*np.sqrt(np.pi)))*(np.exp(-(((x_data[i]-x_int[j])/h)**2))*((-2*x_data[i]+2*x_int[j])**2)-(2*(h**2)*np.exp(-(((x_data[i]-x_int[j])/h)**2))))

            del_x = ((x_data[i]+x_data[i+1])/2) - ((x_data[i]+x_data[i-1])/2)
            y = y + del_x*y_data[i]*W
            #y_dash = y_dash + del_x*y_data[i]*W_dash
            #y_ddash = y_ddash + del_x*y_data[i]*W_ddash

        y_int[j] = y
        #y_1[j] = -y_dash
        #y_2[j] = y_ddash
    """
    plt.plot(x_data,y_data,label= 'Function')
    plt.plot(x_int,y_int, label = 'SPI')
    plt.legend()
    plt.title("SPI vs plotted function.")
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.show()

    plt.plot(x_data,y_d1,label= 'First Derivative of function.')
    plt.plot(x_int,y_1, label = 'SPI')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("SPI vs plotted 1st derivative.")
    #plt.show()

    plt.plot(x_data,y_d2,label= 'Second derivative of function.')
    plt.plot(x_int,y_2, label = 'SPI')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("SPI vs plotted 2nd derivative.")
    #plt.show()
    """
    #Now we calculate the errors (differences between SPI and functions)
    error = np.zeros(N)
    #error_d1 =np.zeros(N)
    #error_d2 =np.zeros(N)

    for x in range(N):
        error[x] = np.abs(y_int[x] - f(x_int[x]))
        #error_d1[x] = y_1[x] - d1_f(x_int[x])
        #error_d2[x] = y_2[x] - d2_f(x_int[x])
    return (np.sum(error))
    """
    plt.plot(x_int, error)
    plt.title("Differences between SPI and function.")
    plt.xlabel("x-values")
    plt.ylabel("Error")
    #plt.show()

    plt.plot(x_int, error_d1)
    plt.title("Differences between SPI and 1st derivative.")
    plt.xlabel("x-values")
    plt.ylabel("Error")
    #plt.show()

    plt.plot(x_int, error_d2)
    plt.title("Differences between SPI and 2nd derivative.")
    plt.xlabel("x-values")
    plt.ylabel("Error")
    #plt.show()
    """
def err(N, h):

    x_data = np.linspace(-10,10,2*N)
    y_data = f(x_data)

    x_int = np.linspace(-5,5,N)
    y_int = np.zeros(N)

    for j in range(N):
        y = 0
        for i in np.arange(1,N): #Begin at second data point
            #Gaussian Kernal
            W = (1/(h*np.sqrt(np.pi)))*np.exp(-(((x_data[i]-x_int[j])/h)**2))
            del_x = ((x_data[i]+x_data[i+1])/2) - ((x_data[i]+x_data[i-1])/2)
            y = y + del_x*y_data[i]*W
        y_int[j] = y
    #Now we calculate the errors (differences between SPI and functions)
    error = np.zeros(N)
    for x in range(N):
        error[x] = np.abs(f(x_int[x])-y_int[x])

    tot_error = np.sum(error)
    return tot_error
#spi(30,0.5)

#To investigate the overall error as a function of SPI parameters, we vary the number of interpolated points and the smoothing length:
h = np.linspace(0.3,1.5,25)
N = np.arange(20,45, 1)
Z = np.zeros((len(N),len(h)))

for i in range (len(N)):
    for j in range(len(h)):
        Z[i][j] = spi(N[i],h[j])

fig,ax=plt.subplots(1,1)
cp = ax.contourf(N,h,Z)
fig.colorbar(cp)
ax.set_title('Error Contour Plot')
ax.set_ylabel('Number of particles (N)')
ax.set_xlabel('Smoothing length (h)')
plt.show()
