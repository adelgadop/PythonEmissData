# PythonEmissData
This repository contents Jupyter Notebooks files useful to process information related to `fleet features`, `use intensity` and `road length`.

`fleet features` and `use intensity` are processing in *Fleet and Use intensity.ipynb*. There are details about how we can process information to get useful data to feed to `wrfchemi_cbmz_fc.ncl` based on emissions pre-processor model [Andrade et al. 2015](https://www.frontiersin.org/articles/10.3389/fenvs.2015.00009/full). Here, I'm considering emission factors based on field experiment, mainly by [Pérez-Martinez et al. (2014)](https://link.springer.com/article/10.1007/s13762-014-0562-7) and by [Andrade et al. 2015](https://www.frontiersin.org/articles/10.3389/fenvs.2015.00009/full), shown as following:

```
&fator_emissao    ! VEIC 1,  VEIC 2,  VEIC 3,  VEIC4A,  VEIC4B,  VEIC4C,  VEIC 5,  VEIC6A,  VEIC6B
 exa_co           = 5.8000,  12.000,  5.8000,  3.6000,  3.6000,  3.6000,  0.0000,  9.1500,  9.0200,
 exa_co2          = 219.00,  219.00,  219.00,  1422.0,  1422.0,  1422.0,  0.0000,  0.0000,  0.0000,
 exa_nox          = 0.3000,  1.1200,  0.3000,  9.2000,  9.2000,  9.2000,  0.0000,  0.1320,  0.1290,
 exa_so2          = 0.0290,  0.0140,  0.0210,  0.6100,  0.6100,  0.6100,  0.0000,  0.0097,  0.0093,
 exa_c2h5oh       = 0.5080,  0.2500,  0.5080,  0.6100,  0.6100,  0.6100,  0.0000,  0.0790,  0.3050,
 exa_hcho         = 0.0089,  0.0110,  0.0098,  0.6100,  0.6100,  0.6100,  0.0000,  0.0152,  0.0155,
 exa_ald          = 0.0140,  0.0300,  0.0220,  0.6100,  0.6100,  0.6100,  0.0000,  0.0164,  0.0188,
 exa_pm           = 0.0200,  0.0200,  0.0200,  0.2770,  0.2770,  0.2770,  0.0000,  0.0500,  0.0500,
 exa_voc          = 0.4250,  1.3000,  0.4340,  2.0500,  2.0500,  2.0500,  0.0000,  1.0800,  1.0800,
 vap_voc          = 0.2300,  0.2500,  0.2400,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,  0.0000,
 liq_voc          = 2.0000,  1.5000,  1.7500,  0.0000,  0.0000,  0.0000,  0.0000,  1.2000,  1.2000,
```

Where `VEIC` corresponds a specific type of vehicle and his fuel use:

* Light-duty vehicles (LDV): VEIC 1 (gasohol fuel), VEIC 2 (ethanol fuel), and VEIC 3 (Flex Gasohol and Ethanol fuel).
* Heavy-duty vehicles (HDV): VEIC4A (trucks diesel fuel), VEIC4B (urban bus, diesel fuel), VEIC4C (articulated urban bus, diesel fuel).
* Motorcycle (MC): VEIC6A (gasohol fuel), VEIC6B (Flex-G and Flex-Eth fuel).
* Others: VEIC 5 that represents taxis with fuel consumption of natural gas.

The second file *Road_Length.ipynb* is useful to process the output file from QGIS in `*.csv` format to `*.txt`.

