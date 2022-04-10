import my_library as ml
import matplotlib.pyplot as plt

def matrix_function(x, y, n):
    i1 = x%n
    i2 = y%n
    j1 = x//n
    j2 = y//n
    if x == y:
        return -0.96
    elif ((i1+1)%n,i2)==(j1,j2) or (i1,(i2+1)%n) == (j1,j2) or ((i1-1)%n,i2) == (j1,j2) or (i1,(i2-1)%n) == (j1,j2):
        return 0.5
    else:
        return 0

n = 20
n2 = n**2
A = []
eps = 10e-6
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
plt.show()
plt.savefig('q3_fig.png')
#print("The inverse of the matrix A::")
#ml.matrix_print(I) 
## inverse of matrix is saved on the file 'q3_invers_of_matrix.csv'