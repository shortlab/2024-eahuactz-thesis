# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 00:04:13 2024

@author: emili
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_path = 'ResultsSheet.xlsx'

# Read Excel file into a dictionary of DataFrames
dfs = pd.read_excel(excel_file_path, sheet_name=None)

# Access each DataFrame using the sheet names
df_pureW = dfs['pureW']
df_W3Ta = dfs['w3%Ta']
df_W6Ta = dfs['w6%Ta']
df_W11Ta = dfs['w11%Ta']

#create scatter plot
fig = plt.figure()
plt.xticks()
plt.yticks()

plt.plot(df_pureW['DPA'], df_pureW['Thermal Diffusivity [m^2s^-1]'],   label='Pure W')
plt.plot(df_W3Ta['DPA'], df_W3Ta['Thermal Diffusivity [m^2s^-1]'],   label='W 3%wtTa')
plt.plot(df_W6Ta['DPA'], df_W6Ta['Thermal Diffusivity [m^2s^-1]'],   label='W 6%wtTa')
plt.plot(df_W11Ta['DPA'], df_W11Ta['Thermal Diffusivity [m^2s^-1]'],  label='W 11%wtTa')

plt.grid(True, linestyle=':', linewidth=0.5, color='gray')

#show plot

plt.xlim(-0.05,1.0)

plt.xlabel('DPA')
plt.ylabel('Thermal Diffusivity [m^2s^-1]')
plt.legend()

plt.title("Thermal diffusivity vs DPA in self-ion irradiated tungsten-tantalum alloys", y=10.5e-1)

plt.savefig('tungstenirradiationAll.png', dpi=300)
plt.show()

