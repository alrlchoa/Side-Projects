# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 15:15:45 2016

@author: Arnold Choa
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import matplotlib.animation as animation
import math
import time
import itertools as iter

def bubbleSort(arr):
    """ Sort array by bubble sort
    arr is an array of numbers
    """
    result = arr[:]
    unsorted_len = len(arr)
    
    while unsorted_len > 1:
        for i in range(0,unsorted_len-1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
        
        unsorted_len -= 1
    
    return result

def insertSort(arr):
    """ Sort array by insert sort
    arr is an array of numbers
    """
    
    result = []
    
    for x in arr:
        count = len(result)
        i = 0
        
        while i < count:
            if result[i] > x:
                result = result[:(i)] + [x] + result [(i):]
                break
            
            i += 1
            
        if i == count:
            result = result + [x]
    
    return result

def mergeSort(arr):
    """ Sort array by merge sort
    arr is an array of numbers
    """
    
    def mergeArr(a,b):
        """ Sort and merge two arrays
        """
        
        result = []
        
        while len(a) > 0 and len(b) > 0:
            if a[0] > b[0]:
                result = result + [b[0]]
                b = b[1:]
            else:
                result = result + [a[0]]
                a = a[1:]
        
        return result + a + b
    
    def helper(arr):
        """ Helper function for recursion
        """
        if len(arr) == 1:
            return arr[0]
        else:
            temp = []
            for i in range(0,len(arr)-1,2):
                a = arr[i]
                b = arr[i+1]
                temp = temp + [mergeArr(a,b)]
            return helper(temp)
    
    temp = [[x] for x in arr]
    
    return helper(temp)

def quickSort(arr):
    """ Sort array by quick sort
    arr is an array of numbers
    """
    
    def pivot (arr, i):
        """ Make 2 arrays, less than, more than or equal 
        arr is an array of numbers
        i is the index of pivot
        Return less, crit, and more array
        """
        crit = arr[i]
        del arr[i]
        less = []
        more = []
        
        for x in arr:
            if x < crit:
                less.append(x)
            else:
                more.append(x)
        
        return less, [crit], more
    
    def helper(arr):
        """ Helper function for recursion
        arr is array
        Return sorted array or recur
        """
        if len(arr) == 0:
            return arr
        else:
            l , e , m = pivot(arr,0)
            return (helper(l) + e + helper(m))

    return helper(arr)

def heapSort(arr):
    """ Sort array by heap sort
    arr is an array of numbers
    """
    
    result = arr[:]
    def swap (i, j):
        """ Swaps ith and jth element of arr, len(arr) > i , j
        i and j are whole numbers
        arr is the array
        Void
        """
        
        result[i], result[j] = result[j], result[i]
        
    def maxHeap(en, i):
        """ Make max heap
        arr is array
        Return tree heap
        """
        while i*2 + 1 < en:
            l = 2*i + 1
            r = 2*i + 2
            
            if r < end:
                if result[l] < result[r]:
                    great = r
                else:
                    great = l
            else:
                great = l
                
            if result[i] < result[great]:
                swap(i,great)
            i = great
                    
    
    end = len(arr)
    
    #build heap
    for x in range(end//2,-1,-1):
        maxHeap(end,x)
    #sort heap
    while end > 0:
        maxHeap(end,  0 )
        swap(0,end-1)
        end -= 1
    
    return result

def shellSort(arr):
    """ Make shell heap
        arr is array
        Return sorted list
        """
    
    result = arr[:]
    
    k = 1
    gap = 2*(len(arr)//(2**(k +1))) + 1
    
    while gap > 1:
        gap = 2*(len(arr)//(2**(k +1))) + 1
        for i in range(0, gap, 1):
            temp = result[i::gap]
            insertSort(temp)
            
            for j in range(0,len(temp),1):
                result[j*gap + i] = temp[j]
        
        k +=1
                
    return insertSort(result)






test = [2,3,32,5,2,3,4,6,3,32,5,2,3,4,6,3,32,5,2,3,4,6,3,32,5,2,3,4,6,3,32,5,2,3,4,6]