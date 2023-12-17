#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:01:11 2023

@author: mohamed
"""
import json

with open('data.json') as f:
    d = json.load(f)
    
    
    
new_json = []    
for i in range(len(d)):
    for j in d[i]:
        new_json.append(d[i][j]['image_path'])
        new_json.append(d[i][j]['regions'])
        
        
def Convert(lst):
	res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
	return res_dct
		
# Driver code
new_json = Convert(new_json)

for j in new_json:
    for i in range(len(new_json[j])):
        del new_json[j][i]['shape_attributes']


with open('data.json', 'w') as fp:
    json.dump(new_json, fp)
    
    
new_json = {}
labels = []   

for j in d:       
    d[j] = [x['region_attributes']['identity'] for x in d[j]]
        
        
with open('data.json', 'w') as fp:
    json.dump(d, fp)