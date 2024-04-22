import numpy as np
import pandas as pd


emptyFloat = np.empty((3,4))
fullFloat = np.full((3,4),11)

emptyInt = np.empty((3,4),dtype =int)
fullInt = np.full((3,4),5)

emptyBool = np.empty((3,4),dtype=bool)
fullBool = np.full((3,4),True)

data_list = np.array([emptyFloat,emptyInt,emptyBool,fullFloat,fullInt,fullBool])
for data,i in enumerate(data_list):
    print(f"{i}:")
    print(data)
    print(data.dtype)
