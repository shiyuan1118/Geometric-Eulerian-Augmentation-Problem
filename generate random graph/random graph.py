#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on The Dec 10 10:34:35 2019

@author: baoshiyuan
"""

import datetime
import random
import numpy as np
import math
import networkx as nx
import matplotlib.pyplot as plt


start=datetime.datetime.now()

n=10#the numer of vertsx#
m=5#the numer of initial edges#
grid_size=10#set the grid range to get no-3-colinear points

grid=np.zeros((grid_size,grid_size), dtype=int)
                             
point=[[0 for j in range(2)] for i in range(n)]
position=[[0]for i in range(n)]

#generate n random no-3-colinear-points in a grid#
i=0
j=0
while i<n:
    point[i]=random.sample(list(np.argwhere(grid==0)),1)
    x=point[i][0][0]
    y=point[i][0][1]    
    for j in range(i):
        x_1=point[j][0][0]
        y_1=point[j][0][1]
        if x_1==x:
            grid[x]=-1
        if y_1==y:
            grid[:,y]=-1
        if x_1!=x and y_1!=y:
            delta_x=x-x_1
            delta_y=y-y_1
            a=math.gcd(abs(delta_x),abs(delta_y))
            s_x=int(abs(delta_x)/a)
            s_y=int(abs(delta_y)/a)
            if delta_x*delta_y>0:
                b_1=int((grid_size-1-x_1)/s_x)
                c_1=int((grid_size-1-y_1)/s_y)
                b_2=int(x_1/s_x)
                c_2=int(y_1/s_y)
                for l_1 in range(min(b_1,c_1)):
                    grid[x_1+s_x*l_1,y_1+s_y*l_1]=-1
                for k_1 in range(min(b_2,c_2)):
                    grid[x_1-s_x*k_1,y_1-s_y*k_1]=-1    
            if delta_x*delta_y<0:
                b_3=int((grid_size-1-x_1)/s_x)
                c_3=int(y_1/s_y)
                b_4=int(x_1/s_x)
                c_4=int((grid_size-1-y_1)/s_y)
                for l_2 in range(min(b_3,c_3)):
                    grid[x_1+s_x*l_2,y_1-s_y*l_2]=-1
                for k_2 in range(min(b_4,c_4)):
                    grid[x_1-s_x*k_2,y_1+s_y*k_2]=-1
        grid[x_1,y_1]=1
        
    grid[x,y]=1    
    position[i]=(x,y)
    i+=1

G=nx.Graph()

#check if two segments are intersected#    
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

#get all edges of a complete graph#    
edge=[]    
for l in range(n):
    for k in range(1,n):
        if k>l:
            edge.append([position[l],position[k]])

#generate m non-crossing edges#           
nc_edge=[0 for i in range(m)]#the list of m non-crossing edges#
c_edge=[]#the list of all crossing edges#
i=0
while i<m:
    exist_intersect=False
    nc_edge[i]=random.sample(edge,1)[0]
    for [e1,e2] in nc_edge[0:i]:
        if e1!=nc_edge[i][0] and e1!=nc_edge[i][1] and e2!=nc_edge[i][0] and e2!=nc_edge[i][1]:
            if do_intersect(e1,e2,nc_edge[i][0],nc_edge[i][1])==True:
                exist_intersect=True
                break
        else:
            continue
    if exist_intersect==False:
        G.add_edge(position.index(nc_edge[i][0]),position.index(nc_edge[i][1]))
        edge.remove(nc_edge[i])
        for [e1,e2] in edge:
            if e1!=nc_edge[i][0] and e1!=nc_edge[i][1] and e2!=nc_edge[i][0] and e2!=nc_edge[i][1]:
                if do_intersect(e1,e2,nc_edge[i][0],nc_edge[i][1])==True:
                    edge.remove([e1,e2])
                    c_edge.append([e1,e2])           
        i+=1
              

for i in range(n):
    G.add_node(i)
    
end=datetime.datetime.now()
print(end-start)

nx.draw_networkx(G, pos=position,with_labels=True)
plt.show()   