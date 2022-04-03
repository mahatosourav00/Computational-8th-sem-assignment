import my_library as ml
import matplotlib.pyplot as plt

M = ml.matrix_read('q2_matrix.txt','r')

print("Equation matrix to be solved is: ")
ml.matrix_print(M)

#separating LHS and RHS of the equations
M = ml.transpose(M)
N = M[-1]
M = M[:-1]
M = ml.transpose(M)
N = ml.transpose(N)

xk0 = [[1],[2],[3],[4],[5],[6]]

eps = 1e-04

print(eps)
A, i, r = ml.jacobi(M,N,xk0,eps)
#print(i)
#print(r)
'''
plt.plot(i,r)
plt.ylabel('residue')
plt.xlabel('no. of iterations')
plt.title('Jacobi method')
plt.grid(True)
plt.show()
'''
print("\nThe solutions for the equations following Jacobi method are:",A)

