#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:16:38 2019

@author: baoshiyuan
"""

import math
from gurobipy import *
from itertools import combinations

# Euclidean distance between two points


def distance(position, i, j):
  dx = position[i][0] - position[j][0]
  dy = position[i][1] - position[j][1]
  return math.sqrt(dx*dx + dy*dy)


m = Model('eulerian graph')


# Create variables
#vars[i,j]=1,edge (i,j) in E or E'
#         =0,otherwise
vars = {}
k={}
for i in range(n):
   for j in range(i+1):
       vars[i,j] = m.addVar(obj=1.0, vtype=GRB.BINARY,
                          name='e'+str(i)+'_'+str(j))
       vars[j,i] = vars[i,j]
       vars[i,i]=0
       k[i]=m.addVar(vtype=GRB.INTEGER,name='k'+str(i))
       m.update()
#variable k is interger variable, 2k is always even

Ad_matrix=np.triu(nx.to_numpy_matrix(G,nodelist=list(range(n))),k=1)
#Add old edges existance constraint
for i in range(len(Ad_matrix)):
    for j in range(len(Ad_matrix)):
        if Ad_matrix[i,j]!=0:#if edge(i,j) in E,vars[i,j]==1
            m.addConstr(vars[i,j]==int(Ad_matrix[i,j]))

#every node has even degree
for i in range(n):
    m.addConstr(quicksum(vars[i,j] for j in range(n)) ==2*k[i])

m.update()

#check every convex qudrangle,
for convex_quadrangle in combinations(position,4):
        (p1,q1,p2,q2)=convex_quadrangle
        if(do_intersect(p1,q1,p2,q2)==True):
#if (p1,q1),(p2,q2) inersect, at most one of these two segments extists
            m.addConstr(vars[position.index(p1),position.index(q1)]+vars[position.index(p2),position.index(q2)]<=1) 
        if(do_intersect(p1,p2,q1,q2)==True):
#if (p1,p2),(q1,q2) inersect, at most one of these two segments extists
            m.addConstr(vars[position.index(p1),position.index(p2)]+vars[position.index(q1),position.index(q2)]<=1) 
        if(do_intersect(p1,q2,p2,q1)==True):
#if (p1,q2),(p2,q1) inersect, at most one of these two segments extists     
            m.addConstr(vars[position.index(p1),position.index(q2)]+vars[position.index(p2),position.index(q1)]<=1)               

#every connected component must connect with the others              
 
for a in range(1,n):
    for combination in combinations(range(n),a):
        for i in combination:
            if j not in combination:
                m.addConstr(quicksum(vars[i,j]for i in combination)>=1)

            
# Optimize model
m._vars = vars
m.optimize()


if m.status == GRB.Status.OPTIMAL:
    feasible=1
elif m.status == GRB.Status.INF_OR_UNBD:
    feasible=0
elif m.status == GRB.Status.INFEASIBLE:
    feasible=0
elif m.status == GRB.Status.UNBOUNDED:
    feasible=0
else:
    feasible=0

