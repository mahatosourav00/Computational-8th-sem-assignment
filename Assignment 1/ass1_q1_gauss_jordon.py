import my_library as ml

M = ml.matrix_read('q1_matrix.txt','r')

print("Equation matrix to be solved is: ")
ml.matrix_print(M)

A = ml.gauss_jordan_solution(M)


print("\nThe solutions for the equations following gauss-jordon method are:",[j[len(j)-1] for j in A])


'''
Equation matrix to be solved is:
1.0  -1.0  4.0  0.0  2.0  9.0  19.0  
0.0  5.0  -2.0  7.0  8.0  4.0  2.0  
1.0  0.0  5.0  7.0  3.0  -2.0  13.0  
6.0  -1.0  2.0  3.0  0.0  8.0  -7.0  
-4.0  2.0  5.0  0.0  -5.0  3.0  -9.0  
0.0  7.0  -1.0  5.0  4.0  -2.0  2.0  

The solutions for the equations following gauss-jordon method are: [0.9580632153602853, 0.5906976022829493, 4.5988088960575695, -4.1119296504234, 5.1921740748782526, -1.127438816340457]

'''