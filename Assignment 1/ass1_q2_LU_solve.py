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

'''
2.0  -3.0  0.0  0.0  0.0  0.0  -1.666666  
-1.0  4.0  -1.0  0.0  -1.0  0.0  0.666666
0.0  -1.0  4.0  0.0  0.0  -1.0  3.0
0.0  0.0  0.0  2.0  -3.0  0.0  -1.333333
0.0  -1.0  0.0  -1.0  4.0  -1.0  -0.333333
0.0  0.0  -1.0  0.0  -1.0  4.0  1.666666

The solutions for the equations following LU decompositon method are: [[-0.3333331948051949], [0.3333332034632034], [0.9999999264069264], [-0.6666663766233767], [8.225108226943767e-08], [0.6666665021645022]]

'''