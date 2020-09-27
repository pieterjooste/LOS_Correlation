From Kaggle:

Problem Statement Recent Covid-19 Pandemic has raised alarms over one of the most overlooked area to focus: Healthcare Management. While healthcare management has various use cases for using data science, patient length of stay is one critical parameter to observe and predict if one wants to improve the efficiency of the healthcare management in a hospital.This parameter helps hospitals to identify patients of high LOS risk (patients who will stay longer) at the time of admission. Once identified, patients with high LOS risk can have their treatment plan optimized to miminize LOS and lower the chance of staff/visitor infection. Also, prior knowledge of LOS can aid in logistics such as room and bed allocation planning.Suppose you have been hired as Data Scientist of HealthMan – a not for profit organization dedicated to manage the functioning of Hospitals in a professional and optimal manner.The task is to accurately predict the Length of Stay for each patient on case by case basis so that the Hospitals can use this information for optimal resource allocation and better functioning. The length of stay is divided into 11 different classes ranging from 0-10 days to more than 100 days.

Data Descriptiontraindata.csv – File containing features related to patient, hospital and Length of stay on case basis traindata_dictonary.csv – File containing the information of the features in train file

Results:

C:\Users\User\Desktop\py4e\Databases\ProjectData>python lose.py

Fieldnames:

['case_id', 'Hospital_code', 'Hospital_type_code', 'City_Code_Hospital', 'Hospital_region_code', 'Available Extra Rooms in Hospital', 'Department', 'Ward_Type', 'Ward_Facility_Code', 'Bed Grade', 'patientid', 'City_Code_Patient', 'Type of Admission', 'Severity of Illness', 'Visitors with Patient', 'Age', 'Admission_Deposit', 'Stay']

Hospital, Admissions:

[(26, 33076), (23, 26566), (19, 21219), (6, 20425), (14, 17328), (11, 17328), (28, 17137), (27, 14244), (9, 11510), (29, 11311), (12, 11297), (32, 10703), (25, 9834), (10, 9435), (15, 9257), (21, 8150), (24, 7992), (3, 7116), (17, 5501), (5, 5261), (1, 5249), (13, 5236), (2, 5102), (30, 5002), (22, 4277), (31, 3967), (16, 3671), (8, 3663), (18, 3630), (20, 1405), (7, 1306), (4, 1240)]

Top Ten Patients, Admissions:

[(66714, 50), (91292, 43), (38525, 39), (101359, 36), (33491, 34), (32886, 32), (6645, 31), (31203, 30), (99644, 30), (126596, 29)]

Total Patients: 92017

Department, Admissions:

[('gynecology', 249486), ('anesthesia', 29649), ('radiotherapy', 28516), ('TB & Chest disease', 9586), ('surgery', 1201)]

Type of Admission, Admissions:

[('Trauma', 152261), ('Emergency', 117676), ('Urgent', 48501)]

Severity, Admissions:

[('Moderate', 175843), ('Minor', 85872), ('Extreme', 56723)]

Age(years), Admissions:

[('45', 63749), ('35', 63639), ('55', 48514), ('25', 40843), ('75', 35792), ('65', 33687), ('15', 16768), ('85', 7890), ('5', 6254), ('95', 1302)]

Stay(days), Admissions:

[('25', 87491), ('15', 78139), ('35', 55159), ('55', 35018), ('5', 23604), ('45', 11743), ('75', 10254), ('150', 6683), ('85', 4838), ('95', 2765), ('65', 2744)]

Correlation between LOS and admissions: (-0.7636363636363637, 0.006233059747904751)

Correlation between 0-10 years and LOS: (-0.8181818181818182, 0.0020831448404786904)

Correlation between 11-20 years and LOS: (-0.8636363636363636, 0.0006116938500931706)

Correlation between 21-30 years and LOS: (-0.8090909090909091, 0.002558580199713915)

Correlation between 31-40 years and LOS: (-0.790909090909091, 0.003746082953397406)

Correlation between 41-50 years and LOS: (-0.7636363636363637, 0.006233059747904751)

Correlation between 51-60 years and LOS: (-0.7636363636363637, 0.006233059747904751)

Correlation between 61-70 years and LOS: (-0.7363636363636363, 0.009759535959916903)

Correlation between 71-80 years and LOS: (-0.7636363636363637, 0.006233059747904751)

Correlation between 81-90 years and LOS: (-0.7181818181818183, 0.01279959806885844)

Correlation between 91-100 years and LOS: (-0.7899625734105961, 0.0038173876554122937)

Scatter plot 1: [LOS], [Admissions 11-20years] = ([5, 35, 25, 15, 55, 45, 75, 85, 95, 65, 150], [1552, 2681, 4312, 5343, 1429, 510, 350, 223, 71, 89, 208])

Scatter plot 2: [LOS], [Admissions 81-90years] = ([5, 15, 55, 25, 35, 45, 75, 85, 95, 150, 65], [422, 1392, 1082, 1920, 1504, 379, 402, 216, 132, 326, 115])



Discussion:

A strong negative correlation was found between age and length of stay in hospital. The stongest correlation was for 11-20 years and weakest for 81-90 years.

Using the code correlation for hospital, department, type of admission and severity can still be examined.
