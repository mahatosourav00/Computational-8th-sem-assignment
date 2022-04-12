from base64 import b16decode
import my_library as ml
import math


#for Steinmetz solid, it is intersection of two cylinders
# so in montecarlo the shooting poin will be counted if x^2+y^2 <= 1 and y^2 + z^2 <= 1(equations of two circles)

#function for first equation
def circle1(x, y):
    return math.sqrt((x**2 + y**2))
#function for second equation
def circle2(y, z):
    return math.sqrt((y**2 + z**2))


#define limits
a1 = -1
a2 = 1

b1 = -1
b2 = 1

c1 = -1
c2 = 1

N = 90000

volume = ml.monte_carlo_steinmetz_vol(a1,a2,b1,b2,c1,c2,circle1,circle2,N)

print("Volume of Steinmetz = ", volume)

'''
Volume of Steinmetz =  5.339555555555556

'''