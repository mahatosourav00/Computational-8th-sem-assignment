import my_library as ml
import math


#First part

#main function
def fun(x):
    return math.exp(-x**2)

n = 5000

a1 = 0
a2 = 1

ans1 = ml.monte_carlo_integral(a1,a2,fun,n)

print("Calculated integration(without importance sampling) = ", ans1)


#Second part

#probability function
def fun_try(x, alpha):
    return alpha*math.e**(-x)


alpha = math.e/(math.e-1)

ans2 = ml.monte_carlo_integral_prob_fun(a1,a2,fun,fun_try,n,alpha)

print('Calculated integration(with importance sampling) = ',ans2)
print('Analytical Value = ',0.746824132812427)

'''

Calculated integration(without importance sampling) =  0.7450734881895202
Calculated integration(with importance sampling) =  0.7469012482922529




'''

'''
As we can see for same no. of points using importance sampling method better result is 
achieved compared to result obtained from simple monte carlo.
'''

