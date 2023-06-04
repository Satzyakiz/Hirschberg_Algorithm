import matplotlib.pyplot as plt
import numpy as np
import sys, getopt
import subprocess
import csv
import os
from tabulate import tabulate


categories = ['dna1\nX\ndna2', 'dna1\nX\ndna1', 'protein1\nX\nprotein2', 'protein1\nX\nprotein1', 'random1\nX\nrandom2', 'random1\nX\nrandom1']
memory_hirshberg = [2064, 1835, 2228, 2113, 2949, 2211]
memory_naive = [73722, 105712, 83632, 88380, 75714, 117778]
time_hirshberg = [33.0361, 33.5587, 31.1133, 30.8536, 30.7029, 30.8025]
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15, 20))

col = 0
x = np.arange(len(memory_hirshberg))
width = 0.1
axes[col].bar(x, memory_hirshberg, width, label = 'Hirshberg')
axes[col].set_title('Memory vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Memory (in MB)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
for i, v in enumerate(memory_hirshberg):
    axes[col].text(i, v + 5, str(v), color='black', fontsize=8, ha='center')
axes[col].legend(loc='upper left', bbox_to_anchor=(0, 1))

col = 1
x = np.arange(len(time_hirshberg))
width = 0.1
axes[col].bar((x - 0.05), time_hirshberg, width, label = 'Hirshberg')
axes[col].set_title('Time vs String Length', fontsize=16)
axes[col].set_xlabel('String Length', fontsize=12)
axes[col].set_ylabel('Time (in sec)', fontsize=12)
axes[col].set_xticks(x)
axes[col].set_xticklabels(categories)
for i, v in enumerate(time_hirshberg):
    axes[col].text(i - 0.15, v + .2, str(v), color='black', fontsize=8, ha='center')
axes[col].legend(loc='upper left', bbox_to_anchor=(0, 1))


plt.savefig('output3.2.png', bbox_inches='tight')