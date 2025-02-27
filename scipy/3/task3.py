import numpy as np
from sympy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = symbols('x')
y = Function('y')
eq = Eq(y(x).diff(x), -2*y(x))
ics = {y(0): sqrt(2)}
res = dsolve(eq, y(x), ics=ics)
print(res)

l = lambdify(x, res.rhs, 'numpy')
x_vals = np.linspace(0, 10, 100)
y_vals = l(x_vals)


def f(y, t):
    return -2 * y

f0 = sqrt(2)
t = np.linspace(0, 10, 100)
f_num = odeint(f, f0, t)


plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Символьное решение', color='green', linestyle=':')
plt.scatter(t, f_num, label='Численное решение', color='magenta', marker='*', s=25)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Решения дифференциального уравнения')
plt.legend()
plt.grid(True)
#plt.show()
plt.savefig('solutions.png')

plt.figure(figsize=(10, 6))
plt.scatter(t, f_num[:, 0] - y_vals, s=10)
plt.xlabel('t')
plt.ylabel('Разница между решениями')
plt.title('Разница между численным и символьным решениями')
plt.grid(True)
#plt.show()
plt.savefig('difference.png')
