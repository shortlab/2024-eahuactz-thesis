# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 01:45:13 2024

@author: emili
"""

import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as patches

df = pd.read_excel('damagedepth.xlsx')
xval = df['Depth (um)']
ydam = df['dpa']
yion = df['Ions']

fig, ax1 = plt.subplots()


plt.xticks()
plt.yticks()
plt.grid(True, linestyle=':', linewidth=0.5, color='gray')
plt.title('DPA and W-ion deposition vs depth in W-3%Ta')

plt.xlim(0,1.75)

ax1.plot(xval, ydam, 'g-')
ax1.set_xlabel('Depth (um)')
ax1.set_ylabel('DPA', color='g')

ax1.axvline(x=1.12, color='r', linestyle='--')
ax1.fill_betweenx(ax1.get_ylim(), 0, 1.12, facecolor='gray', alpha=0.22)

ax2 = ax1.twinx()
ax2.plot(xval, yion, 'b-')
ax2.set_ylabel('Deposited W-ions', color='b')

plt.savefig('damageplusionvdepthv2.png', dpi=300, bbox_inches = 'tight')
plt.show()