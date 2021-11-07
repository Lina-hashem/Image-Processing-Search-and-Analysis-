# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:13:59 2021

@author: Farizeh
"""

#from PIL import Image
from numpy import asarray
from scipy.ndimage import correlate
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as img
import timeit, functools
import imageio
  
  
# load the image and convert into
# numpy array

def imageread(imagename): 
    return imageio.imread(imagename)#.astype(arrtype)

    
# asarray() class is used to convert
# PIL images into NumPy arrays
img= imageread(r"asterix.png")
arrF = asarray(img)
  
# <class 'numpy.ndarray'
print(type(arrF))
  
#  shape
print(arrF.shape)
#put 'gray''seismic'... or dont put any thing to get it with color
plt.imshow(arrF/255,'spring')
plt.show()

    

def embossV1(arrF): #first method for embossing using nasted for loop
    M, N = arrF.shape
    arrG = np.zeros((M,N))
    for i in range(1,M-1):
        for j in range(1,N-1):
           arrG[i,j] = 128 + arrF[i+1,j+1] - arrF[i-1,j-1]
           arrG[i,j] = np.maximum(0, np.minimum(255, arrG[i,j]))
    return arrG
z= embossV1(arrF)  # call the function
plt.imshow(z)
plt.show()

def embossV2(arrF): #second method for embossing
     M, N = arrF.shape
     arrG = np.zeros((M,N))
     arrG[1:M-1,1:N-1] = 128 + arrF[2:,2:] - arrF[:-2,:-2]
     arrG = np.maximum(0, np.minimum(255, arrG))
     return arrG
h= embossV2(arrF)  #call function 
plt.imshow(h)
plt.show()

def embossV3(arrF): # third method using correlate
     mask = np.array([[-1, 0, 0],
                      [ 0, 0, 0],
                      [ 0, 0, +1]])
     arrG = 128 + correlate(arrF,mask,output=None,mode='reflect',cval=0.0,origin=0)
     arrG = np.maximum(0, np.minimum(255, arrG))
     return arrG           
l= embossV3(arrF)  # calling the function embossV3
plt.imshow(l)
plt.show()                      

def embossV4(arrF):
    arrG = 128 + arrF[2:,2:] - arrF[:-2,:-2]
    arrG[arrG< 0] = 0
    arrG[arrG>255] = 255
    return arrG
d= embossV4(arrF)
plt.imshow(d)
plt.show()

mtds = [embossV1, embossV2, embossV3, embossV4]
nRep = 5
nRun = 100
for mtd in mtds:
    ts = timeit.Timer(functools.partial(mtd, arrF)).repeat(nRep, nRun)
    print (min(ts) / nRun)
