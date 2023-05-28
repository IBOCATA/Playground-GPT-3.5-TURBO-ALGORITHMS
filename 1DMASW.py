# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:48:20 2023

@author: ilias
"""


import openquake.engine as oqe 
from openquake.hazardlib.imt import PGA, PGV
from openquake.commonlib import logs
from openquake.calculators.base import calculators
import swprocess as swp 
from obspy import read, Stream 
from openquake.hazardlib import geo

import os
from openquake.commonlib import logs






 # Generate Plausible Accelerogram for the given PGA and PGV values  
acc_stream = Stream()   
for trace in [PGA(), PGV()]:     acc_stream += trace  

 # Obtain frequencies of subsurface for highly random media using Masw process (Multi-channel Analysis of Surface Waves)  
freqs = swp.masw_process(acc_stream) 

 # Inverse the signal with Masw process using SWProcess library to detect reservoir of oil & gas  
reservoirs = swp.masw_inverse(freqs) 
print("Detected Reservoirs: ", reservoirs) 

 # Map the detected Reservoirs of Oil & Gas  
swp.map_reservoirs(reservoirs) 
 
 # View the mapped Reservoirs of Oil & Gas  
swp.view_reservoirs()