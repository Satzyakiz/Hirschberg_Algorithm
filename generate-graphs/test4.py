import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
import subprocess
import csv
import os
from tabulate import tabulate


categories = ['unary-1\nX\nunary-1', 'unary-1\nX\nunary-0']
memory_hirshberg = [2539, 2441]
time_hirshberg = [138.483, 141.189]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

col = 0
x = np.arange(len(memory_hirshberg))
width = .5
axes[col].bar(x, memory_hirshberg, width, label = 'Hirshberg')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
axes[col].set_xlim(-1, 2)
for i, v in enumerate(memory_hirshberg):
    axes[col].text(i, v + 5, str(v), color='black', fontsize=8, ha='center')

col = 1
x = np.arange(len(time_hirshberg))
width = 0.5
axes[col].bar((x - 0.05), time_hirshberg, width, label = 'Hirshberg')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
axes[col].set_xlim(-1, 2)
offset = [.0, -.1]
index = 0
for i, v in enumerate(time_hirshberg):
    axes[col].text(i + offset[index], v + 2, str(v), color='black', fontsize=8, ha='center')
    index += 1


plt.savefig('output4.png', bbox_inches='tight')