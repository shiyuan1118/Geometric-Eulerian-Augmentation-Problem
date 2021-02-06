#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:39:56 2019

@author: baoshiyuan
"""

import numpy as np
import networkx as nx
from gurobipy import *
import math
import datetime
from itertools import combinations
import operator
from functools import reduce
import matplotlib.pyplot as plt

start=datetime.datetime.now()

Ad_matrix=np.triu(nx.to_numpy_matrix(G,nodelist=list(range(n))),k=1)
    
class Graph: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 

#add edges in Graph
g=Graph(n)
for i in range(n):
    for j in range(n):
        if Ad_matrix[i,j]!=0:
            g.addEdge(i,j)  

#print connected components            
cc=g.connectedComponents()   
      
def distance(position, i, j):
    dx = position[i][0] - position[j][0]
    dy = position[i][1] - position[j][1]
    return math.sqrt(dx*dx + dy*dy)

m = Model('eulerian graph')
    
vars = {}
k={}
    
for i in range(n):
    for j in range(i+1):
        vars[i,j] = m.addVar(obj=distance(position,i,j), vtype=GRB.CONTINUOUS,
                              name='e'+str(i)+'_'+str(j))
        vars[j,i] = vars[i,j]
        vars[i,i]=0
        k[i]=m.addVar(vtype=GRB.CONTINUOUS,name='k'+str(i))
        m.addConstr(0<=vars[i,j]<=1)
        m.addConstr(0<=k[i])

for (e1,e2) in nc_edge:
    i=position.index(e1)
    j=position.index(e2)
    m.addConstr(vars[i,j]==1)
    
for (e1,e2) in c_edge:
    i=position.index(e1)
    j=position.index(e2)
    m.addConstr(vars[i,j]==0)
    
for i in range(len(edge)):
    (e1,e2)=edge[i]
    for (e3,e4) in edge[i+1:len(edge)]:
        if e1!=e3 and e1!=e4 and e2!=e3 and e2!=e4:
            if do_intersect(e1,e2,e3,e4)==True:
                m.addConstr(vars[position.index(e1),position.index(e2)]+vars[position.index(e3),position.index(e4)]<=1)
    for (e5,e6) in nc_edge:
        if e1!=e5 and e1!=e6 and e2!=e5 and e2!=e6:
            if do_intersect(e1,e2,e5,e6)==True:
                m.addConstr(vars[position.index(e1),position.index(e2)]+vars[position.index(e5),position.index(e6)]<=1)      
for i in range(n):
    m.addConstr(quicksum(vars[i,j] for j in range(n)) ==2*k[i])    
    
if len(cc)>1:
    for a in range(1,len(cc)):
        for combination in combinations(cc,a):
            combination_1=reduce(operator.add,combination)
            not_in=[i for i in range(n) if i not in combination_1]
            m.addConstr(quicksum(vars[i,j]for i in combination_1 for j in not_in)>=1)
            
m._vars = vars
m.optimize()

end=datetime.datetime.now()
print(end-start) 

nx.draw_networkx(G, pos=position,with_labels=True)
plt.show() 