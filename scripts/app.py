#!/usr/bin/env python
""" 
    A high-level code for running the SYSNet software

    Take a look into the config file under the directory 'scripts'
    to learn about the input parameters.
    
    Mehdi Rezaie, mr095415@ohio.edu
    October 2020
"""
import sysnet

debug = False
if debug:
    sysnet.detect_anomaly() # this will slow down

config = sysnet.parse_cmd_arguments('config.yaml')
pipeline = sysnet.SYSNet(config)
pipeline.run()
