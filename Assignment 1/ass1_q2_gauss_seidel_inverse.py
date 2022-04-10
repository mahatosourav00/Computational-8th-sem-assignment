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
    N, it, res = ml.gauss_seidel(M,N, xk0, eps)

    for i in range(len(M)):
        I[i][j] = N[i][0]

#storing iteration vs res data for later comparision
f = open("q2_iteration_datafile_gauss_seidel_inverse.txt","w+")

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
0.9351212942602889  0.8700823021978656  0.2598059559740195  0.20774037553018224  0.4155262653918362  0.1688849259681447
0.29006844739312837  0.5800653469391317  0.17318949833277603  0.13850500184516829  0.277030320249557  0.11257810840953553
0.08658914280529613  0.17315252958219926  0.3203568769180118  0.056268727451947755  0.11254476853778872  0.10823374633175872
0.2078383247304324  0.41554549225770676  0.16888492597075422  0.9350225221402364  0.8700822876752787  0.2597842474970288
0.13854872398790424  0.27703890264662595  0.11257810841070034  0.2900243579870069  0.5800653404566084  0.17317980820601592
0.05628446669830009  0.1125478580572063  0.10823374633217803  0.08657327135973866  0.17315252724859928  0.3203533886344436

'''