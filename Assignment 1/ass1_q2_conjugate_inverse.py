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

x0 = [[1],[2],[3],[4],[5],[6]]

eps = 1e-04

for j in range(len(M)):
    N = [[I[i][j]] for i in range(len(M))]
    N, it, res = ml.conjugate_gradient(M,N, x0, eps)

    for i in range(len(M)):
        I[i][j] = N[i][0]

#storing iteration vs res data for later comparision
f = open("q2_iteration_datafile_conjugate_inverse.txt","w+")

for i in range(len(it)):
    f.write("{:<6}{:<15}\n".format(it[i], res[i]))
f.close


print("\nThe inverse matrix is:")
ml.matrix_print(I)

'''

Matrix whose inverse to be calculated:
2.0  -3.0  0.0  0.0  0.0  0.0  
-1.0  4.0  -1.0  0.0  -1.0  0.0
0.0  -1.0  4.0  0.0  0.0  -1.0
0.0  0.0  0.0  2.0  -3.0  0.0
0.0  -1.0  0.0  -1.0  4.0  -1.0
0.0  0.0  -1.0  0.0  -1.0  4.0

The inverse matrix is:
0.9350224624075912  0.8700951489303965  0.2596983769604248  0.20773218145454875  0.41563388142822705  0.1688308734951734
0.29003894167692257  0.5800638124701429  0.17313021614430602  0.13851215498816513  0.27707185293911496  0.11256922782875521
0.08658701725363702  0.17314092631825606  0.32031864584577796  0.0562792619482779  0.11254995838218244  0.10824678476210971
0.20784626256491978  0.41555432820369953  0.16881752979886744  0.9350397668844252  0.8701985083032386  0.2597285930394052
0.13854386882493674  0.277033849907601  0.11254104439466825  0.2900219474999224  0.5801157146669393  0.17316292506930533
0.05628223472883411  0.11253709093396527  0.10821480398309892  0.0865681765391175  0.17316777599536765  0.3203625244970791

'''