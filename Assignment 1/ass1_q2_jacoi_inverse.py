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

'''
Matrix whose inverse to be calculated:
2.0  -3.0  0.0  0.0  0.0  0.0
-1.0  4.0  -1.0  0.0  -1.0  0.0
0.0  -1.0  4.0  0.0  0.0  -1.0
0.0  0.0  0.0  2.0  -3.0  0.0
0.0  -1.0  0.0  -1.0  4.0  -1.0
0.0  0.0  -1.0  0.0  -1.0  4.0

The inverse matrix is:
0.9351924096255395  0.8701137494547289  0.2598011565211614  0.2077852293724691  0.415545481965912  0.16886716261453733
0.29010516068639985  0.580065351606516  0.17317980820765533  0.1385122183069077  0.27704747513045325  0.11258733248629857
0.08661067905337379  0.1731563043778687  0.32036093489475526  0.05627538153408351  0.11254476891974935  0.10823374633181487
0.20790562532802548  0.4155455008136745  0.16886716261730855  0.9350357510737097  0.870113734969759  0.25980115651903174
0.13859767744898677  0.2770474830321802  0.11258733248746036  0.2900394832302905  0.5800653413248328  0.17317980820614357
0.05630427522111987  0.1125447734430022  0.10823374633247995  0.08657308274762966  0.17315630090163742  0.32036093489424416

'''