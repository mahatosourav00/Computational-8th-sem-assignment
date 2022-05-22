import my_library as ml
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def fun1(x,y,z):
    return (-(n**2)*((math.pi)**2)*y)

def fun2(x,y,z):
    return z


def fun3(x):
    return np.sqrt(2)*np.sin(np.pi*x)

# normalisation function
def normalise(x,y):
    ymod = [abs(yval)**2 for yval in y]
    norm = integrate.simps(ymod,x)
    if norm == 1:
        return y
    else:
        for i in range(len(y)):
            y[i] = y[i]/np.sqrt(norm)
        return y

x0 = 0
xn = 1

y0 = 0
yn = 0

zl0 = 0
zh0 = 5

h = 0.0001

#lowest energy level
n=1
x1,y1 = ml.shoting_method(x0,y0,zh0,zl0,xn,yn,h,fun1,fun2)
y1 = normalise(x1,y1)
#2nd lowest energy level
n=2
x2,y2 = ml.shoting_method(x0,y0,zh0,zl0,xn,yn,h,fun1,fun2)
y2 = normalise(x2,y2)

plt.plot(x1,y1,label='Lowest energy level(n=1)')
plt.plot(x2,y2,label='2nd lowest energy level(n=2)')
plt.title('Solve for Schrodinger equation for infinite square well potential,')
plt.xlabel('position(x)')
plt.ylabel('wavefunction')
plt.legend()
plt.grid()
plt.savefig('plot_ass3_q2.png')
plt.show()
