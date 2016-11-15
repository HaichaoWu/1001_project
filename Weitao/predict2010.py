import pandas as pd
import os

raw_target_data = pd.read_csv("../CSD20_Resident_Data_Phase_1.csv")
#First predict the number of students in K
cts = sorted(set(raw_target_data['2010 Census Tract']))
cols = ['CnsTrct','KStdntNum','Y5','Y6','Y7','Wht','Blck','Amrc','Asia','HawP','Mix','Hispn']
data = pd.DataFrame(columns = cols)
data['CnsTrct'] = cts
i = 0
for ct in cts:
    StdntNum = pd.DataFrame(raw_target_data.ix[(raw_target_data['2010 Census Tract'] == ct) & (raw_target_data['School Year'] == 20102011) & (raw_target_data['Grade Level'] == 'K')])
    if (StdntNum.shape[0] == 0):
        data['KStdntNum'][i] = 0
    else:
        data['KStdntNum'][i] = StdntNum['Count of Students'].values[0]
    i = i + 1
age_data = pd.read_csv("../11-9/population_2010_accurate.csv")
for i in range(len(age_data["2010 Census Tract"])):
    if (age_data.ix[i,1] % 1 != 0):
        age_data.set_value(i,"2010 Census Tract",age_data.ix[i,1] * 100)
age_data = age_data[['2010 Census Tract','5 Years','6 Years','7 to 9 Years']]
#Some error here
data_merge = pd.merge(data,age_data,how='left',on=['CnsTrct','2010 Census Tract'])
print(data_merge)
