#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:11:30 2023

@author: mohamed
"""
import json

with open('data.json') as f:
    d = json.load(f)      
        
value_mapping = {
  "lefttailgate": "rear",
  "fuelcapmissing": "rear",
  "leftfender": "front left",
  "bumpertorn": "front",
  "partial_frontws": "front",
  "partial_rightfender": "front right",
  "rightcpillar": "rear right",
  "leftfrontdoorcladding": "front left",
  "rightbootlamp": "rear right",
  "leftreardoorglass": "rear left",
  "rightapillar": "front right",
  "rightqpanel": "rear right",
  "bumperbroken": "front",
  "rightreardoorcladding": "rear right",
  "leftheadlamp": "front left",
  "rearbumpermissing": "rear",
  "leftcabcorner": "front left",
  "rightorvmmissing": "front right",
  "leftcpillar": "front left",
  "leftreardoorcladding": "rear left",
  "leftqpanel": "front left",
  "lowerbumpergrille": "front",
  "leftfoglampassemblymissing": "front left",
  "leftreardoorcladdingmissing": "rear left",
  "rearbumpercladding": "rear",
  "rearws": "rear",
  "rightfender": "front right",
  "rightfoglamp": "front right",
  "partial_bonnet": "front",
  "rightreardoorcladdingmissing": "rear right",
  "rightfrontventglass": "front right",
  "frontbumpergrillemissing": "front",
  "lefttaillampmissing": "rear left",
  "partial_leftfender": "front left",
  "rightroofside": "front right",
  "partial_frontbumper": "front",
  "frontbumpermissing": "front",
  "bonnet": "front",
  "doorglass": "front",
  "rightfrontbumper": "front right",
  "frontbumpercladdingdetached": "front",
  "partial_leftqpanel": "front left",
  "leftheadlampmissing": "front left",
  "leftorvm": "front left",
  "leftfoglamp": "front left",
  "partial_rightfrontdoor": "front right",
  "rightorvmbroken": "front right",
  "leftrearbumper": "rear left",
  "leftwa": "front left",
  "tailgate": "rear",
  "lefttaillamp": "rear left",
  "leftrunningboard": "front left",
  "leftquarterglass": "front left",
  "leftdpillar": "front left",
  "rightquarterglass": "front right",
  "mtailgate": "rear",
  "rightdpillar": "front right",
  "headlightwasher": "front",
  "bumperdent": "front",
  "frontbumpergrillebroken": "front",
  "rightwa": "front right",
  "leftbootlamp": "rear left",
  "rightrunningboard": "front right",
  "rightfoglampassemblybroken": "front right",
  "rearwsmissing": "rear",
  "rightfoglampmissing": "front right",
  "rightbootlampmissing": "rear right",
  "partial_rearws": "rear",
  "leftbootlampmissing": "rear left",
  "leftfrontdoor": "front left",
  "rightreardoor": "rear right",
  "frontbumper": "front",
  "leftfoglampmissing": "front left",
  "leftfendermissing": "front left",
  "leftorvmbroken": "front left",
  "rightorvm": "front right",
  "frontbumpercladding": "front",
  "righttaillampmissing": "rear right",
  "rightfrontdoor": "front right",
  "leftfrontbumper": "front left",
  "leftreardoor": "rear left",
  "righttaillamp": "rear right",
  "leftrearventglass": "rear left",
  "partial_leftfrontdoor": "front left",
  "leftrearcladding": "rear left",
  "righttailgate": "rear right",
  "rightwatorn": "front right",
  "frontws": "front",
  "leftapillar": "front left",
  "headlightwashermissing": "front",
  "leftwatorn": "front left",
  "rightfrontdoorcladding": "front right",
  "partial_rearbumper": "rear",
  "partial_tailgate": "rear",
  "partial_rightreardoor": "rear right",
  "lowerbumpergrillebroken": "front",
  "partial_leftreardoor": "rear left",
  "fadelamp": "front",
  "bumpertear": "front",
  "rightreardoorglass": "rear right",
  "rightwadetached": "front right",
  "leftfrontdoorglass": "front left",
  "rightrearventglass": "rear right",
  "leftfoglampassemblybroken": "front left",
  "leftbpillar": "front left",
  "rightbpillar": "front right",
  "rearbumper": "rear",
  "rightfrontdoorglass": "front right",
  "partial_rightqpanel": "front right",
  "leftfrontventglass": "front left",
  "lowerbumpergrillemissing": "front",
  "rightfendermissing": "front right",
  "rightheadlamp": "front right",
  "frontbumpergrille": "front",
  "rightcabcorner": "front right"}

dataset = {}
for k in d:
    for i in range(len(d[k])):
        if d[k][i] in value_mapping:
            dataset[k] = value_mapping[d[k][i]]
            i+=1

with open('dataset.json', 'w') as fp:
    json.dump(dataset, fp)