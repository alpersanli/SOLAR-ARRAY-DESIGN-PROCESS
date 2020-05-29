import math

#SOLAR ARRAY DESIGN PROCESS


#Steps


#1) Determine requirements and constraints for power subsystem solar array design
# Avarage power required during daylight and eclipse      =110 W during daylight and eclipse
# Orbit altitude and eclipse duration     =700 km
# Design lifetime     =5 years
# Id = inherit degradation
# teta = the Sun incidence angle
# Ld = life degradation
# Xe and Xd = the efficiencies of the power distribution paths


#2) Calculate amount of power that must be produced by the solar arrays, Psa
Pe = Pd = 110   # [W]
Te = 35.3   # [min] the time of eclipse
Td = 63.5   # [min] the time of daylight
# Assume a peak power tracking regulation scheme with...
Xe = 0.6
Xd = 0.8
Psa = (((Pe * Te) / Xe) + ((Pd * Td) / Xd)) / Td   # [W]


#3) Select type of solar cell and  estimate power output, Po with the Sun normal to the surface of the cells
#   Si solar cells = Si
#   GaAs solar cells = Ga
#   Multijunction solar cells = Mj
#   XTE-HF High Fluence, Triple Junction Solar Cell = XTEHF
# Typical demonstrated efficiencies for Si, GaAs multijunction and XTE-HF High Fluence solar cells are 14.8 % , 18.5 % , 28 % and 32.1 % respectively.
print("-----Solar Cell-----")
print("Si = Si\nGaAs = Ga \nMultijunction = Mj \nXTE-HF High Fluence = XTE-HF ")
print("-----Po Values-----")
Po1 = 0.148 * 1368  #for Si [W/m^2]
Po2 = 0.185 * 1368  #for Ga [W/m^2]
Po3 = 0.28 * 1368  #for Mj [W/m^2]
Po4 = 0.321 * 1368  #for XTEHF [W/m^2]
print("Si Po = {} [W/m^2] \nGa Po = {} [W/m^2] \nMj Po = {} [W/m^2] \nXTE-HF Po = {} [W/m^2] ".format(Po1,Po2,Po3,Po4))


#4) Determine the beginning of life (BOL) power production capability, Pbol for the solar array
Id = 0.77
Teta = 23.5 #[deg]
print("-----Pbol Values-----")
Pbol1 = Po1 * Id * (math.cos(math.pi * 0.1305555556))    # [W/m^2] , [math.cos(math.pi*0.1305555556)=cos(23.5) degree]
Pbol2 = Po2 * Id * (math.cos(math.pi * 0.1305555556))
Pbol3 = Po3 * Id * (math.cos(math.pi * 0.1305555556))
Pbol4 = Po4 * Id * (math.cos(math.pi * 0.1305555556))
print("Si Pbol = {} [W/m^2] \nGa Pbol = {} [W/m^2] \nMj Pbol = {} [W/m^2] \nXTE-HF Pbol = {} [W/m^2] ".format(Pbol1,Pbol2,Pbol3,Pbol4))


#5) Determine the end of life (EOF) power production capability, Peol for the solar array
#   Si D: 3.75 % per yr
#   GaAs D: 2.75 % per yr
#   Triple Junction D: 0.5 % per yr
#   XTE-HF D: 0.093 % per yr
D1 = 3.75 / 100
D2 = 2.75 / 100
D3 = 0.5 / 100
D4 = 0.0056    #((32.1/100)-(23.7/100))/15  (BOL-EOL)/15Years
L = 5   # [years]
print("-----Ld Values-----")
Ld1 = (1 - D1)**L
Ld2 = (1 - D2)**L
Ld3 = (1 - D3)**L
Ld4 = (1 - D4)**L
print("Si Ld = {} [for 5 years] \nGa Ld = {} [for 5 years] \nMj Ld = {} [for 5 years] \nXTE-HF Ld = {} [for 5 years] ".format(Ld1,Ld2,Ld3,Ld4))
print("-----Peol Values-----")
Peol1 = Pbol1 * Ld1
Peol2 = Pbol2 * Ld2
Peol3 = Pbol3 * Ld3
Peol4 = Pbol4 * Ld4
print("Si Peol = {} [W/m^2] \nGa Peol = {} [W/m^2] \nMj Peol = {} [W/m^2] \nXTE-HF Peol = {} [W/m^2] ".format(Peol1,Peol2,Peol3,Peol4))


#6) Estimate the solar array area, Asa required to produce the necessary power, Psa based on Peol an alternate approach
print("-----Psa Values-----")
Asa1 = Psa / Peol1
Asa2 = Psa / Peol2
Asa3 = Psa / Peol3
Asa4 = Psa / Peol4
print("Si Asa = {} [m^2] \nGa Asa = {} [m^2] \nMj Asa = {} [m^2] \nXTE-HF Asa = {} [m^2] ".format(Asa1,Asa2,Asa3,Asa4))
