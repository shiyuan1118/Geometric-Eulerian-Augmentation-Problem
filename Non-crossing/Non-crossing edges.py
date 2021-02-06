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
m=30


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
    
edge=[[0 for j in range(2)] for i in range(m)]

i=0
while i<m:
    exist_intersect=False
    edge[i]=random.sample(position,2)  
    for (e1,e2)in edge[0:i]:
        if do_intersect(e1,e2,edge[i][0],edge[i][1])==True:
            exist_intersect=True
            break
        if e1==edge[i][0] and e2==edge[i][1]:
            exist_intersect=True 
            break
        if e1==edge[i][1] and e2==edge[i][0]:
            exist_intersect=True
            break
        else:
            continue
    if exist_intersect==False:
        G.add_edge(position.index(edge[i][0]),position.index(edge[i][1]))
        i+=1

       
for i in range(n):
    G.add_node(i) 
        

end=datetime.datetime.now()
print(end-start)