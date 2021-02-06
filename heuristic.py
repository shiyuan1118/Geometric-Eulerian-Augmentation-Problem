#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:52:25 2019

@author: baoshiyuan
"""

from scipy.spatial import ConvexHull
from functools import reduce
import operator
import math
import matplotlib.pyplot as plt
from itertools import combinations
import datetime

start=datetime.datetime.now()

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
    
CH[len(CH)-1]=position_a
while [] in CH:
    CH.remove([])
    

for i in range(len(CH[0])):
    degree=list(nx.degree(G))
    if i<len(CH[0])-1:
        for j in range(n):
            if CH[0][i]==degree[j][0]:
                if degree[j][1]==0 or degree[j][1]%2!=0:
                    G.add_edge(CH[0][i],CH[0][i+1])
                
    degree=list(nx.degree(G))
    if i==len(CH[0])-1:
        for j in range(n):
            if CH[0][i]==degree[j][0]:
                if degree[j][1]==0 or degree[j][1]%2!=0:
                    G.add_edge(CH[0][i],CH[0][0])

i=1
while i<len(CH):
    for j in range(len(CH[i])):
        degree=list(nx.degree(G))
        if j<len(CH[i])-1:
            for k in range(n):
                if CH[i][j]==degree[k][0]:
                    if degree[k][1]==0 or degree[k][1]%2!=0:
                        exist_intersect=False
                        for (a,b) in list(G.edges):
                            if do_intersect(position[a],position[b],position[CH[i][j]],position[CH[i][j+1]])==True:
                                exist_intersect=True
                                break 
                        if exist_intersect==False:
                            G.add_edge(CH[i][j],CH[i][j+1])
                            
        degree=list(nx.degree(G))                        
        if j==len(CH[i])-1:
            for k in range(n):
                if CH[i][j]==degree[k][0]:
                    if degree[k][1]==0 or degree[k][1]%2!=0:
                        exist_intersect=False
                        for (a,b) in list(G.edges):
                            if do_intersect(position[a],position[b],position[CH[i][j]],position[CH[i][0]])==True:
                                exist_intersect=True
                                break  
                        if exist_intersect==False:    
                            G.add_edge(CH[i][j],CH[i][0])
                            
    i+=1
    
    
degree=list(nx.degree(G))  
K=[]

for i in range(n):
    if degree[i][1]==0 or degree[i][1]%2!=0:
        K.append(degree[i][0])

        
for j in K:
    for k in K:
        if j!=k:
            exist_intersect=False
            for (a,b) in list(G.edges):
                if a!=j and b!=k and a!=k and b!=j:
                    if do_intersect(position[a],position[b],position[j],position[k])==True:
                        exist_intersect=True
                        break
                    else:
                        continue
            if exist_intersect==False:
                G.add_edge(j,k)
                

degree=list(nx.degree(G))  
K=[]

for i in range(n):
    if degree[i][1]==0 or degree[i][1]%2!=0:
        K.append(degree[i][0])


L=[i for i in range(n) if i not in K]

def test():
    for i in L:
        for combination in combinations(K,2):
            exist_intersect=False           
            for (a,b) in list(G.edges):
                if a!=combination[0] and b!=i and b!=combination[0] and i!=a:
                    if do_intersect(position[a],position[b],position[combination[0]],position[i])==True:
                        exist_intersect=True
                if a!=combination[1] and b!=i and b!=combination[1] and i!=a:
                    if do_intersect(position[a],position[b],position[combination[1]],position[i])==True:
                        exist_intersect=True
            if exist_intersect==False:
                G.add_edge(i,combination[0])
                G.add_edge(i,combination[1])                
                return
            else:
                continue
test()
            
I=[]
degree=list(nx.degree(G))

for i in range(n):
    if degree[i][1]==0 or degree[i][1]%2!=0:
        I.append(degree[i][0])            
       
if len(I)>0:
    print('infeasible')
if len(I)==0:
    print('feasible')              
                                              

end=datetime.datetime.now()
print(end-start)
                
                
                    
                
                
                    
                


                