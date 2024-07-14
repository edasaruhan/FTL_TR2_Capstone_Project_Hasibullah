import pandas as pd

fh = pd.read_csv("heart_raw.csv")
# Checking for missing values
print(fh.isnull().sum())
# Remove duplicates if any
print(fh.duplicated())
fh = fh.drop_duplicates()
# as caa (number of major vessels colord by fluoroscopy) is between
# 0-3 and the set is between 0-4 we need to clean the data first
median_caa = fh[fh['caa']!=4]['caa'].median()
fh['caa']= fh['caa'].replace(4,median_caa)
print('Replacing the caa values...')

fh.to_csv('heart.csv', index=False)
print('Done!')