from PIL import Image
import math
import imageio
import numpy as np
import scipy.ndimage as img

def create_pattern_vertical (M, N, f):
  x ,y= np.meshgrid(np.linspace (0, N-1,N), np. linspace (M-1, 0, M))
  im =0.5*(np.sin(2* np.pi*f*x/(N-1)+0.5*np.pi*(N-1)) + 1)*255
  imageWrite (im, f'imv_{f}.png')
for f in [1,2,3,9]: 
  create_pattern_vertical (256,256,f)
