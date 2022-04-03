import my_library as ml

M = ml.matrix_read('q2_matrix.txt','r')

print("Equation matrix to be solved is: ")
ml.matrix_print(M)

#separating LHS and RHS of the equations
M = ml.transpose(M)
N = M[-1]
M = M[:-1]
M = ml.transpose(M)
N = ml.transpose(N)

#performing LU decomposiotion
A = ml.lu_decomposition(M)
#substitution perform
N = ml.forward_substitution(A, N)
N = ml.backward_substituition(A, N)
print("\nThe solutions for the equations following LU decompositon method are:",N)

