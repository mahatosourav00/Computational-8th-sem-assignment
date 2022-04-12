import my_library as ml
import matplotlib.pyplot as plt
import numpy as np

F = ml.matrix_read("Ass2_q1_data.txt",'r')

F = ml.transpose(F)
#print(F)
X = F[0]
Y = F[1]

sig = [1 for i in range(len(X))]

def phi0(x):
    return 1

def phi1(x):
    return (2*x-1)

def phi2(x):
    return ((8*(x)**2) - (8*x) + 1)

def phi3(x):
    return ((32*(x)**3) - (48*(x)**2) + (18*x) -1)

phi = [phi0, phi1, phi2, phi3]


fit,covar = ml.polynomial_fit_chebyshev(X,Y,sig,phi)
    
print("Fitting parameters are: ",fit)
print("Covariance matrix is: ")
ml.matrix_print(covar)

condition_no = np.linalg.cond(covar, 1)
print("Condition no.: ",condition_no)

Yn = ml. Chebyshev_fun(X,phi,fit)

plt.plot(X, Y,'go--',label = 'data' )
plt.plot(X, Yn, label = 'Fit with fitting parameters are:\n%s'%fit )
plt.plot(label = 0 )
plt.legend()
plt.show()

'''
Fitting parameters are:  [[1.1609694790335525], [0.39351446798815237], [0.04684983209010658], [0.23964617571596986]]
Covariance matrix is: 
0.05554399833576034  2.118889052292686e-17  0.029718565187672727  5.3226006444140366e-17
2.1188890522926858e-17  0.14345628380716105  3.504678676646284e-18  0.036918896568019444
0.029718565187672727  3.504678676646284e-18  0.11144461945377275  7.194797693443246e-18
5.322600644414036e-17  0.036918896568019444  7.194797693443246e-18  0.10032308850005271
Condition no.:  4.797979797979804

'''