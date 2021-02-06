#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:55:55 2019

@author: baoshiyuan
"""

import datetime
import random
import numpy as np
import math

start=datetime.datetime.now()
###the number of nodes that we generate
n=5
grid_size=10
grid=np.zeros((grid_size,grid_size), dtype=int)
                           
point=[[0 for j in range(2)] for i in range(n)]
position=[[0]for i in range(n)]

all_point=[]
for i in range(grid_size):
    for j in range(grid_size):
        all_point.append((i,j))
        
i=0
j=0
while i<n:
    point[i]=random.sample(all_point,1)
    x=point[i][0][0]
    y=point[i][0][1]    
    all_point.remove((x,y))
    grid[x,y]=1
    for j in range(i):
        x_1=point[j][0][0]
        y_1=point[j][0][1]
        if x_1==x:
            for i in range(grid_size):
                if grid[x,i]==0:
                    all_point.remove((x,i))
            grid[x]=-1
        if y_1==y:
            for i in range(grid_size):
                if grid[i,y]==0:
                    all_point.remove((i,y))
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
                    if grid[x_1+s_x*l_1,y_1+s_y*l_1]==0:
                        all_point.remove((x_1+s_x*l_1,y_1+s_y*l_1))
                    grid[x_1+s_x*l_1,y_1+s_y*l_1]=-1
                for k_1 in range(min(b_2,c_2)):
                    if grid[x_1-s_x*k_1,y_1-s_y*k_1]==0:
                        all_point.remove((x_1-s_x*k_1,y_1-s_y*k_1))
                    grid[x_1-s_x*k_1,y_1-s_y*k_1]=-1    
            if delta_x*delta_y<0:
                b_3=int((grid_size-1-x_1)/s_x)
                c_3=int(y_1/s_y)
                b_4=int(x_1/s_x)
                c_4=int((grid_size-1-y_1)/s_y)
                for l_2 in range(min(b_3,c_3)):
                    if grid[x_1+s_x*l_2,y_1-s_y*l_2]==0:
                        all_point.remove((x_1+s_x*l_2,y_1-s_y*l_2))
                    grid[x_1+s_x*l_2,y_1-s_y*l_2]=-1
                for k_2 in range(min(b_4,c_4)):
                    if grid[x_1-s_x*k_2,y_1+s_y*k_2]==0:
                        all_point.remove((x_1-s_x*k_2,y_1+s_y*k_2))
                    grid[x_1-s_x*k_2,y_1+s_y*k_2]=-1    
            grid[x_1,y_1]=1
    grid[x,y]=1
    position[i]=(x,y)
    i+=1
                
end=datetime.datetime.now()
print('Finished in'+str(end-start))
