#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:55:27 2019

@author: baoshiyuan
"""

from scipy.spatial import ConvexHull
from functools import reduce
import operator
import math

CH=[[]for i in range(n)]
j=0
position_a=position
while j<n:
    if len(position_a)>2:
        hull=ConvexHull(position_a)
        hull=hull.simplices
        hull_point=list(set(list(hull.flatten())))
    
        hull_position=[]
        for i in range(len(hull_point)):
            hull_position.append(position_a[hull_point[i]])
        
        coords = hull_position
        center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
        hull_position_1=sorted(coords, key=lambda coord: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)
    
        hull_position_2=[]
        for i in range(len(hull_position_1)):
            hull_position_2.append(position.index(hull_position_1[i]))
        CH[j]=hull_position_2  
        
    position_a=[i for i in position_a if i not in hull_position]        
    j+=1

while [] in CH:
    CH.remove([])

    
nx.draw_networkx(G, pos=position,with_labels=True)
plt.show()     
     
    
    