import matplotlib.pyplot as plt
import numpy as np

with open('2.dat', 'r') as f:
    N = 6
    arrays = {}
    for i in range(1, N + 1):
        arrays[f'x_{i}'] = [float(j) for j in f.readline().split()]
        arrays[f'y_{i}'] = [float(j) for j in f.readline().split()]

def plotp(x, y, i):
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, color='darkviolet', linewidth=2)
    plt.title(f'Frame {i}')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.xlim(0, 16)
    plt.ylim(-10, 12)

    plt.minorticks_on()
    plt.grid(which='major', color='gray', linewidth=1)
    plt.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)
    plt.yticks(np.arange(-10, 13, 2))
    minor_yticks = np.arange(-10, 12, 1)
    plt.gca().set_yticks(minor_yticks, minor=True)
    plt.savefig(f'frame_{i}.png')

for i in range(1, N + 1):
    x = arrays[f'x_{i}']
    y = arrays[f'y_{i}']
    plotp(x, y, i)
