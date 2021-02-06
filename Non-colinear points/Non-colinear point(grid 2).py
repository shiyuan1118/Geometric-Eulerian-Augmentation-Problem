#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:51:12 2019

@author: baoshiyuan
"""
import numpy as np
import random 
import datetime

start=datetime.datetime.now() 

n=100
grid_size=30
grid = np.dstack(np.meshgrid(np.arange(grid_size), np.arange(grid_size)))

point=[[0 for j in range(2)] for i in range(n)]
position=[[0]for i in range(n)]

i=0
j=0
while i<n:
    x_shape=np.shape(grid)[0]
    y_shape=np.shape(grid)[1]
    x_index=random.sample(range(np.shape(grid)[0]),1)[0]
    y_index=random.sample(range(np.shape(grid)[1]),1)[0]
    point[i]=grid[x_index][y_index]
    x=point[i][0]
    y=point[i][1]   
    for j in range(i):
        x_1=point[j][0]
        y_1=point[j][1]
        if x_1==x:
            grid[~(grid[:,:,0]==x)]
        if y_1==y:
            grid[~(grid[:,:,1]==y)]
        if x_1!=x and y_1!=y:
            delta_x=abs(x-x_1)
            delta_y=abs(y-y_1)
            p=Point(x,y)
            q=Point(x_1,y_1)
            a=getCount(p,q)
            s_x=delta_x/(a+1)
            s_y=delta_y/(a+1)
            b_1=int((grid_size-x_1)/s_x)
            c_1=int((grid_size-y_1)/s_y)
            b_2=int(x_1/s_x)
            c_2=int(y_1/s_y)
            for l in range(min(b_1,c_1)):
                if (x_1+s_x*l in grid[:,:,0])==True and (y_1+s_y*l in grid[:,:,1])==True:
                    grid[~((grid[:,:,0]==x_1+s_x*l) & (grid[:,:,1]==y_1+s_y*l))]
            for k in range(min(b_2,c_2)):
                if (x_1-s_x*k in grid[:,:,0])==True and (y_1-s_y*k in grid[:,:,1])==True:
                    grid[~((grid[:,:,0]==x_1-s_x*k) & (grid[:,:,1]==y_1-s_y*k))]                       
    position[i]=(x,y)
    i+=1
                
end=datetime.datetime.now()
print('Finished in'+str(end-start))