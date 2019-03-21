# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:23:20 2019

@author: tuj47049
"""
from __future__ import absolute_import, division, print_function 

import arcpy, sys, os

# System Arguments 'C:/Users/tuj47049/Desktop/Module/module.mxd'

myMap = sys.argv[1]
mxd = arcpy.mapping.MapDocument(myMap)
print(mxd)
print(mxd.author)
mxd.author = "Zach"
print(mxd.author)
print(mxd.dateSaved)
print(mxd.filePath)
