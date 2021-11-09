import numpy as np
import Img as img


def downsample(arrF, m, n):
    arrG = np.copy(arrF)
    arrG = arrG[slice(None, None, m), slice(None, None, n)]
    return arrG


def upsample(arrF, m, n):
    arrO = np.ones((m, n))
    arrG = np.kron(arrF, arrO)
    return arrG


arrF = img.imageRead('portrait.png')
arrG = upsample(downsample(arrF, 2, 2), 2, 2)
img.imageWrite(arrG, 'upsample_2x2.png')

arrF = img.imageRead('portrait.png')
arrG = upsample(downsample(arrF, 4, 4), 4, 4)
img.imageWrite(arrG, 'upsample_4x4.png')

arrF = img.imageRead('portrait.png')
arrG = upsample(downsample(arrF, 8, 8), 8, 8)
img.imageWrite(arrG, 'upsample_8x8.png')