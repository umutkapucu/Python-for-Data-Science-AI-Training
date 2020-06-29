# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:34:32 2020

@author: umut.kapucu
"""

import pandas as pd

csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

df.loc[0.0]