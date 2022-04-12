import my_library as ml
import matplotlib.pyplot as plt

F = ml.matrix_read("Ass2_q1.txt",'r')

F = ml.transpose(F)
#print(F)
X = F[0]
Y = F[1]

sig = [1 for i in range(len(X))]

fit, covar = ml.polynomial_fit(X,Y,sig, 3)
print("Fitting parameters are: ",fit)
print("Covariance matrix is: ")
ml.matrix_print(covar)
Yn = ml.poly_fun(X, 3 ,fit)

plt.plot(X, Y,'go--',label = 'data' )
plt.plot(X, Yn, label = 'Fit with fitting parameters are:\n%s'%fit )
plt.plot(label = 0 )
plt.legend()
plt.show()

'''
Fitting parameters are:  [[0.5746586674195995], [4.725861442142078], [-11.128217777643616], [7.6686776229096685]]
Covariance matrix is: 
0.05595529072557773  -0.2591764908821467  -0.1250564034737248  -0.05338707525025874
-0.020195911015934022  0.3732283040317623  0.6436942454513308  0.046719765541034776
0.0024981461271529  0.18926240746656434  -0.39931220029600956  0.7186947310800936
0.003459730062195539  0.030086411359451972  -0.22993924120941198  -0.8210546310068212

'''