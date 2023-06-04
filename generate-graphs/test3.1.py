import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
import subprocess
import csv
import os
from tabulate import tabulate


categories = ['dna1\nX\ndna2', 'dna1\nX\ndna1', 'protein1\nX\nprotein2', 'protein1\nX\nprotein1', 'random1\nX\nrandom2', 'random1\nX\nrandom1']
memory_hirshberg = [2064, 1835, 2228, 2113, 2949, 2211]
memory_naive = [603930, 865992, 685113, 724008, 620249, 964837]
time_hirshberg = [33.0361, 33.5587, 31.1133, 30.8536, 30.7029, 30.8025]
time_naive = [24.4678, 23.0614, 23.4196, 21.4411, 21.7548, 21.42]
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 20))

col = 0
x = np.arange(len(memory_hirshberg))
width = 0.1
axes[col].bar((x - 0.05), memory_hirshberg, width, label = 'Hirshberg')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
for i, v in enumerate(memory_hirshberg):
    axes[col].text(i - 0.15, v + 1000, str(v), color='black', fontsize=8, ha='center')
axes[col].legend()

x = np.arange(len(memory_naive))
width = 0.1
axes[col].bar((x + 0.05), memory_naive, width, label = 'Naive')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
for i, v in enumerate(memory_naive):
    axes[col].text(i + 0.15, v + 1000, str(v), color='black', fontsize=8, ha='center')
axes[col].legend()


col = 1
x = np.arange(len(time_hirshberg))
width = 0.1;
axes[col].bar((x - 0.05), time_hirshberg, width, label = 'Hirshberg')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
for i, v in enumerate(time_hirshberg):
    axes[col].text(i - 0.15, v + .2, str(v), color='black', fontsize=8, ha='center')
axes[col].legend(loc='upper left', bbox_to_anchor=(0, 1))

x = np.arange(len(memory_naive))
width = 0.1;
axes[col].bar((x + 0.05), time_naive, width, label = 'Naive')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
for i, v in enumerate(time_naive):
    axes[col].text(i + 0.15, v + .2, str(v), color='black', fontsize=8, ha='center')
axes[col].legend()

plt.savefig('output3.1.png', bbox_inches='tight')