#!/usr/bin/env python
# coding: utf-8
#
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import seaborn as sns
import numpy as np
import os
#
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
#
# show 6 different variables on our radar chart, so take them out and set as a np.array.
labels=np.array(['Median', 'Max', '1stQ', '3rdQ', 'Min', 'Mean'])
stats=df.loc[1, labels].values
#
# close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
#
# plotting
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, c='g',alpha=0.2)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.title('Radar chart for the Mariana Trench \nStatistics on bathymetric profile (nr.1)', 
          fontsize=12, fontfamily='sans-serif')
ax.grid(True)
ax.annotate('(A)', fontsize=18, xy=(1.02, .90), xycoords="axes fraction")
plt.show()
#
# show 6 different variables on our radar chart, so take them out and set as a np.array.
stats=df.loc[5, labels].values
#
# close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
#
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, c='#a0d8ef',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.title('Radar chart for the Mariana Trench \nStatistics on bathymetric profile (nr.5)', 
          fontsize=12, fontfamily='sans-serif')
ax.grid(True)
ax.annotate('(D)', fontsize=18, xy=(1.02, .90), xycoords="axes fraction")
plt.show()
#
# show 6 different variables on our radar chart, so take them out and set as a np.array.
stats=df.loc[12, labels].values
#
# close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
#
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, c='#ee827c',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.title('Radar chart for the Mariana Trench \nStatistics on bathymetric profile (nr.12)', 
          fontsize=12, fontfamily='sans-serif')
ax.grid(True)
ax.annotate('(B)', fontsize=18, xy=(1.02, .90), xycoords="axes fraction")
plt.show()
#
# Show 6 different variables on our radar chart, so take them out and set as a np.array.
stats=df.loc[15, labels].values
#
# Step-3. close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
#
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, c='plum',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.title('Radar chart for the Mariana Trench \nStatistics on bathymetric profile (nr.15)', 
          fontsize=12, fontfamily='sans-serif')
ax.grid(True)
ax.annotate('(E)', fontsize=18, xy=(1.02, .90), xycoords="axes fraction")
plt.show()
#
# show 6 different variables on radar chart: take them out and set as a np.array.
stats=df.loc[18, labels].values
#
# close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
#
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, c='#ffd900',alpha=0.2)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.title('Radar chart for the Mariana Trench \nStatistics on bathymetric profile (nr.19)', 
          fontsize=12, fontfamily='sans-serif')
ax.grid(True)
ax.annotate('(C)', fontsize=18, xy=(1.02, .90), xycoords="axes fraction")
plt.show()
#
# show 6 different variables on radar chart: take them out and set as a np.array.
stats=df.loc[23, labels].values
#
# close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))
#
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, c='#c3d825',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.title('Radar chart for the Mariana Trench \nStatistics on bathymetric profile (nr.24)', 
          fontsize=12, fontfamily='sans-serif')
ax.grid(True)
ax.annotate('(F)', fontsize=18, xy=(1.02, .90), xycoords="axes fraction")
plt.show()
