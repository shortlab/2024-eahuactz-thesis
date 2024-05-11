# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:34:40 2024

@author: emili
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file
df = pd.read_excel('beforeafter.xlsx', index_col=0)

# Extract data for plotting
before_values = df.iloc[0]
before_errors = df.iloc[1]
after_values = df.iloc[2]
after_errors = df.iloc[3]

# Set the positions for the bars
bar_width = 0.3
x = np.arange(len(before_values))

# Plotting
plt.figure(figsize=(7, 4.5))

# Plotting bars with error bars
plt.bar(x - bar_width/2, before_values, width=bar_width, yerr=before_errors, label='0 dpa', alpha=0.7, capsize=5, color='b')
plt.bar(x + bar_width/2, after_values, width=bar_width, yerr=after_errors, label='0.9-1 dpa', alpha=0.7, capsize=5, color='r')

# Adding labels and title
#plt.xlabel('Items')
plt.ylabel('Thermal Diffusivity (10^-5 m^2/s ')
plt.title('Initial thermal diffusivity and thermal diffusivity averaged over 0.9-1 dpa')
plt.xticks(x, before_values.index)
plt.legend()

# Show plot
plt.tight_layout()
plt.savefig('beforeandafter.png', dpi=300)
plt.show()