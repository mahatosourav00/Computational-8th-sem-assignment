import my_library as ml

M = ml.matrix_read('q1_matrix.txt','r')

print("Equation matrix to be solved is: ")
ml.matrix_print(M)

#separating LHS and RHS of the equations
M = ml.transpose(M)
N = M[-1]
M = M[:-1]
M = ml.transpose(M)
N = ml.transpose(N)

#performing Lu decomposiotion
A = ml.lu_decomposition(M)
#substitution perform
N = ml.forward_substitution(A, N)
N = ml.backward_substituition(A, N)
#print solutions
print("\nThe solutions for the equations following LU decompositon method are:",N)

'''

Equation matrix to be solved is: 
1.0  -1.0  4.0  0.0  2.0  9.0  19.0  
0.0  5.0  -2.0  7.0  8.0  4.0  2.0  
1.0  0.0  5.0  7.0  3.0  -2.0  13.0  
6.0  -1.0  2.0  3.0  0.0  8.0  -7.0  
-4.0  2.0  5.0  0.0  -5.0  3.0  -9.0  
0.0  7.0  -1.0  5.0  4.0  -2.0  2.0  

The solutions for the equations following LU decompositon method are: [[0.9580632153602799], [0.5906976022829514], [4.598808896057574], [-4.1119296504234075], [5.192174074878261], [-1.1274388163404607]]

'''