import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    data = np.loadtxt(filename)
    return data

def showi(data, filename):
    plt.plot(data)
    plt.title('Сигнал датчика')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда')
    plt.savefig(filename)
    plt.close()

def calculate_av(data):
    window_size = 10
    av = np.zeros_like(data)

    for i in range(len(data)):
        start_idx = max(0, i - window_size + 1)
        end_idx = i + 1
        av[i] = np.mean(data[start_idx:end_idx])

    return av

def process_data(filename):
    data = read_data(filename)
    showi(data, 'start.png')
    av = calculate_av(data)
    showi(av, 'result.png')

for i in range(1, 4):
    filename = f'/Users/evelaveta/Desktop/Programming/term4/numpy/2/signals/signal{i:02}.dat'
    process_data(filename)
