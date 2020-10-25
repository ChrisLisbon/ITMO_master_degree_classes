# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:22:04 2020

@author: Julia
"""

from gap_filling_functions import *
from sklearn.metrics import mean_squared_error


values=np.array([-10, -9, -8, -7, -6, -5, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100, 7, 12, 15, 17, 20], dtype=np.float64)

numbers=np.arange(len(values))
plt.rcParams['figure.figsize'] = [6, 3]
fig, ax = plt.subplots()
ax.plot(numbers, values)
ax.scatter(numbers, values, color='r')
plt.ylim((-11,18))
ax.grid()
plt.show()

print(values)

direct=fill_gaps_linear(values, -100)
plt.rcParams['figure.figsize'] = [6, 3]
fig, ax = plt.subplots()
ax.plot(numbers, direct)
ax.scatter(numbers, direct, color='r')
plt.ylim((-11,18))
ax.grid()
plt.show()

print(values)

direct=fill_gaps_poly(values, -100)
plt.rcParams['figure.figsize'] = [6, 3]
fig, ax = plt.subplots()
ax.plot(numbers, direct)
ax.scatter(numbers, direct, color='r')
plt.ylim((-11,18))
ax.grid()
plt.show()

print(values)

direct=fill_gaps_hybrid(values, -100)
plt.rcParams['figure.figsize'] = [6, 3]
fig, ax = plt.subplots()
ax.plot(numbers, direct)
ax.scatter(numbers, direct, color='r')
plt.ylim((-11,18))
ax.grid()
plt.show()

print(values)


file_path='C:/Users/Julia/Documents/ITMO/Statistical_data_analysis/1_data_preparation/parsed_2018-2020/WI_Necedah_5_WNW.txt'
df=pd.read_csv(file_path, sep=' ', header=None)
SUR_TEMP=df[14]
SOIL_TEMP_5=df[23]
SOIL_TEMP_10=df[24]
SOIL_TEMP_20=df[25]
SOIL_TEMP_50=df[26]
SOIL_TEMP_100=df[27]
numbers=np.arange(len(SUR_TEMP))
plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt')
plt.ylim((-35,35))
plt.legend()
plt.show()


gap_genered_x=np.random.choice(range(0, 1000), 100, replace=False)
print(gap_genered_x)    

test_SUR_TEMP=[]
test_SOIL_TEMP_5=[]
test_SOIL_TEMP_10=[]
test_SOIL_TEMP_20=[]
test_SOIL_TEMP_50=[]
test_SOIL_TEMP_100=[]

for val in gap_genered_x:
    test_SUR_TEMP.append(SUR_TEMP[val])
    SUR_TEMP[val]=-9999
    test_SOIL_TEMP_5.append(SOIL_TEMP_5[val])
    SOIL_TEMP_5[val]=-9999
    test_SOIL_TEMP_10.append(SOIL_TEMP_10[val])
    SOIL_TEMP_10[val]=-9999
    test_SOIL_TEMP_20.append(SOIL_TEMP_20[val])
    SOIL_TEMP_20[val]=-9999
    test_SOIL_TEMP_50.append(SOIL_TEMP_50[val])
    SOIL_TEMP_50[val]=-9999
    test_SOIL_TEMP_100.append(SOIL_TEMP_100[val])
    SOIL_TEMP_100[val]=-9999
    
plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt\nGAPS_GENERATION')
plt.ylim((-35,35))
plt.legend()
plt.show()

SUR_TEMP_lin=fill_gaps_linear(SUR_TEMP, -9999)
SOIL_TEMP_5_lin=fill_gaps_linear(SOIL_TEMP_5, -9999)
SOIL_TEMP_10_lin=fill_gaps_linear(SOIL_TEMP_10, -9999)
SOIL_TEMP_20_lin=fill_gaps_linear(SOIL_TEMP_20, -9999)
SOIL_TEMP_50_lin=fill_gaps_linear(SOIL_TEMP_50, -9999)
SOIL_TEMP_100_lin=fill_gaps_linear(SOIL_TEMP_100, -9999)

plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP_lin, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5_lin, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10_lin, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20_lin, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50_lin, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100_lin, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt\nLINEAR_REGRESSION')
plt.ylim((-35,35))
plt.legend()
plt.show()

predicted_SUR_TEMP_lin=[]
predicted_SOIL_TEMP_5_lin=[]
predicted_SOIL_TEMP_10_lin=[]
predicted_SOIL_TEMP_20_lin=[]
predicted_SOIL_TEMP_50_lin=[]
predicted_SOIL_TEMP_100_lin=[]

for val in gap_genered_x:
    predicted_SUR_TEMP_lin.append(SUR_TEMP_lin[val])
    predicted_SOIL_TEMP_5_lin.append(SOIL_TEMP_5_lin[val])
    predicted_SOIL_TEMP_10_lin.append(SOIL_TEMP_10_lin[val])
    predicted_SOIL_TEMP_20_lin.append(SOIL_TEMP_20_lin[val])
    predicted_SOIL_TEMP_50_lin.append(SOIL_TEMP_50_lin[val])
    predicted_SOIL_TEMP_100_lin.append(SOIL_TEMP_100_lin[val])

print('\nLinear regression RMSE:')    
SUR_TEMP_error_lin=mean_squared_error(test_SUR_TEMP, predicted_SUR_TEMP_lin)
print(SUR_TEMP_error_lin)
SOIL_TEMP_5_error_lin=mean_squared_error(test_SOIL_TEMP_5, predicted_SOIL_TEMP_5_lin)
print(SOIL_TEMP_5_error_lin)
SOIL_TEMP_10_error_lin=mean_squared_error(test_SOIL_TEMP_10, predicted_SOIL_TEMP_10_lin)
print(SOIL_TEMP_10_error_lin)
SOIL_TEMP_20_error_lin=mean_squared_error(test_SOIL_TEMP_20, predicted_SOIL_TEMP_20_lin)
print(SOIL_TEMP_20_error_lin)
SOIL_TEMP_50_error_lin=mean_squared_error(test_SOIL_TEMP_50, predicted_SOIL_TEMP_50_lin)
print(SOIL_TEMP_50_error_lin)
SOIL_TEMP_100_error_lin=mean_squared_error(test_SOIL_TEMP_100, predicted_SOIL_TEMP_100_lin)
print(SOIL_TEMP_100_error_lin)

SUR_TEMP_poly=fill_gaps_poly(SUR_TEMP, -9999)
SOIL_TEMP_5_poly=fill_gaps_poly(SOIL_TEMP_5, -9999)
SOIL_TEMP_10_poly=fill_gaps_poly(SOIL_TEMP_10, -9999)
SOIL_TEMP_20_poly=fill_gaps_poly(SOIL_TEMP_20, -9999)
SOIL_TEMP_50_poly=fill_gaps_poly(SOIL_TEMP_50, -9999)
SOIL_TEMP_100_poly=fill_gaps_poly(SOIL_TEMP_100, -9999)

plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP_poly, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5_poly, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10_poly, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20_poly, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50_poly, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100_poly, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt\nPOLYNOMIAL_REGRESSION')
plt.ylim((-35,35))
plt.legend()
plt.show()

predicted_SUR_TEMP_poly=[]
predicted_SOIL_TEMP_5_poly=[]
predicted_SOIL_TEMP_10_poly=[]
predicted_SOIL_TEMP_20_poly=[]
predicted_SOIL_TEMP_50_poly=[]
predicted_SOIL_TEMP_100_poly=[]

for val in gap_genered_x:
    predicted_SUR_TEMP_poly.append(SUR_TEMP_poly[val])
    predicted_SOIL_TEMP_5_poly.append(SOIL_TEMP_5_poly[val])
    predicted_SOIL_TEMP_10_poly.append(SOIL_TEMP_10_poly[val])
    predicted_SOIL_TEMP_20_poly.append(SOIL_TEMP_20_poly[val])
    predicted_SOIL_TEMP_50_poly.append(SOIL_TEMP_50_poly[val])
    predicted_SOIL_TEMP_100_poly.append(SOIL_TEMP_100_poly[val])

print('\nPolynomial regression RMSE:')
SUR_TEMP_error_poly=mean_squared_error(test_SUR_TEMP, predicted_SUR_TEMP_poly)
print(SUR_TEMP_error_poly)
SOIL_TEMP_5_error_poly=mean_squared_error(test_SOIL_TEMP_5, predicted_SOIL_TEMP_5_poly)
print(SOIL_TEMP_5_error_poly)
SOIL_TEMP_10_error_poly=mean_squared_error(test_SOIL_TEMP_10, predicted_SOIL_TEMP_10_poly)
print(SOIL_TEMP_10_error_poly)
SOIL_TEMP_20_error_poly=mean_squared_error(test_SOIL_TEMP_20, predicted_SOIL_TEMP_20_poly)
print(SOIL_TEMP_20_error_poly)
SOIL_TEMP_50_error_poly=mean_squared_error(test_SOIL_TEMP_50, predicted_SOIL_TEMP_50_poly)
print(SOIL_TEMP_50_error_poly)
SOIL_TEMP_100_error_poly=mean_squared_error(test_SOIL_TEMP_100, predicted_SOIL_TEMP_100_poly)
print(SOIL_TEMP_100_error_poly)

##############################################################################################
############                         MULTIPLE GAP SIZE                            ############
##############################################################################################

file_path='C:/Users/Julia/Documents/ITMO/Statistical_data_analysis/1_data_preparation/parsed_2018-2020/WI_Necedah_5_WNW.txt'
df=pd.read_csv(file_path, sep=' ', header=None)
SUR_TEMP=df[14]
SOIL_TEMP_5=df[23]
SOIL_TEMP_10=df[24]
SOIL_TEMP_20=df[25]
SOIL_TEMP_50=df[26]
SOIL_TEMP_100=df[27]
numbers=np.arange(len(SUR_TEMP))
plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt')
plt.ylim((-35,35))
plt.legend()
plt.show()

one_gap_genered_x=np.random.choice(range(0, 1000), 30, replace=False)
 
multiple_gap_genered_x=[]
for el in one_gap_genered_x:
    multiple_gap_genered_x.append(el)
    multiple_gap_genered_x.append(el+1)
    multiple_gap_genered_x.append(el+2)
#print(multiple_gap_genered_x)

test_SUR_TEMP=[]
test_SOIL_TEMP_5=[]
test_SOIL_TEMP_10=[]
test_SOIL_TEMP_20=[]
test_SOIL_TEMP_50=[]
test_SOIL_TEMP_100=[]

for val in multiple_gap_genered_x:
    test_SUR_TEMP.append(SUR_TEMP[val])
    SUR_TEMP[val]=-9999
    test_SOIL_TEMP_5.append(SOIL_TEMP_5[val])
    SOIL_TEMP_5[val]=-9999
    test_SOIL_TEMP_10.append(SOIL_TEMP_10[val])
    SOIL_TEMP_10[val]=-9999
    test_SOIL_TEMP_20.append(SOIL_TEMP_20[val])
    SOIL_TEMP_20[val]=-9999
    test_SOIL_TEMP_50.append(SOIL_TEMP_50[val])
    SOIL_TEMP_50[val]=-9999
    test_SOIL_TEMP_100.append(SOIL_TEMP_100[val])
    SOIL_TEMP_100[val]=-9999
    
print(test_SUR_TEMP)
index=np.where(np.array(test_SUR_TEMP)==-9999)
print(index)
multiple_gap_genered_x = np.delete(multiple_gap_genered_x, index)
#print(multiple_gap_genered_x)

test_SUR_TEMP = np.delete(test_SUR_TEMP, index)
print(test_SUR_TEMP)
test_SOIL_TEMP_5 = np.delete(test_SOIL_TEMP_5, index)
test_SOIL_TEMP_10 = np.delete(test_SOIL_TEMP_10, index)
test_SOIL_TEMP_20 = np.delete(test_SOIL_TEMP_20, index)
test_SOIL_TEMP_50 = np.delete(test_SOIL_TEMP_50, index)
test_SOIL_TEMP_100 = np.delete(test_SOIL_TEMP_100, index)

'''
print(multiple_gap_genered_x)
print(test_SUR_TEMP)
print(test_SOIL_TEMP_5)
print(test_SOIL_TEMP_10)
print(test_SOIL_TEMP_20)
print(test_SOIL_TEMP_50)
print(test_SOIL_TEMP_100)
'''

plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt\nGAPS_GENERATION')
plt.ylim((-35,35))
plt.legend()
plt.show()

SUR_TEMP_lin=fill_gaps_linear(SUR_TEMP, -9999)
SOIL_TEMP_5_lin=fill_gaps_linear(SOIL_TEMP_5, -9999)
SOIL_TEMP_10_lin=fill_gaps_linear(SOIL_TEMP_10, -9999)
SOIL_TEMP_20_lin=fill_gaps_linear(SOIL_TEMP_20, -9999)
SOIL_TEMP_50_lin=fill_gaps_linear(SOIL_TEMP_50, -9999)
SOIL_TEMP_100_lin=fill_gaps_linear(SOIL_TEMP_100, -9999)

plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP_lin, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5_lin, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10_lin, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20_lin, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50_lin, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100_lin, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt\nLINEAR_REGRESSION')
plt.ylim((-35,35))
plt.legend()
plt.show()

predicted_SUR_TEMP_lin=[]
predicted_SOIL_TEMP_5_lin=[]
predicted_SOIL_TEMP_10_lin=[]
predicted_SOIL_TEMP_20_lin=[]
predicted_SOIL_TEMP_50_lin=[]
predicted_SOIL_TEMP_100_lin=[]

for val in multiple_gap_genered_x:
    predicted_SUR_TEMP_lin.append(SUR_TEMP_lin[val])
    predicted_SOIL_TEMP_5_lin.append(SOIL_TEMP_5_lin[val])
    predicted_SOIL_TEMP_10_lin.append(SOIL_TEMP_10_lin[val])
    predicted_SOIL_TEMP_20_lin.append(SOIL_TEMP_20_lin[val])
    predicted_SOIL_TEMP_50_lin.append(SOIL_TEMP_50_lin[val])
    predicted_SOIL_TEMP_100_lin.append(SOIL_TEMP_100_lin[val])

print('\nLinear regression RMSE:')    
SUR_TEMP_error_lin=mean_squared_error(test_SUR_TEMP, predicted_SUR_TEMP_lin)
print(SUR_TEMP_error_lin)
SOIL_TEMP_5_error_lin=mean_squared_error(test_SOIL_TEMP_5, predicted_SOIL_TEMP_5_lin)
print(SOIL_TEMP_5_error_lin)
SOIL_TEMP_10_error_lin=mean_squared_error(test_SOIL_TEMP_10, predicted_SOIL_TEMP_10_lin)
print(SOIL_TEMP_10_error_lin)
SOIL_TEMP_20_error_lin=mean_squared_error(test_SOIL_TEMP_20, predicted_SOIL_TEMP_20_lin)
print(SOIL_TEMP_20_error_lin)
SOIL_TEMP_50_error_lin=mean_squared_error(test_SOIL_TEMP_50, predicted_SOIL_TEMP_50_lin)
print(SOIL_TEMP_50_error_lin)
SOIL_TEMP_100_error_lin=mean_squared_error(test_SOIL_TEMP_100, predicted_SOIL_TEMP_100_lin)
print(SOIL_TEMP_100_error_lin)

SUR_TEMP_poly=fill_gaps_poly(SUR_TEMP, -9999)
SOIL_TEMP_5_poly=fill_gaps_poly(SOIL_TEMP_5, -9999)
SOIL_TEMP_10_poly=fill_gaps_poly(SOIL_TEMP_10, -9999)
SOIL_TEMP_20_poly=fill_gaps_poly(SOIL_TEMP_20, -9999)
SOIL_TEMP_50_poly=fill_gaps_poly(SOIL_TEMP_50, -9999)
SOIL_TEMP_100_poly=fill_gaps_poly(SOIL_TEMP_100, -9999)

plt.rcParams['figure.figsize'] = [17, 6]
fig, ax = plt.subplots()
ax.plot(numbers, SUR_TEMP_poly, label='SUR_TEMP_DAILY_AVG')
ax.plot(numbers, SOIL_TEMP_5_poly, label='SOIL_TEMP_5_DAILY')
ax.plot(numbers, SOIL_TEMP_10_poly, label='SOIL_TEMP_10_DAILY')
ax.plot(numbers, SOIL_TEMP_20_poly, label='SOIL_TEMP_20_DAILY')
ax.plot(numbers, SOIL_TEMP_50_poly, label='SOIL_TEMP_50_DAILY')
ax.plot(numbers, SOIL_TEMP_100_poly, label='SOIL_TEMP_100_DAILY')
ax.grid()
ax.set(ylabel='Temperature, C',title='WV_Elkins_21_ENE.txt\nPOLYNOMIAL_REGRESSION')
plt.ylim((-35,35))
plt.legend()
plt.show()

predicted_SUR_TEMP_poly=[]
predicted_SOIL_TEMP_5_poly=[]
predicted_SOIL_TEMP_10_poly=[]
predicted_SOIL_TEMP_20_poly=[]
predicted_SOIL_TEMP_50_poly=[]
predicted_SOIL_TEMP_100_poly=[]

for val in multiple_gap_genered_x:
    predicted_SUR_TEMP_poly.append(SUR_TEMP_poly[val])
    predicted_SOIL_TEMP_5_poly.append(SOIL_TEMP_5_poly[val])
    predicted_SOIL_TEMP_10_poly.append(SOIL_TEMP_10_poly[val])
    predicted_SOIL_TEMP_20_poly.append(SOIL_TEMP_20_poly[val])
    predicted_SOIL_TEMP_50_poly.append(SOIL_TEMP_50_poly[val])
    predicted_SOIL_TEMP_100_poly.append(SOIL_TEMP_100_poly[val])

print('\nPolynomial regression RMSE:')
SUR_TEMP_error_poly=mean_squared_error(test_SUR_TEMP, predicted_SUR_TEMP_poly)
print(SUR_TEMP_error_poly)
SOIL_TEMP_5_error_poly=mean_squared_error(test_SOIL_TEMP_5, predicted_SOIL_TEMP_5_poly)
print(SOIL_TEMP_5_error_poly)
SOIL_TEMP_10_error_poly=mean_squared_error(test_SOIL_TEMP_10, predicted_SOIL_TEMP_10_poly)
print(SOIL_TEMP_10_error_poly)
SOIL_TEMP_20_error_poly=mean_squared_error(test_SOIL_TEMP_20, predicted_SOIL_TEMP_20_poly)
print(SOIL_TEMP_20_error_poly)
SOIL_TEMP_50_error_poly=mean_squared_error(test_SOIL_TEMP_50, predicted_SOIL_TEMP_50_poly)
print(SOIL_TEMP_50_error_poly)
SOIL_TEMP_100_error_poly=mean_squared_error(test_SOIL_TEMP_100, predicted_SOIL_TEMP_100_poly)
print(SOIL_TEMP_100_error_poly)