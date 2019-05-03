# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2018

@author: eser.arslan
"""
import os
import json

from itertools import islice

config=None

#   Load config to get parameters
def loadConfig(file='config/config.json'):
    global config
    if(config==None):
        if(os.path.exists(file)):
            print("Opening Local Config")
            with open(file, 'r') as f:
                config = json.load(f)
        else:
            print("Opening Container Mapped Config")
            with open('/config/config.json', 'r') as f:
                config = json.load(f)
    return config

#   Create chunk generator fro multiprocessing
def dict_chunk_generator(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}
