import pandas as pd
import matplotlib.pyplot as plt

fh = pd.read_csv("heart.csv")
# print(fh.head())
# print(fh.info())
# print(fh.describe())
# print(fh['caa'].unique())
# print(fh.isnull().sum())#describe shows this information as well
# as caa (number of major vessels colord by fluoroscopy) is between
# 0-3 and the set is between 0-4 we need to clean the data first 

fig, axs = plt.subplots(3,3,figsize=(14,8))
axs[0,0].scatter(fh[fh['sex']==1].index,fh[fh['sex']==1]['age'],color="green", label='age', marker='o')
axs[0,0].scatter(fh[fh['sex']==1].index,fh[fh['sex']==1]["output"],color='blue',label='output')
axs[0,0].set_title("Age in Heart Attacks (Males)")
axs[0,0].legend()

axs[0,1].scatter(fh[fh['sex']==0].index,fh[fh['sex']==0]['age'],color="green", label='age', marker='o')
axs[0,1].scatter(fh[fh['sex']==0].index,fh[fh['sex']==0]["output"],color='blue',label='output')
axs[0,1].set_title("Age in Heart Attack (Females)")
axs[0,1].legend()

axs[0,2].plot(fh.index,fh['cp'], color="green" ,label='cp')
axs[0,2].plot(fh.index,fh['output'], color="blue" ,label='output')
axs[0,2].set_title("Chest Pain effect in Heart Attack")
axs[0,2].legend()

axs[1,0].plot(fh[fh['output']==1]['trtbps'],color='red',label='trtbps')
axs[1,0].plot(fh[fh['output']==1]['output'],color='blue',label='output')
axs[1,0].set_title("blood pressure (mm Hg) effect in heart attack")
axs[1,0].legend()

axs[1,1].plot(fh[fh['output']==1]['chol'],color='black',label='chol')
axs[1,1].plot(fh[fh['output']==1]['output'],color='blue',label='output')
axs[1,1].set_title("Serum cholesterol (mg/dl) effect in heart attack")
axs[1,1].legend()

axs[1,2].plot(fh[fh['output']==1]['thalachh'],color='green',label='thalachh')
axs[1,2].plot(fh[fh['output']==1]['output'],color='blue',label='output')
axs[1,2].set_title("Maximum heart rate effect in heart attack")
axs[1,2].legend()

axs[2,0].plot(fh.index,fh['slp'], color="brown",label='slp')
axs[2,0].plot(fh.index,fh['output'], color="blue",label='output')
axs[2,0].set_title("Slope of the peak exercise effect in Heart Attack")
axs[2,0].legend()

axs[2,1].plot(fh.index,fh['caa'], color="orange",label='caa')
axs[2,1].plot(fh.index,fh['output'], color="blue",label='output')
axs[2,1].set_title("Significant vessels colored by fluoroscopy effect in Heart Attack")
axs[2,1].legend()

axs[2,2].plot(fh.index,fh['fbs'], color="grey",label='fbs')
axs[2,2].plot(fh.index,fh['output'], color="blue",label='output')
axs[2,2].set_title("Fasting blood sugar > 120 mg/dl effect in Heart Attack")
axs[2,2].legend()

# fig, axs = plt.subplots(1,2,figsize=(10,4))
# axs[0].plot(fh[fh['output']==1]['trtbps'],color='red',label='blood pressure')
# axs[0].plot(fh[fh['output']==1]['chol'],color='black',label='Serum cholesterol')
# axs[0].plot(fh[fh['output']==1]['thalachh'],color='green',label='Maximum heart rate')
# axs[0].legend()
# axs[1].plot(fh)

plt.tight_layout()
plt.show()


