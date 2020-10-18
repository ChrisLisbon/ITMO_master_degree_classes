# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:56:42 2020

@author: Julia
"""

import requests
import pandas as pd
import os

output_folder='C://Users/Julia/Documents/ITMO/Statistical_data_analysis/hourly02_2019'
incorrect_stations=[]


stations_df=pd.read_csv('C://Users/Julia/Documents/ITMO/Statistical_data_analysis/stations.tsv', sep='\t', header = None)
incorrect_stations=['CRNH0203-2019-NM_Dulce_1_NW.txt', 'CRNH0203-2019-CO_Grand_Junction_9_W.txt', 'CRNH0203-2019-AZ_Holbrook_17_ESE.txt', 'CRNH0203-2019-CO_Eads_16_ENE.txt', 'CRNH0203-2019-CO_Saguache_2_WNW.txt', 'CRNH0203-2019-NM_Reserve_1_W.txt', 'CRNH0203-2019-UT_Tropic_9_SE.txt', 'CRNH0203-2019-NM_Carrizozo_1_W.txt', 'CRNH0203-2019-CO_Stratton_24_N.txt', 'CRNH0203-2019-CO_Center_A_4_SSW.txt', 'CRNH0203-2019-AZ_Bowie_23_SSE.txt', 'CRNH0203-2019-CO_Springfield_6_WSW.txt', 'CRNH0203-2019-NM_Santa_Fe_20_WNW.txt', 'CRNH0203-2019-CO_Woodland_Park_14_WSW.txt', 'CRNH0203-2019-CO_Rocky_Ford_1_ESE.txt', 'CRNH0203-2019-NM_Taos_27_NW.txt', 'CRNH0203-2019-CO_Kim_9_WSW.txt', 'CRNH0203-2019-NM_Raton_26_ESE.txt', 'CRNH0203-2019-CO_Genoa_35_N.txt', 'CRNH0203-2019-NM_Clayton_3_ENE.txt', 'CRNH0203-2019-NM_Mills_6_WSW.txt', 'CRNH0203-2019-CO_Rifle_23_NW.txt', 'CRNH0203-2019-NM_Mountainair_2_WSW.txt', 'CRNH0203-2019-CO_Eagle_13_SSE.txt', 'CRNH0203-2019-CO_Craig_30_N.txt', 'CRNH0203-2019-UT_Provo_22_E.txt', 'CRNH0203-2019-AK_Utqiaġvik_formerly_Barrow_4_ENE.txt', 'CRNH0203-2019-SA_Tiksi_4_SSE.txt', 'CRNH0203-2019-NM_Artesia_2_WNW.txt', 'CRNH0203-2019-NM_Grants_2_S.txt', 'CRNH0203-2019-UT_Bluff_32_NW.txt', 'CRNH0203-2019-CO_Buena_Vista_2_SSE.txt', 'CRNH0203-2019-AZ_Amado_23_W.txt', 'CRNH0203-2019-CO_Colorado_Springs_23_NW.txt', 'CRNH0203-2019-NM_Clovis_7_N.txt', 'CRNH0203-2019-NM_Ramah_9_SE.txt', 'CRNH0203-2019-UT_Monticello_24_NW.txt', 'CRNH0203-2019-AZ_Tsaile_1_SSW.txt', 'CRNH0203-2019-UT_Blanding_26_SSW.txt', 'CRNH0203-2019-UT_Cedar_City_18_SSE.txt', 'CRNH0203-2019-UT_Mexican_Hat_10_NW.txt', 'CRNH0203-2019-NM_Hagerman_10_ESE.txt', 'CRNH0203-2019-NM_Vaughn_36_SSE.txt', 'CRNH0203-2019-NM_Aztec_43_E.txt', 'CRNH0203-2019-AZ_Whiteriver_A_1_SW.txt', 'CRNH0203-2019-NM_Elida_14_SW.txt', 'CRNH0203-2019-UT_Spanish_Valley_25_SW.txt', 'CRNH0203-2019-NM_Las_Vegas_6_NE.txt', 'CRNH0203-2019-NM_Hachita_7_ESE.txt', 'CRNH0203-2019-NM_Pinon_8_SSE.txt', 'CRNH0203-2019-AZ_Phoenix_7_S.txt', 'CRNH0203-2019-AZ_Cameron_25_SSE.txt', 'CRNH0203-2019-AZ_Camp_Verde_3_N.txt', 'CRNH0203-2019-AZ_Coolidge_5_W.txt', 'CRNH0203-2019-NM_Socorro_17_WSW.txt', 'CRNH0203-2019-AZ_Page_9_WSW.txt', 'CRNH0203-2019-UT_Delta_4_NE.txt', 'CRNH0203-2019-UT_St._George_15_NE.txt', 'CRNH0203-2019-UT_Midway_3_NE.txt', 'CRNH0203-2019-AZ_Ajo_29_S.txt', 'CRNH0203-2019-AZ_Kayenta_16_WSW.txt', 'CRNH0203-2019-AZ_Heber_3_SE.txt', 'CRNH0203-2019-UT_Milford_42_WNW.txt', 'CRNH0203-2019-AZ_Lake_Havasu_City_19_SE.txt', 'CRNH0203-2019-NM_Nageezi_18_SSW.txt', 'CRNH0203-2019-UT_Price_3_E.txt', 'CRNH0203-2019-AZ_Gila_Bend_3_ENE.txt', 'CRNH0203-2019-AZ_Kingman_8_NE.txt', 'CRNH0203-2019-AZ_Safford_5_NNE.txt', 'CRNH0203-2019-AZ_Fredonia_7_SSE.txt', 'CRNH0203-2019-AZ_Meadview_7_N.txt', 'CRNH0203-2019-UT_Beaver_15_E.txt', 'CRNH0203-2019-OH_Coshocton_8_NNE.txt', 'CRNH0203-2019-AL_Guntersville_2_SW.txt', 'CRNH0203-2019-CO_Akron_A_4_E.txt', 'CRNH0203-2019-CO_Meeker_15_W.txt', 'CRNH0203-2019-UT_Vernal_23_SSE.txt', 'CRNH0203-2019-UT_Grantsville_12_WNW.txt', 'CRNH0203-2019-UT_Manila_18_ESE.txt', 'CRNH0203-2019-VA_Sterling_0_N.txt', 'CRNH0203-2019-TN_Oakridge_0_N.txt']


for index, row in stations_df.iterrows():
    prefix='CRNH0203-2019-'
    file_name=(prefix+row[2]+'_'+row[3]+'_'+row[4]+'.txt').replace(' ', '_')
    if file_name not in incorrect_stations:
        with open ('C://Users/Julia/Documents/ITMO/Statistical_data_analysis/valid_stations.csv', 'a') as file:
            file.write(str(row[0])+';'+str(row[1])+';'+str(row[2])+';'+str(row[3])+';'+str(row[4])+';'+str(row[5])+';'+str(row[6])+';'+str(row[7])+';'+str(row[8])+';'+str(row[9])+';'+str(row[10])+';'+str(row[11])+';'+str(row[12])+';'+str(row[13])+';'+str(row[14])+';'+str(row[15])+'\n')
    
    '''
    print('Collecting data:')
    print(file_name)
    
    url = 'https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2019/'
    
    try:
        r = requests.get(url+file_name, allow_redirects=True)
        if r.status_code==404:
            print ('This station is not in hourly02 dataset')
            incorrect_stations.append(file_name)
            pass
        else:
            print ('Downloading...')
            with open (os.path.join(output_folder, file_name), 'wb') as file:
                file.write(r.content)
        
    except Exception as e:
        print ('Server error:')
        print(e)
        incorrect_stations.append(file_name)
     
print('Proccess finished')
print('Incorrect stations:')
print(incorrect_stations)
'''   

        