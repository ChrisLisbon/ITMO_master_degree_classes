# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:19:58 2020

@author: Julia
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def fill_gaps_linear(input_array, nodata, window_size=2):
    x_train=[]
    y_train=[]
    output_array = np.copy(input_array)
    
    for i in range(window_size, len(output_array)):
        go_next=False
        skip_gap=False

        while not go_next:
            sample_predictors=[]
            for j in range(window_size):
                if output_array[i-j-1]!=nodata:
                    sample_predictors.append(output_array[i-j-1])
                else:
                    go_next=True
                    skip_gap=True
                    pass

            if output_array[i]!=nodata and skip_gap==False:
                y_train.append(output_array[i])                 
                x_train.append(sample_predictors)
                while len(y_train)>window_size:
                    del y_train[0]
                    del x_train[0]
                go_next=True

            if len(x_train)>1:
                if output_array[i]==nodata and skip_gap==False:
                    regr = linear_model.LinearRegression()
                    regr.fit(x_train, y_train)
                    y_pred = regr.predict([sample_predictors])                    
                    output_array[i]=y_pred[0]
            else:
                go_next=True           
    return output_array

def fill_gaps_poly(input_array, nodata, poly_window_size=5):
    gap_indices=[]
    output_array = np.copy(input_array)
    for i in range(len(input_array)):
        if output_array[i]==nodata:
            gap_indices.append(i)
        else:                
            if len(gap_indices)!=0:
                try:
                    subarray=output_array[gap_indices[0]-poly_window_size:gap_indices[-1]+poly_window_size+1]
                    subarray_ind=np.arange(gap_indices[0]-poly_window_size, gap_indices[-1]+poly_window_size+1)
                    inds=np.where(subarray==nodata)
                    subarray = np.delete(subarray, inds)
                    subarray_ind = np.delete(subarray_ind, inds)
                    z = np.polyfit(subarray_ind, subarray, 6)
                    p = np.poly1d(z)
                    for gap in gap_indices:
                        output_array[gap]=p(gap)
                except Exception as e:
                    print(e)
                    pass                
                gap_indices=[]
    return output_array

def fill_gaps_hybrid(input_array, nodata, lin_window_size=3, poly_window_size=5):
    gap_indices=[]
    output_array = np.copy(input_array)
    for i in range(len(output_array)):
        if output_array[i]==nodata:
            gap_indices.append(i)
        else:
            if len(gap_indices)<4 and len(gap_indices)!=0:
                subarray=output_array[gap_indices[0]-lin_window_size-2:gap_indices[-1]+1]
                filled_subarray=fill_gaps_linear(subarray, nodata, window_size=lin_window_size)
                output_array[gap_indices[0]-lin_window_size-2:gap_indices[-1]+1]=filled_subarray
                gap_indices=[]
    
    for i in range(len(output_array)):
        if output_array[i]==nodata:
            gap_indices.append(i)
        else:                
            if len(gap_indices)>=4 and len(gap_indices)!=0:
                try:
                    subarray=output_array[gap_indices[0]-poly_window_size:gap_indices[-1]+poly_window_size+1]
                    subarray_ind=np.arange(gap_indices[0]-poly_window_size, gap_indices[-1]+poly_window_size+1)
                    inds=np.where(subarray==nodata)
                    subarray = np.delete(subarray, inds)
                    subarray_ind = np.delete(subarray_ind, inds)
                    z = np.polyfit(subarray_ind, subarray, 4)
                    p = np.poly1d(z)
                    for gap in gap_indices:
                        output_array[gap]=p(gap)
                except Exception as e:
                    print(e)
                    pass    
                gap_indices=[]
    return output_array