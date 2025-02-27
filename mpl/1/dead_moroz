import matplotlib.pyplot as plt

def readf(filename):
    with open(filename, 'r') as f:
        N = int(f.readline())
        x = [0] * N
        y = [0] * N
        for i in range(N):
            x[i], y[i] = map(float, f.readline().split())
    return N, x, y

def plotp(N, x, y, filename, i):
    k = (max(y) - min(y)) / (max(x) - min(x))
    plt.figure(figsize=(20, 20 * k))
    plt.scatter(x, y, color='darkviolet', marker='o', s=5)
    plt.title(f'Test: {filename} (Number of points: {N})')
    plt.xlabel('X')
    plt.ylabel('Y')

    fname =f'/Users/evelaveta/Desktop/Programming/term4/mpl/1/{i:03}.png'
    plt.savefig(fname)
    #plt.show()

for i in range(1, 6):
    f = '00' + str(i) + '.dat'
    filename = f'{i:03}.dat'
    N, x, y = readf(filename)
    plotp(N, x, y, filename, i)
