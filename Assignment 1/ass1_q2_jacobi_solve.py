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
A, it, res = ml.jacobi(M,N,xk0,eps)

f = open("generated iteration data_jacobi.txt","w+")

for i in range(len(it)):
    f.write("{:<6}{:<15}\n".format(it[i], res[i]))
f.close

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

'''

Equation matrix to be solved is: 
2.0  -3.0  0.0  0.0  0.0  0.0  -1.666666  
-1.0  4.0  -1.0  0.0  -1.0  0.0  0.666666  
0.0  -1.0  4.0  0.0  0.0  -1.0  3.0  
0.0  0.0  0.0  2.0  -3.0  0.0  -1.333333  
0.0  -1.0  0.0  -1.0  4.0  -1.0  -0.333333  
0.0  0.0  -1.0  0.0  -1.0  4.0  1.666666  
0.0001

The solutions for the equations following Jacobi method are: [[-0.3332031511206105], [0.3333945702755737], [1.0000311354413247], [-0.6665538826797187], [7.102266026022541e-05], [0.6666934994567448]]


'''