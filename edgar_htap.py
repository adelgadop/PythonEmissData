# modules
import numpy as np
import xarray as xr
import pandas as  pd
from matplotlib import pyplot as plt

# open NETCDF files
i_d01 = ['wrfchemi_00z_d01_ind' , 'wrfchemi_12z_d01_ind' ]
i_d02 = ['wrfchemi_00z_d02_ind' , 'wrfchemi_12z_d02_ind' ]
print(f"""Reading files:
{i_d01}
{i_d02}
""")

file_dir = '/Volumes/passport/Dissertation/data/wrfchemis/'
print(f"The path is {file_dir}")

def readnc(path = file_dir, file= i_d01[0]):
    fnc = path+file
    print('Reading ', fnc)
    ncfile = xr.open_dataset(fnc)
    return ncfile

ind_00z_d01 = readnc(file=i_d01[0])
ind_12z_d01 = readnc(file=i_d01[1])
ind_00z_d02 = readnc(file=i_d02[0])
ind_12z_d02 = readnc(file=i_d02[1])

# 36 species
emi_esp = ['E_CO'  , 'E_HCHO', 'E_C2H5OH', 'E_KET'  , 'E_NH3'  , 'E_XYL',
           'E_TOL' , 'E_ISO' , 'E_OLI'   , 'E_OLT'  , 'E_OL2'  , 'E_HC8',
           'E_HC5' , 'E_ORA2', 'E_ETH'   , 'E_ALD'  , 'E_CSL'  , 'E_SO2',
           'E_HC3' , 'E_NO2' , 'E_NO'    , 'E_CH3OH', 'E_PM25I', 'E_PM25J',
           'E_SO4I', 'E_SO4J', 'E_NO3I'  , 'E_NO3J' , 'E_ORGI' , 'E_ORGJ',
           'E_ECI' , 'E_ECJ' , 'E_SO4C'  , 'E_NO3C' , 'E_ORGC' , 'E_ECC']
print(f"We define species of emission rates as: \n {emi_esp}")

Dx = int(input("resolution in km for d01: "))
area = (int(input("nx: "))*Dx + int(input("ny: "))*Dx)
print("Choose a species:")
print(f"The area is {area} km^2")

def total_emi(pol = 'E_CO'):
    ind = (np.sum(ind_00z_d01[pol].values)*2)*365
    print("Emissions of "+pol+"   are: {:8.2f}".format(ind) +" mol km^-2 year^-1\n")

    if pol == 'E_CO':
        mol = 12+16
        print(f"Molecular weight of CO is {mol} g/mol")
        print("1 ton = 10^6 grams")
        co = (ind*mol*area/1E6).round(2)
        print(pol+" = {:8.2f}".format(co) +" tons year^-1\n")
        return co
    if pol == 'E_NO':
        mol = 14+16
        print(f"Molecular weight of NO is {mol} g/mol")
        print("1 ton = 10^6 grams")
        no = (ind*mol*area/1E6).round(2)
        print(pol+"   = {:8.2f}".format(no) +" tons year^-1\n")
        mol = 46
        print(f"Molecular weight of NO2 is {mol} g/mol")
        no2 = (ind*mol*area/1E6).round(2)
        nox = no+no2
        print("E_NO2 = {:8.2f}".format(no2) +" tons year^-1")
        print("E_NOx = {:8.2f}".format(nox) +" tons year^-1 \n")
        return nox

total_emi(pol = input("Choose a emi_esp: "))
total_emi(pol = input("Choose a emi_esp: "))
total_emi(pol = input("Choose a emi_esp: "))

SEEG_2010_ind = {'Pollutants':['CO','NOx'],
                'SP':[52218,8454],
                'RJ':[80786,13930],
                'ES':[44862,13558],
                'MG':[632831/2,39959/2],
                'Pa':[0,0]}
data = {'Pollutants':['CO','NOx'],
        'SEEG Ind (SP, 2010) [t]':[52218,8454],
        'SEEG Total (SP, 2010) [t]':[3109294,594283],
        'EDGAR Ind (D01, 2010) [t]':[total_emi('E_CO').round(2),total_emi('E_NO').round(2)]}
print(data)

fig, ax = plt.subplots(2,1, figsize=(6,8))
pd.DataFrame(data).set_index('Pollutants').T.plot.pie(subplots=True, ax = ax, legend=False)
plt.show()

print("""

#######
# End #
#######

""")
