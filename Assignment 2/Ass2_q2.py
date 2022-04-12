import my_library as ml
import math



#function for montecarlo integration
def fun(x):
    y = math.sqrt(1-(x**2))
    return y

a1 = 0
a2 = 1
N = 50000
#Monte carlo integration for a=65, m=1021
A = ml.monte_carlo_integral(a1, a2, fun, N, a = 65, m = 1021)
print("Value of Pi for Monte carlo integration (a=65, m=1021)",4*A)
#Monte carlo integration for a=572, m=16381
A = ml.monte_carlo_integral(a1, a2, fun, N, a = 572, m = 16381)
print("Value of Pi for Monte carlo integration (a=572, m=16381)",4*A)


#function for monte carlo shooting method
def circle(x, y):
    return math.sqrt((x**2 + y**2))


a1 = -1
a2 = 1

b1 = -1
b2 = 1
#Monte carlo shooting method for a=65, m=1021
A = ml.monte_carlo_circle_area(a1, a2, b1, b2, circle, N, a = 65, m = 1021)
print("Value of Pi for Monte carlo shooting method (a=65, m=1021)",A)
#Monte carlo shooting method for a=572, m=16381
A = ml.monte_carlo_circle_area(a1, a2, b1, b2, circle, N, a = 572, m = 16381)
print("Value of Pi for Monte carlo shooting method (a=572, m=16381)",A)


'''
Value of Pi for Monte carlo integration (a=65, m=1021) 3.1426744211306716
Value of Pi for Monte carlo integration (a=572, m=16381) 3.1409144676992775
Value of Pi for Monte carlo shooting method (a=65, m=1021) 3.14352
Value of Pi for Monte carlo shooting method (a=572, m=16381) 3.1366400000000003

'''