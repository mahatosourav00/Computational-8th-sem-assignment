import my_library as ml
import matplotlib.pyplot as plt

F = ml.matrix_read("Ass2_q1.txt",'r')

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
    return (((8*x)**2) - (8*x) + 1)

def phi3(x):
    return (((32*x)**3) - ((48*x)**2) + (18*x) -1)

phi = [phi0, phi1, phi2, phi3]


fit,covar = ml.polynomial_fit_chebyshev(X,Y,sig,phi)
    
print("Fitting parameters are: ",fit)
print("Covariance matrix is: ")
ml.matrix_print(covar)
Yn = ml. Chebyshev_fun(X,phi,fit)

plt.plot(X, Y,'go--',label = 'data' )
plt.plot(X, Yn, label = 'Fit with fitting parameters are:\n%s'%fit )
plt.plot(label = 0 )
plt.legend()
plt.show()

'''
Fitting parameters are:  [[2.439357127011113], [1.6990110882124052], [-0.16545334191069927], [0.0002340294684726262]]
Covariance matrix is: 
0.04909872262130023  -0.008669372044218677  -0.6478413531313245  0.7649330719824796
0.005170393317878095  0.11958170003046965  -0.964775779441998  0.9079194468655019
0.00047435572003944813  0.000938578160673179  0.03372177836859711  -0.08279022255105657
-1.3332463506933329e-06  -1.1554598657464848e-06  1.4859635461996592e-06  0.00010189231695482902

'''