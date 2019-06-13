#!/usr/bin/env python
# coding: utf-8

# In[11]:


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
stats1=df.loc[1, labels].values
stats2=df.loc[5, labels].values
stats3=df.loc[12, labels].values
stats4=df.loc[15, labels].values
stats5=df.loc[18, labels].values
stats6=df.loc[23, labels].values
#
# close the plot
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
angles=np.concatenate((angles,[angles[0]]))
stats1=np.concatenate((stats1,[stats1[0]]))
stats2=np.concatenate((stats2,[stats2[0]]))
stats3=np.concatenate((stats3,[stats3[0]]))
stats4=np.concatenate((stats4,[stats4[0]]))
stats5=np.concatenate((stats5,[stats5[0]]))
stats6=np.concatenate((stats6,[stats6[0]]))

#  
fig = plt.figure(figsize=(10.0, 5.0), dpi=300)
fig.suptitle('Radar chart for the bathymetry of the Mariana Trench',
            fontsize=12, fontweight='bold', x=0.5, y=0.99)
#
# subplot 1
ax = fig.add_subplot(231, polar=True)
ax.plot(angles, stats1, 'o-', linewidth=2)
ax.fill(angles, stats1, c='g',alpha=0.2)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.title('profile (nr.1)', fontsize=12, fontfamily='sans-serif')
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(True)
ax.annotate('(A)', fontsize=14, xy=(1.02, .90), xycoords="axes fraction")
#
# subplot 2
ax = fig.add_subplot(232, polar=True)
ax.plot(angles, stats2, 'o-', linewidth=2)
ax.fill(angles, stats2, c='#a0d8ef',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.title('profile (nr.5)', fontsize=12, fontfamily='sans-serif')
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(True)
ax.annotate('(D)', fontsize=14, xy=(1.02, .90), xycoords="axes fraction")
#
# subplot 3
ax = fig.add_subplot(233, polar=True)
ax.plot(angles, stats3, 'o-', linewidth=2)
ax.fill(angles, stats3, c='#ee827c',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.title('profile (nr.12)', fontsize=12, fontfamily='sans-serif')
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(True)
ax.annotate('(B)', fontsize=14, xy=(1.02, .90), xycoords="axes fraction")
#
# subplot 4
ax = fig.add_subplot(234, polar=True)
ax.plot(angles, stats4, 'o-', linewidth=2)
ax.fill(angles, stats4, c='plum',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.title('profile (nr.15)', fontsize=12, fontfamily='sans-serif')
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(True)
ax.annotate('(E)', fontsize=14, xy=(1.02, .90), xycoords="axes fraction")
#
# subplot 5
ax = fig.add_subplot(235, polar=True)
ax.plot(angles, stats5, 'o-', linewidth=2)
ax.fill(angles, stats5, c='#ffd900',alpha=0.2)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.title('profile (nr.19)', fontsize=12, fontfamily='sans-serif')
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(True)
ax.annotate('(C)', fontsize=14, xy=(1.02, .90), xycoords="axes fraction")
#
# subplot 6
ax = fig.add_subplot(236, polar=True)
ax.plot(angles, stats6, 'o-', linewidth=2)
ax.fill(angles, stats6, c='#c3d825',alpha=0.4)
ax.set_thetagrids(angles * 180/np.pi, labels)
plt.title('profile 24', fontsize=12, fontfamily='sans-serif')
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(True)
ax.annotate('(F)', fontsize=14, xy=(1.02, .90), xycoords="axes fraction")
#
plt.tight_layout()
fig.savefig('plot_RadarChart.png', dpi=300)
plt.show()


# In[ ]:




