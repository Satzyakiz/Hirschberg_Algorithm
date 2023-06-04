import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
import subprocess
import csv
import os
from tabulate import tabulate


string_length = [1000, 1000000, 2000000, 5000000, 10000000, 20000000, 50000000, 100000000]
memory_hirshberg = [1179, 10829, 18579, 41910, 106037, 165543, 349126, 647757]
memory_naive = [1146, 82755, 164265, 409075, 797491, 1186611, 1411432, 2096660]
time_hirshberg = [0.009883, 3.63907, 7.26977, 18.1171, 38.7645, 73.6928, 186.984, 376.979]
time_naive = [0.000583, 0.573507, 1.14726, 2.8706, 5.77192, 11.5981, 29.0987, 58.5028]
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

col = 0
axes[col].plot(string_length, memory_hirshberg, label = 'Hirshberg', marker = 'x')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].legend()
x_offset = [-3600000, -2000000, 500000, -100000, 0, 0, 0, -3000000]
y_offset = [-100000, -110000, -100000, 40000, 40000, 40000, 30000, 1000]
i = 0
for x, y in zip(string_length, memory_hirshberg):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:blue', fontsize=8, ha='left', rotation = 20)
    i += 1

axes[col].plot(string_length, memory_naive, label = 'Naive', marker = 'o')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
x_offset = [-2500000, 800000, -3000000, -10000, -50000, -2000000, -2000000, -1000000]
y_offset = [-8000, -5000, -5000, -100000, -100000, -250000, -200000, -150000]
i = 0
for x, y in zip(string_length, memory_naive):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:red', fontsize=8, ha='left', rotation = 45)
    i += 1
axes[col].legend()

col = 1
axes[col].plot(string_length, time_hirshberg, label = 'Hirshberg', marker = 'x')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].legend()
i = 0
x_offset = [-5000000, -4000000, -2500000, -1000000, -1000000, -1000000, -2000000, -2000000]
y_offset = [-10, 8, -2, 5, 7, 5, 5, -25]
time_hirshberg_print = [0.009, 3.639, 7.269, 18.11, 38.764, 73.692, 186.984, 376.979]
for x, y in zip(string_length, time_hirshberg_print):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:blue', fontsize=8, ha='left', rotation = 25)
    i += 1
    
axes[col].plot(string_length, time_naive, label = 'Naive', marker = 'o')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].legend()
i = 0
x_offset = [-5000000, -1800000, 100000, 600000, 700000, 800000, 0, -3000000]
y_offset = [-19, -19, -19, 5, 5, 5, 5, 5]
time_naive_print = [0.0005, 0.57, 1.147, 2.87, 5.771, 11.598, 29.098, 58.502]
for x, y in zip(string_length, time_naive_print):
    axes[col].text(x + x_offset[i], y + y_offset[i], str(y), color='tab:red', fontsize=8, ha='left', rotation = 15)
    i += 1

plt.savefig('output2.png', bbox_inches='tight')
