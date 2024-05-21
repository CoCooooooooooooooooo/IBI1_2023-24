import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
  
# define dalys_data and use it to store the file data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")  

# my work
mydalys=dalys_data.iloc[0:110:10,3]
print(mydalys)

# Boolean
my_columns = [True, True, False, True]
E=dalys_data.iloc[0:3,my_columns]
print(E)

# create a Boolean to check if the row's entity is Afghanistan
AB=dalys_data.loc[dalys_data['Entity'] == 'Afghanistan', 'DALYs']
print(AB)

# 5.Examining the situation in China
# use china_data to store data we need
china_data=dalys_data.loc[dalys_data['Entity'] == 'China',['DALYs', 'Year'] ]
# select dalys data in China
dalys_value=china_data.loc[:,'DALYs']

# use numpy to get the mean of dalys in China
mean_dalys=np.mean(dalys_value)
print("the mean of dalys in China is",mean_dalys)
# select dalys data in China
latest_dalys = china_data.loc[1169,'DALYs']
print("the latest dalys in China is",latest_dalys)
# use Boolean function to test if dalys in 2019 is bigger than mean value
M=latest_dalys>mean_dalys
print(M)
print("dalys in 2019 is below the mean")

# b+ means blue symbol"+", r+ reprenet red symbol "+", bo represent blue dots
N=plt.plot(china_data.Year, china_data.DALYs, 'b+')
print(N)
plt.title('China DALYs Over Time')
plt.xlabel('Year')
plt.ylabel('DALYs')
# rotate the labels of xaxis clockwise 90 degree
plt.xticks(china_data.Year,rotation=-90)
plt.show()

dalys2019=dalys_data.loc[dalys_data['Year'] == 2019,['DALYs', 'Entity'] ]
under=dalys2019.loc[dalys2019['DALYs'] < 18000.00,'Entity']
print(under)
print("the places in the World where the DALYs in 2019 is less than 18,000 is Iceland, Israel, Japan, Singapore, South Korea and Switzerland")


