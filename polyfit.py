#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:25:39 2019

@author: baoshiyua
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

x=[0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0,
   0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
y=[1.0,1.0,1.0,0.8,0.75,0.7,0.65,0.3,0.25,0.05,0.05,0,0,0,0,
   1.0,1.0,0.95,0.95,0.8,0.75,0.8,0.35,0.35,0.15,0,0,0,0,0,
   1.0,1.0,1.0,1.0,0.85,0.9,0.75,0.5,0.5,0.3,0.15,0,0,0,0,
   1.0,1.0,1.0,1.0,0.95,0.75,0.85,0.75,0.65,0.4,0.2,0.05,0,0,0,
   1.0,1.0,0.95,0.9,0.9,0.85,0.7,0.75,0.5,0.35,0.15,0.05,0,0,0,
   1.0,1.0,1.0,0.9,0.95,0.85,0.75,0.8,0.4,0.35,0.1,0.1,0,0,0,
   1.0,1.0,1.0,0.95,0.9,0.95,0.85,0.8,0.45,0.5,0.15,0.1,0,0,0,
   1.0,1.0,1.0,0.95,0.9,0.85,0.95,0.65,0.45,0.5,0.15,0.1,0,0,0]

def func(x,a,b):
    return 0.5-(1/math.pi)*np.arctan(a*x+b)

x=np.array(x)
y=np.array(y)

popt,pcov=curve_fit(func,x,y)
a=popt[0]
b=popt[1]
yval=np.vectorize(func(x,a,b))


plot1=plt.plot(x,y,'s',color='grey',label='original values')
plot2=plt.plot(x,yval,'r',color='black',label='polyfit values')
plt.xlabel('the number of initial edges')
plt.ylabel('average probability')
plt.legend(loc=3)
plt.show()

