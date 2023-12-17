#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:28:12 2023

@author: mohamed
"""
from glob import glob
image_folder = glob("/home/mohamed/Desktop/exercise1/dataset/*/", recursive = True)


import json

def add_image_path(path):
    with open(path + "via_region_data.json", "r") as jsonFile:
        data = json.load(jsonFile)

    for d in data:
        data[d]['image_path'] = path + d

    with open(path +"path_via_region_data.json", "w") as jsonFile:
        json.dump(data, jsonFile)
        
        
for folder in image_folder:
    add_image_path(folder)
    
    
    

    
    
