"""

Main codebase of prototyping algo analysis

Created: 15/09/2019
Author: MBRS

"""

"""
1. READ DATA
"""

import pandas as pd
import os


#Dir
active_dir = '/Users/Mich/Github/Moonbird/data_analysis/yasu/ppg_readings/'
#Name
files_in_active_dir = os.listdir(active_dir)


df = pd.read_csv(active_dir+files_in_active_dir[0]);