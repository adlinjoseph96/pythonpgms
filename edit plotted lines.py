# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:07:17 2019

@author: Bindhu Joseph
"""

import matplotlib.pyplot as plt
x=[2,5,8,6,7]
y=[5,8,6,7,2]
plt.plot(x,y,color='green',linestyle='dashed',linewidth=2,marker='o',markerfacecolor="blue",markersize=12)
plt.ylim(1,10)
plt.xlim(1,10)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('edtting')
plt.show()