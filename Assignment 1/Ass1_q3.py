import my_library as ml
import matplotlib.pyplot as plt

def matrix_function(x, y, n):
    i1 = x%n
    i2 = y%n
    j1 = x//n
    j2 = y//n
    if x == y:
        return -0.96
    if ((i1+1)%n,j1) == (i2,j2):
        return 0.5
    if (i1,(j1+1)%n) == (i2,j2):
        return 0.5
    if ((i1-1)%n,j1) == (i2,j2):
        return 0.5
    if (i1,(j1-1)%n) == (i2,j2):
        return 0.5
    
    return 0



n = 20
n2 = n**2
A = []
eps = 1e-4


'''
def make_matrix(N, M):
    I = [[0 for x in range(M)] for y in range(N)]
    return I
M = make_matrix(n2,n2)
for i in range(n2):
    for j in range(n2):
        M[i][j] = matrix_function(i,j,n)

print(M)
'''

I=ml.unit_matrix(n2)
for j in range(n2):
    A1 = [[I[i][j]] for i in range(n2)]
    #print("A",A1)
    A1,it,res=ml.conjugate_gradient_on_the_fly(matrix_function, A1, eps)             # sending the function as argument instead of matrix                                                                                 
    print("column=",j)
    for i in range(n2):
        I[i][j] = A1[i][0]

f = open("q3_invers_of_matrix.csv","w+")
#saving the inverse of matrix in text file

for i in range(len(I)):
    for j in range(len(I[i])):
        f.write("{:<15}".format(round(I[i][j],6)))
        f.write('\t')
    f.write('\n')
f.close


# residue plot
plt.plot(it,res,label='Conjugate gradient method by generating matrix on the fly')
plt.xlabel('Iterations')
plt.ylabel('Residue')
plt.legend()
plt.savefig('q3_fig.png')
plt.show()

#print("The inverse of the matrix A::")
#ml.matrix_print(I) 
## inverse of matrix is saved on the file 'q3_invers_of_matrix.csv'

