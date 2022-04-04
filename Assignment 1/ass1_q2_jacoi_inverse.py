import my_library as ml
import matplotlib.pyplot as plt

M = ml.matrix_read('q2_matrix.txt','r')



#eliminating RHS of the equations
M = ml.transpose(M)
M = M[:-1]
M = ml.transpose(M)

print("\nMatrix whose inverse to be calculated: ")
ml.matrix_print(M)

I = ml.unit_matrix(len(M))

xk0 = [[1],[2],[3],[4],[5],[6]]

eps = 1e-04

for j in range(len(M)):
    N = [[I[i][j]] for i in range(len(M))]
    N, it, res = ml.jacobi(M,N, xk0, eps)

    for i in range(len(M)):
        I[i][j] = N[i][0]

#storing iteration vs res data for later comparision
f = open("q2_iteration_datafile_jacobi_inverse.txt","w+")

for i in range(len(it)):
    f.write("{:<6}{:<15}\n".format(it[i], res[i]))
f.close


print("\nThe inverse matrix is:")
ml.matrix_print(I)
