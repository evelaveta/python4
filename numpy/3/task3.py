import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

u = np.loadtxt('3.dat')
N = len(u)

A = np.eye(N) - np.roll(np.eye(N), 1, axis=1)

all_u = np.zeros((255, N))
all_u[0] = u

for n in range(254):
    u_next = u - 0.5 * np.dot(A, u)
    u = u_next
    all_u[n+1] = u

for i in range(N):
    plt.figure(figsize=(10, 6))
    plt.plot(all_u[:, i])
    plt.title('Эволюция процесса')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.savefig(f'variable_{i + 1}.png')


files = [f'variable_{i + 1}.png' for i in range(len(u))]

with imageio.get_writer('animation.gif', mode='I', fps=5) as writer:
    for file in files:
        image = imageio.imread(file)
        writer.append_data(image)

for file in files:
    os.remove(file)
