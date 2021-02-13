# -*- coding: utf-8 -*-
"""
BARNSLEY FERN

By: it's literally monique
"""

# import libraries needed for program
import matplotlib.pyplot as plt 
from random import randint 
  
#initialize list & set first values to 1
x = [0] 
y = [0] 

# create the barnsley fractal by creating the points on the scatterplot
for i in range(0, 50000): 
  
    z = randint(1, 100) 
      
    if z == 1: 
        x.append(0) 
        y.append(0.16*(y[i])) 
         
    if z>= 2 and z<= 86: 
        x.append(0.85*(x[i]) + 0.04*(y[i])) 
        y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) 
      
    if z>= 87 and z<= 93: 
        x.append(0.2*(x[i]) - 0.26*(y[i])) 
        y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 
          
    if z>= 94 and z<= 100: 
        x.append(-0.15*(x[i]) + 0.28*(y[i])) 
        y.append(0.26*(x[i]) + 0.24*(y[i])+0.44) 

# make and show the scatterplot
plt.scatter(x, y, s = 0.2, edgecolor ='#5dbb63') 

plt.show()