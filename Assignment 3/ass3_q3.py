
import my_library as ml
import numpy as np
import matplotlib.pyplot as plt


n = 50
U = np.zeros(shape=(n,n))



U[0,:] = 0
U[-1,:] = 1
U[:,0] = 0
U[:,-1] = 0 
Uold = U.copy()
#print(U)

eps = 0.00001
steps = 500
Unew = ml.laplace_solve(U,steps,eps)


fig, (ax1, ax2,) = plt.subplots(1,2)

fig.suptitle('Laplace solve')
im1 = ax1.imshow(Uold, aspect='auto',cmap = "gray")
ax1.set_title('Initial Matrix')
ax1.set_xlabel('x axis ->')
ax1.set_ylabel('y axis --> ')
im2 = ax2.imshow(Unew, aspect='auto',cmap = "gray")
ax2.set_title('Final Matrix')
ax2.set_xlabel('x axis -->')
ax2.set_ylabel('y axis --> ')
plt.tight_layout()
plt.savefig('plot_ass3_q3.png')
plt.show()