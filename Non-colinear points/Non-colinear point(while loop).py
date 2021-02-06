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
n=100

def orientation(p,q,r):#define orientation of (p,q,r)
    val=((q[1]-p[1])*(r[0]-q[0])-
    (q[0]-p[0])*(r[1]-q[1]))
    if val==0:#p,q,r are colinear
        return 0
    
position=[(0,0) for i in range(n)] 

G=nx.Graph()

i=0
while i<n:
    exist_colinear=False
    position[i]=tuple(random.sample(range(-100,100),2))
    for p1 in position[0:i]:
        for p2 in position[0:i]:
            if p1!=p2 and p1!=position[i] and p2!=position[i]:
                if orientation(p1,p2,position[i])==0:
                    exist_colinear=True
                    break
                else:
                    continue
    if exist_colinear==False:
        G.add_node(i)
        i+=1
        

end=datetime.datetime.now()
print(end-start)