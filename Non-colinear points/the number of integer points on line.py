#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:50:26 2019

@author: baoshiyuan
"""

class Point: 
      
    def __init__(self, a, b): 
        self.x = a 
        self.y = b 
  
def gcd(a, b):   
    if b == 0: 
        return a 
    return gcd(b, a % b) 
  
def getCount(p, q):    
    if p.x == q.x: 
        return abs(p.y - q.y) - 1 
    if p.y == q.y: 
        return abs(p.x - q.x) - 1
  
    return gcd(abs(p.x - q.x),  
               abs(p.y - q.y)) - 1