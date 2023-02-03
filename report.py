from tabulate import tabulate
from IPython.display import display, Markdown
import matplotlib.pyplot as plt
import numpy as np

headers = ['block size', 'sequential time, s', 'parallel first loop time, s', 'parallel second loop time, s']
display(Markdown('## results'))

file = open('output.txt', 'r')
for line in file:
    size, rows = map(int, line.split())
    title = 'matrix {}x{}'.format(size, size)
    display(Markdown('### {}'.format(title)))
    table = [file.readline().split() for _ in range(rows)]
    display(Markdown(tabulate(table, headers, tablefmt='pipe')))
    
    data = np.array(table)
    labels = ['sequential', 'first parallel', 'second parallel']
    block_sizes = list(map(int, data[:,0]))
    plt.xlabel('Block size')
    plt.ylabel('Elapsed time, seconds')
    plots = []
    for i in range(1, 4):
        plots.append(plt.plot(block_sizes,  list(map(float, data[:,i])), label=labels[i-1])[0])
    plt.legend(handles=plots)
    plt.show()
    

