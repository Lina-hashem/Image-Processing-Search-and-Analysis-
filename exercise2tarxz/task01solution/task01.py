import numpy as np
import Img as img


def downsample(arrF, m=2, n=2):
    arrG = np.copy(arrF)
    arrG = arrG[slice(None, None, m), slice(None, None, n)]
    return arrG


arrF = img.imageRead('portrait.png')
arrG = downsample(arrF, 4, 4)  # keep only every m-th row and every n-th to reduce resolution
img.imageWrite(arrG,'Final_32x32.png')
arrG = downsample(arrF, 8, 8)  # keep only every m-th row and every n-th to reduce resolution
img.imageWrite(arrG,'Final_64x64.png')
