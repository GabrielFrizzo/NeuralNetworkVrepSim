#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:46:04 2019

@author: frizzo
"""

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def get():
    data = [
            ([   0,    0,    0,    0,    0], [ 5, 5]),
            ([   0, 2000, 1500,    0,    0], [ 5, 4]),
            ([   0,    0,    0, 1500, 2000], [ 4, 5]),
            ([   0,    0, 2000, 2000,    0], [ 5,-2]),
            ([   3, 1500, 2000, 2000, 1500], [ 5,-2]),
            ([  -5, 1500, 1700, 1800, 1500], [ 5,-2]),
            ([  30, 1500, 1700, 1800, 1500], [ 5,-2]),
            ([ -30, 1500, 1700, 1800, 1500], [ 5,-2]),
            ([ 180,    0,    0,    0,    0], [-5, 5]),
            ([-180,    0,    0,    0,    0], [ 5,-5]),
            ([  90,    0,    0,    0,    0], [-2, 5]),
            ([ -90,    0,    0,    0,    0], [ 5,-2]),
            ([ -85,    1,    3,    2,    9], [ 5,-2]),
            ([ -90,    0,    0, 1500, 1500], [ 3, 5]),
            ([  90, 1500, 1500,    0,    0], [ 5, 3]),
            ([   5,    7,    8,    3,   12], [ 5, 5]),
            ([  45, 1500, 1500,    0,    0], [ 5, 3]),
            ([   0, 1500, 1500,    0,    0], [ 5, 3]),
            ([ -45,    0,    0, 1500, 1500], [ 3, 5]),
            ([   0,    0,    0, 1500, 1500], [ 3, 5]),
            ([   0,    0,    0,    0,    0], [ 5, 5]),
            ([   0, 1750, 1500,    0,    0], [ 5, 4]),
            ([   0,    0,    0, 1500, 1750], [ 4, 5]),
            ([   0,    0, 1750, 1750,    0], [ 5,-2]),
            ([   3, 1500, 1750, 1750, 1500], [ 5,-2]),
            ([  -5, 1500, 1500, 1800, 1500], [ 5,-2]),
            ([  30, 1500, 1500, 1800, 1500], [ 5,-2]),
            ([ -30, 1500, 1500, 1800, 1500], [ 5,-2]),
            ([ 180,    0,    0,    0,    0], [-5, 5]),
            ([-180,    0,    0,    0,    0], [ 5,-5]),
            ([  90,    0,    0,    0,    0], [-2, 5]),
            ([ -90,    0,    0,    0,    0], [ 5,-2]),
            ([ -85,    1,    3,    2,    9], [ 5,-2]),
            ([ -90,    0,    0, 1500, 1500], [ 3, 5]),
            ([  90, 1500, 1500,    0,    0], [ 5, 3]),
            ([   5,    7,    8,    3,   12], [ 5, 5]),
            ([  45, 1500, 1500,    0,    0], [ 5, 3]),
            ([   0, 1500, 1500,    0,    0], [ 5, 3]),
            ([ -45,    0,    0, 1500, 1500], [ 3, 5]),
            ([   0,    0,    0, 1500, 1500], [ 3, 5]),
            
    ]
    
    X = [item[0] for item in data]
    y = [item[1] for item in data]
    
    #xscaler = MinMaxScaler(feature_range=(0,1))
    xscaler = StandardScaler()
    xscaler.fit(X)
    X = xscaler.transform(X)
    
    #yscaler = MinMaxScaler(feature_range=(-1,1))
    #yscaler.fit(y)
    #y = yscaler.transform(y)
    print('AAA')
    print(X)
    print(y)
    clf = MLPRegressor(activation='relu',
                       hidden_layer_sizes=(100,),
                       max_iter = 1000,
                       random_state=9)
    clf.fit(X,y)
    
    return clf, xscaler