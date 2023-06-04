import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
import subprocess
import csv
import os
from tabulate import tabulate
import random


string_length = [100, 1000, 2000, 5000, 8000, 10000, 20000]
memory_hirshberg = [1015, 1114, 1163, 1474, 1671, 2129, 2244]
memory_naive = [1064, 5144, 17317, 175636, 260489, 496533, 644612]
time_hirshberg = [0.001053, 0.074819, 0.236601, 1.43839, 3.67888, 5.67314, 22.8164]
time_naive = [0.000434, 0.03969, 0.157222, 0.986531, 2.53625, 3.96867, 15.9354]
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

col = 0
axes[col].plot(string_length, memory_hirshberg, label = 'Hirshberg', marker = 'x')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].legend()
y_offset = [10000, 12000, 19000, 10000, 10000, 10000, 10000]
i = 0
for x, y in zip(string_length, memory_hirshberg):
    axes[col].text(x - 200, y + y_offset[i], str(y), color='tab:blue', fontsize=8, ha='left', rotation = 45)
    i += 1

axes[col].plot(string_length, memory_naive, label = 'Naive', marker = 'o')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].legend()
x_offset = [0, 0, 0, -500, -500, -500, -1000]
y_offset = [50000, 50000, 50000, 1000, 1000, 1000, -70000]
i = 0
for x, y in zip(string_length, memory_naive):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:red', fontsize=8, ha='left', rotation = 45)
    i += 1


col = 1
axes[col].plot(string_length, time_hirshberg, label = 'Hirshberg', marker = 'x')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].legend()
i = 0
x_offset = [0, 0, 0, -400, -400, -400, -400]
y_offset = [.4, .4, .4, .3, .3, .1, -2]
time_hirshberg_print = [0.001, 0.074, 0.236, 1.438, 3.678, 5.673, 22.816]
for x, y in zip(string_length, time_hirshberg_print):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:blue', fontsize=8, ha='left', rotation = 45)
    i += 1

pos = 1
axes[col].plot(string_length, time_naive, label = 'Naive', marker = 'o')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].legend()
i = 0
x_offset = [-200, 0, 0, 0, 0, 0, -800]
y_offset = [-1.1, -1.1, -1.1, -1.1, -1.1, -1.1, 0]
time_naive_print = [.0004, .039, 0.157, 0.986, 2.53, 3.968, 15.935]
for x, y in zip(string_length, time_naive_print):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:red', fontsize=8, ha='left', rotation = 20)
    i += 1

plt.savefig('output1.png', bbox_inches='tight')
