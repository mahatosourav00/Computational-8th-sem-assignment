import my_library as ml
import matplotlib.pyplot as plt



def data_seperate(M):
    M = ml.transpose(M)
    X = M[0]
    Y = M[1]
    return X,Y

jacobi = ml.matrix_read("q2_iteration_datafile_jacobi_inverse.txt",'r')
print(jacobi)
gauss_seidel = ml.matrix_read("q2_iteration_datafile_gauss_seidel_inverse.txt",'r')
conjugate = ml.matrix_read("q2_iteration_datafile_conjugate_inverse.txt",'r')

fig,axs = plt.subplots(2, 2)
#plt.suplots_adjust(vspace=0.4)


X, Y = data_seperate(jacobi)
axs[0, 0].plot(X,Y)
axs[0,0].set_title("Jacobi Method")
axs[0,0].set_xlabel("no. of iterations")
axs[0,0].set_ylabel("Residue")

X, Y = data_seperate(gauss_seidel)
axs[0, 1].plot(X,Y)
axs[0, 1].set_title("Gauss-Seidel Method")
axs[0,1].set_xlabel("no. of iterations")
axs[0,1].set_ylabel("Residue")
print('1')

X, Y = data_seperate(conjugate)
axs[1, 0].plot(X,Y)
axs[1,0].set_title("Conjugate Gradient Method")
axs[1,0].set_xlabel("no. of iterations")
axs[1,0].set_ylabel("Residue")
print('2')

X, Y = data_seperate(jacobi)
axs[1, 1].plot(X,Y,label='Jacobi')
X, Y = data_seperate(gauss_seidel)
axs[1, 1].plot(X,Y,label='Gauss-Seidel')
X, Y = data_seperate(conjugate)
axs[1, 1].plot(X,Y,label='Conjugate Gradient')
axs[1,1].set_title("All Together")
axs[1,1].set_xlabel("no. of iterations")
axs[1,1].set_ylabel("Residue")
#axs[1,1].set_xlim(0,40)
axs[1,1].legend()
#axs[1,1].set_yscale('log')
print('3')

fig.suptitle('No. of iteration vs Residue plots for\nJacobi, Gauss-Seidel, Conjugate Gradient Method')
fig.tight_layout()




fig.savefig('q2_iteration vs residue plot.png')
plt.show()