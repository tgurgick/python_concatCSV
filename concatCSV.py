'''
STAND ALONE FUNCTION FOR QUICKLY CONCATINATING MULTIPLE CSV INTO A SINGLE FILE 
NOTE: ASSUMES THE DATA SETS ARE THE SAME STRUCTURE
NOVEMBER 2018
'''

__author__ = "Trevor Gurgick"
__copyright__ = "Copyright (c) 2018, Trevor Gurgick"
__license__ = "GPL"
__version__ = "0.0.1"

import pandas as pd
import csv
import os

def concatCSV(dataset_a,dataset_b,filename):
	cwd = os.getcwd()
	path = '%s/%s.csv' %(cwd,filename)
	#dataset_a = pd.DataFrame(dataset_a,dtype=None)
	#dataset_b = pd.DataFrame(dataset_b,dtype=None)	
	data = [dataset_a,dataset_b]	
	data = pd.concat(data)
	data.to_csv(path)	
	print("SAVED: %s" %(path))	
if __name__ == '__main__':
	concatCSV(dataset_a,dataset_b,filename)