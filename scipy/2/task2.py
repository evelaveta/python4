from sympy import *
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

with open('2_large.txt', 'r') as file:
    N = int(file.readline())
    A = np.zeros((N, N))
    for i in range(N):
        A[i] = np.array([float(x) for x in file.readline().split()])
    b = np.array([float(x) for x in file.readline().split()])

x_num = solve(A, b)
plt.bar(range(len(x_num)), x_num)
plt.xlabel('Индекс решения')
plt.ylabel('Значение решения')
plt.title('Численное решение системы линейных уравнений')
plt.grid()
#plt.show()
plt.savefig('2_large.png')

A_sym = Matrix(A)
b_sym = Matrix(b)
x_sym = A_sym.solve(b_sym)
print("Символьное решение:", x_sym)
