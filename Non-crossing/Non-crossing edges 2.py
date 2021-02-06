#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:04:58 2019

@author: baoshiyuan
"""

import random
import networkx as nx
import datetime

start=datetime.datetime.now()

G=nx.Graph()
m=7


def orientation(p,q,r):#define orientation of (p,q,r)
    val=((q[1]-p[1])*(r[0]-q[0])-
    (q[0]-p[0])*(r[1]-q[1]))
    if val==0:#p,q,r are colinear
        return 0
    elif val>0:
        return 1#p,q,r are clockwise
    else:
        return 2#p,q,r are counterclockwise

def do_intersect(p1,q1,p2,q2):
    o1=orientation(p1,q1,p2)
    o2=orientation(p1,q1,q2)
    o3=orientation(p2,q2,p1)
    o4=orientation(p2,q2,q1)

#oritations(p1,q1,p2) and (p2,q1,q2)are different,oritations of (p2,q2,p1) and (p2,q2,q1) are also different
    if(o1!=o2 and o3!=o4):
        return True
    return False

edge=[]    
for l in range(n):
    for k in range(1,n):
        if k>l:
            edge.append((l,k))

nc_edge=[() for i in range(m)]

i=0
while i<m:
    nc_edge[i]=random.sample(edge,1)
    G.add_edge(nc_edge[i][0][0],nc_edge[i][0][1])
    edge.remove((nc_edge[i][0][0],nc_edge[i][0][1]))
    for (e1,e2) in edge:
        p1=position[nc_edge[i][0][0]]
        q1=position[nc_edge[i][0][1]]
        p2=position[e1]
        q2=position[e2]
        if e1!=nc_edge[i][0][0] and e2!=nc_edge[i][0][0] and e1!=nc_edge[i][0][1] and e2!=nc_edge[i][0][1]:
            if do_intersect(p1,q1,p2,q2)==True:
                edge.remove((e1,e2))
    i+=1

       
for i in range(n):
    G.add_node(i) 
        

end=datetime.datetime.now()
print(end-start)