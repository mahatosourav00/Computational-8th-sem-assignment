import my_library as ml
import matplotlib.pyplot as plt
import numpy as np

F = ml.matrix_read("Ass2_q1_data.txt",'r')

F = ml.transpose(F)
#print(F)
X = F[0]
Y = F[1]

sig = [1 for i in range(len(X))]

fit, covar = ml.polynomial_fit(X,Y,sig, 3)
print("Fitting parameters are: ",fit)
print("Covariance matrix is: ")
ml.matrix_print(covar)

condition_no = np.linalg.cond(covar, 1)
print("Condition no.: ",condition_no)


Yn = ml.poly_fun(X, 3 ,fit)

plt.plot(X, Y,'go--',label = 'data' )
plt.plot(X, Yn, label = 'Fit with fitting parameters are:\n%s'%fit )
plt.plot(label = 0 )
plt.legend()
plt.show()

'''
Fitting parameters are:  [[0.5746586674195995], [4.725861442142078], [-11.128217777643616], [7.6686776229096685]]
Covariance matrix is: 
0.5440429136080978  -3.9604115691067845  7.716920760397946  -4.3917435221776
-3.960411569106761  42.869122007178575  -97.35581817960204  60.14890835637396
7.716920760397848  -97.35581817960166  238.27685154912544  -154.09626393605663
-4.391743522177528  60.148908356373575  -154.0962639360563  102.73084262403798
Condition no.:  21980.888692411267

'''