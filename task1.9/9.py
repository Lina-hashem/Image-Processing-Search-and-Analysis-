from PIL import Image
import math
import imageio
import numpy as np
import scipy.ndimage as img

def imageWrite(arrF, imgname, arrtype=np.uint8):
  imageio.imwrite(imgname, arrF.astype(arrtype))
  
def imageRead(imgname, pilmode='L', arrtype=np.float):
  return imageio.imread(imgname, pilmode=pilmode).astype(arrtype)

def create_pattern_horizontal(M, N, f):
  x,y = np. meshgrid(np.linspace (0, N-1,N),np. linspace (M-1, 0, M))
  im =0.5*(np.exp(-4/M*y)*np.sin(2*math.pi*f*y/(M-1)+0.5*math.pi*(M-1))+1)*255
  imageWrite(im,f'imh_{f}.png')
for f in [5,9,11,13]: 
  create_pattern_horizontal(256, 256, f)
