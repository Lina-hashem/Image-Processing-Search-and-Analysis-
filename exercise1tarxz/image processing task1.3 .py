# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:41:15 2021

@author: Farizeh
"""

from numpy import asarray
from scipy.ndimage import correlate
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as img
import timeit, functools
import imageio
import matplotlib

  
# load the image and convert into
# numpy array
#imagename= C:\Users\Farizeh\Downloads\Imagr processing exercise\portrait.png
def imageread(imagename, pilmode='RGB'): 
    return imageio.imread(imagename,pilmode='RGB')#.astype(arrtype)

    
# asarray() class is used to convert
# PIL images into NumPy arrays
img= imageread(r"asterixRGB.png",'RGB')
arrF = asarray(img)
  
print(type(arrF))
  
#  shape
print(arrF.shape)
plt.imshow(arrF/255)
plt.show()
#copy 
arrG = np.copy(arrF)

arrG[:,:,0] = 0
plt.imshow(arrG)
plt.show


from PIL import Image
im = Image.fromarray(arrG)
im.save("your_file.png")