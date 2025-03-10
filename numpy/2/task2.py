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
    cumsum = np.cumsum(data)
    av = np.zeros_like(data)

    av[:window_size] = cumsum[:window_size] / np.arange(1, window_size + 1)
    av[window_size:] = (cumsum[window_size:] - cumsum[:-window_size]) / window_size
    return av

def process_data(filename, i):
    data = read_data(filename)
    showi(data, f'start{i:02}.png')
    av = calculate_av(data)
    showi(av, f'result{i:02}.png')

for i in range(1, 4):
    filename = f'/Users/evelaveta/Desktop/Programming/term4/numpy/2/signals/signal{i:02}.dat'
    process_data(filename, i)
