import pandas as pd
import joblib
import sqlite3 

conn = sqlite3.connect('heart.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User(age INTEGER, sex INTEGER, cp INTEGER, trtbps INTEGER, chol INTEGER, fbs INTEGER,
               rectecg INTEGER, thalachh INTEGER, exng INTEGER, oldpeak FLOAT, slp INTEGER, caa INTEGER, thall INTEGER, output INTEGER)''')

features = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
age = int(input("""1)Age cannot be negative!
                   Enter the age of the Patient:"""))
sex = int(input("""2)Sex (2 values)
0: for female
1: for male!
                   Enter the sex of the Patient:"""))
cp = int(input("""3)cp: Chest Pain type (4 values)
0: typical angina
1: atypical angina
2: non-anginal pain
3: asymptomatic
                   Enter the cp of the Patient:"""))
trtbps = int(input("""4)trtbps: Resting blood pressure (mm Hg) (numeric)
                   Enter the trtbps of the Patient:"""))
chol = int(input("""5)chol: Serum cholesterol (mg/dl) (numeric)
                   Enter the chol of the Patient:"""))
fbs = int(input("""6)fbs: Fasting blood sugar > 120 mg/dl (binary: 1 = true, 0 = false)
                   Enter the fbs of the Patient:"""))
restecg = int(input("""7)restecg: Resting electrocardiographic results (ordinal categorical):
0: Normal
1: ST-T wave abnormality
2: Left ventricular hypertrophy
                   Enter the restecg of the Patient:"""))
thalachh = int(input("""8)thalachh: Maximum heart rate achieved (numeric)
                   Enter the thalachh of the Patient:"""))
exng = int(input("""9)exng: Exercise induced angina (binary: 1 = yes, 0 = no)
                   Enter the exng of the Patient:"""))
oldpeak = float(input("""10)oldpeak: ST depression induced by exercise relative to rest (numeric)(0-6.2)
                   Enter the oldpeak of the Patient:"""))
slp = int(input("""11)slp: Slope of the peak exercise ST segment (ordinal categorical):
0: Upsloping
1: Flat
2: Downsloping
                   Enter the slp of the Patient:"""))
caa = int(input("""12)caa: Number of major vessels (0-3) colored by fluoroscopy (numeric)

                   Enter the caa of the Patient:"""))
thall = int(input("""13)thall: Thallium heart scan (ordinal categorical):
1: Normal
2: Fixed defect
3: Reversible defect
                   Enter the thall of the Patient:"""))


user_input = pd.DataFrame([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]], columns=features)

scaler = joblib.load('scaler.pkl')
print('Scaler loaded successfully!')
user_input_scaled = scaler.transform(user_input)
model = joblib.load('model.pkl')
print('Model loaded successfully!')
print('Predecting the output...')
a = model.predict(user_input_scaled)

output = int(a[0])
if output==1:
    print(f'''The patient has a highly risk of heart attack!!!
Please take the required actions immediately
Predicted value: {output}''')
else:
    print(f'''The patient doesn't have the risk of heart attack!!!
Predicted value: {output}''')

cursor.execute('''INSERT INTO User(age, sex, cp, trtbps, chol, fbs, rectecg,thalachh, exng, oldpeak, slp, caa, thall, output) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
               ,(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall,output))
conn.commit()
print("Successfully added to the database!")
conn.close()