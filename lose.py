import sqlite3
import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

conn = sqlite3.connect('lose.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Admission ''')

cur.execute('''CREATE TABLE "Admission" (
	"case_id" INTEGER NOT NULL UNIQUE,
    "Hospital_code" INTEGER NOT NULL,
	"Hospital_type_code" TEXT NOT NULL,
	"City_Code_Hospital" INTEGER NOT NULL,
	"Hospital_region_code" TEXT NOT NULL,
	"Available_extra_Rooms" INTEGER NOT NULL,
	"Department" TEXT NOT NULL,
	"Ward_Type"	TEXT NOT NULL,
	"Ward_Facility_Code" TEXT NOT NULL,
	"Bed_Grade"	REAL NOT NULL,
	"patientid"	INTEGER NOT NULL,
	"City_Code_Patient"	REAL NOT NULL,
	"Type_of_Admission"	TEXT NOT NULL,
	"Severity_of_Illness" TEXT NOT NULL,
	"Visitors_with_Patient" INTEGER NOT NULL,
	"Age" TEXT NOT NULL,
	"Admission_Deposit" REAL NOT NULL,
	"Stay" TEXT NOT NULL,
	PRIMARY KEY("case_id" AUTOINCREMENT))''')

fh = open('train_data.csv','r')
lines = fh.readlines()
header = lines[0]
fieldnames = header.strip().split(',')
print('Fieldnames: ')
print(fieldnames)
print()
count = 0
for row in lines[1:]:
    count = count + 1
    value = row.strip().split(',')
    #print(values)
    cur.execute('''INSERT OR IGNORE INTO Admission (case_id, Hospital_code, Hospital_type_code, City_Code_Hospital,
            Hospital_region_code, Available_extra_Rooms, Department, Ward_Type, Ward_Facility_Code,
            Bed_Grade, patientid, City_Code_Patient, Type_of_Admission, Severity_of_Illness,
            Visitors_with_Patient, Age, Admission_Deposit, Stay) VALUES ( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )''',
            ( value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8],
            value[9], value[10], value[11], value[12], value[13], value[14], value[15], value[16],
            value[17] ))
    if count >= 1000:
        conn.commit()
        #print(row)
        count = 0

conn.commit()

hosp_dict  = {}
cur.execute(''' SELECT Hospital_code FROM Admission ''')
for row in cur:
    if row[0] in hosp_dict:
        hosp_dict[row[0]] += 1
    else:
        hosp_dict[row[0]] = 1

print('Hospital, Admissions: ')
print(sorted(hosp_dict.items(), key = lambda k: k[1], reverse = True))
print()

patientid  = {}
cur.execute(''' SELECT patientid FROM Admission ''')
for row in cur:
    if row[0] in patientid:
        patientid[row[0]] += 1
    else:
        patientid[row[0]] = 1

Patients = sorted(patientid.items(), key = lambda k: k[1], reverse = True)
print('Top Ten Patients, Admissions: ')
print(Patients[0:10])
print('Total Patients: ', len(Patients))
print()

depart_dict  = {}
cur.execute(''' SELECT Department FROM Admission ''')
for row in cur:
    if row[0] in depart_dict:
        depart_dict[row[0]] += 1
    else:
        depart_dict[row[0]] = 1

print('Department, Admissions: ')
print(sorted(depart_dict.items(), key = lambda k: k[1], reverse = True))
print()

type_adm  = {}
cur.execute(''' SELECT Type_of_Admission FROM Admission ''')
for row in cur:
    if row[0] in type_adm:
        type_adm[row[0]] += 1
    else:
        type_adm[row[0]] = 1

print('Type of Admission, Admissions: ')
print(sorted(type_adm.items(), key = lambda k: k[1], reverse = True))
print()

severity  = {}
cur.execute(''' SELECT Severity_of_Illness FROM Admission ''')
for row in cur:
    if row[0] in severity:
        severity[row[0]] += 1
    else:
        severity[row[0]] = 1
print('Severity, Admissions: ')
print(sorted(severity.items(), key = lambda k: k[1], reverse = True))
print()

age  = {}
cur.execute(''' SELECT Age FROM Admission''')
for row in cur:
    cur.execute("UPDATE Admission SET Age = 5 WHERE Age = '0-10'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 15 WHERE Age = '11-20'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 25 WHERE Age = '21-30'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 35 WHERE Age = '31-40'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 45 WHERE Age = '41-50'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 55 WHERE Age = '51-60'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 65 WHERE Age = '61-70'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 75 WHERE Age = '71-80'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 85 WHERE Age = '81-90'")
    conn.commit()
    cur.execute("UPDATE Admission SET Age = 95 WHERE Age = '91-100'")
    conn.commit()

cur.execute(''' SELECT Age FROM Admission ''')
for row in cur:
    if row[0] in age:
        age[row[0]] += 1
    else:
        age[row[0]] = 1

print('Age(years), Admissions: ')
print(sorted(age.items(), key = lambda k: k[1], reverse = True))
print()

los  = {}
cur.execute(''' SELECT Stay FROM Admission''')
for row in cur:
    cur.execute("UPDATE Admission SET Stay = 5 WHERE Stay = '0-10'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 15 WHERE Stay = '11-20'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 25 WHERE Stay = '21-30'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 35 WHERE Stay = '31-40'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 45 WHERE Stay = '41-50'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 55 WHERE Stay = '51-60'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 65 WHERE Stay = '61-70'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 75 WHERE Stay = '71-80'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 85 WHERE Stay = '81-90'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 95 WHERE Stay = '91-100'")
    conn.commit()
    cur.execute("UPDATE Admission SET Stay = 150 WHERE Stay = 'More than 100 Days'")
    conn.commit()

cur.execute('''SELECT Stay FROM Admission''')
for row in cur:
    if row[0] in los:
        los[row[0]] += 1
    else:
        los[row[0]] = 1

print('Stay(days), Admissions: ')
print(sorted(los.items(), key = lambda k: k[1], reverse = True))
print()

def Spearman(dict):
    k = []
    v = []
    for key,value in dict.items():
        k.append(int(key))
        v.append(int(value))
    coef, p = spearmanr(k, v)
    #print('Spearman ranked Correlation: ', coef)
    #print('p-value: ', p)
    return coef, p

stay_age_5 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '5'")
for row in cur:
    if row[0] in stay_age_5:
        stay_age_5[row[0]] += 1
    else:
        stay_age_5[row[0]] = 1

#print('Stay(days)_Age_5, Admissions: ')
#print(sorted(stay_age_5.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_15 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '15'")
for row in cur:
    if row[0] in stay_age_15:
        stay_age_15[row[0]] += 1
    else:
        stay_age_15[row[0]] = 1

#print('Stay(days)_Age_15, Admissions: ')
#print(sorted(stay_age_15.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_25 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '25'")
for row in cur:
    if row[0] in stay_age_25:
        stay_age_25[row[0]] += 1
    else:
        stay_age_25[row[0]] = 1

#print('Stay(days)_Age_25, Admissions: ')
#print(sorted(stay_age_25.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_35 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '35'")
for row in cur:
    if row[0] in stay_age_35:
        stay_age_35[row[0]] += 1
    else:
        stay_age_35[row[0]] = 1

#print('Stay(days)_Age_35, Admissions: ')
#print(sorted(stay_age_35.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_45 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '45'")
for row in cur:
    if row[0] in stay_age_45:
        stay_age_45[row[0]] += 1
    else:
        stay_age_45[row[0]] = 1

#print('Stay(days)_Age_45, Admissions: ')
#print(sorted(stay_age_45.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_55 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '55'")
for row in cur:
    if row[0] in stay_age_55:
        stay_age_55[row[0]] += 1
    else:
        stay_age_55[row[0]] = 1

#print('Stay(days)_Age_55, Admissions: ')
#print(sorted(stay_age_55.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_65 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '65'")
for row in cur:
    if row[0] in stay_age_65:
        stay_age_65[row[0]] += 1
    else:
        stay_age_65[row[0]] = 1

#print('Stay(days)_Age_65, Admissions: ')
#print(sorted(stay_age_65.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_75 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '75'")
for row in cur:
    if row[0] in stay_age_75:
        stay_age_75[row[0]] += 1
    else:
        stay_age_75[row[0]] = 1

#print('Stay(days)_Age_75, Admissions: ')
#print(sorted(stay_age_75.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_85 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '85'")
for row in cur:
    if row[0] in stay_age_85:
        stay_age_85[row[0]] += 1
    else:
        stay_age_85[row[0]] = 1

#print('Stay(days)_Age_85, Admissions: ')
#print(sorted(stay_age_85.items(), key = lambda k: k[1], reverse = True))
#print()

stay_age_95 = {}
cur.execute("SELECT Stay FROM Admission WHERE Age = '95'")
for row in cur:
    if row[0] in stay_age_95:
        stay_age_95[row[0]] += 1
    else:
        stay_age_95[row[0]] = 1

#print('Stay(days)_Age_95, Admissions: ')
#print(sorted(stay_age_95.items(), key = lambda k: k[1], reverse = True))
#print()

print('Correlation between LOS and admissions: ', Spearman(los))
print()
print('Correlation between 0-10 years and LOS: ', Spearman(stay_age_5))
print()
print('Correlation between 11-20 years and LOS: ', Spearman(stay_age_15))
print()
print('Correlation between 21-30 years and LOS: ', Spearman(stay_age_25))
print()
print('Correlation between 31-40 years and LOS: ', Spearman(stay_age_35))
print()
print('Correlation between 41-50 years and LOS: ', Spearman(stay_age_45))
print()
print('Correlation between 51-60 years and LOS: ', Spearman(stay_age_55))
print()
print('Correlation between 61-70 years and LOS: ', Spearman(stay_age_65))
print()
print('Correlation between 71-80 years and LOS: ', Spearman(stay_age_75))
print()
print('Correlation between 81-90 years and LOS: ', Spearman(stay_age_85))
print()
print('Correlation between 91-100 years and LOS: ', Spearman(stay_age_95))
print()

def Plot(dict):
    k = []
    v = []
    for key,value in dict.items():
        k.append(int(key))
        v.append(int(value))
    plt.scatter(k, v)
    plt.title('Correlation between Age and LOS')
    plt.xlabel('Length of Stay(days) - LOS')
    plt.ylabel('Total Admissions')
    x = np.array(k)
    y = np.array(v)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color = 'black')
    plt.show()
    return k, v

print('Scatter plot 1: [LOS], [Admissions 11-20years] = ', Plot(stay_age_15))
print('Scatter plot 2: [LOS], [Admissions 81-90years] = ', Plot(stay_age_85))

cur.close()
