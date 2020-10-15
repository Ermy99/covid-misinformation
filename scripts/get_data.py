
import numpy as numpy
import os
import urllib.request


print('Downloading data...')
url = 'https://raw.githubusercontent.com/susanli2016/NLP-with-Python/master/data/corona_fake.csv'
saveto = "data\\raw_data.csv"
urllib.request.urlretrieve(url,saveto)

