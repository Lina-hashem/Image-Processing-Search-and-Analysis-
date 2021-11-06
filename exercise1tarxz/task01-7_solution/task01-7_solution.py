import numpy as np
import exercise1tarxz.Img as img


# ringmask function form the lecture
def ringmask(arrF, c, rmin, rmax):
    M, N = arrF.shape
    arrG = np.copy(arrF)
    rmin2 = rmin ** 2
    rmax2 = rmax ** 2
    rs, cs = np.meshgrid(np.arange(M), np.arange(N), indexing='ij')
    dist2 = (rs - c[0]) ** 2 + (cs - c[1]) ** 2
    bmask = (dist2 >= rmin2) & (dist2 <= rmax2)
    arrG[bmask] = 255
    return arrG


# read image into a numpy array
arrF = img.imageRead(imgname='portrait.png', pilmode='L')
# divide the image into 16 blocks and start at center point 32,32
cntr = (np.array(arrF.shape) / 16) + (16, 16)
# not sure if even here we are not allowed to use loops :)
# work on the 16 Blocks in the image
i, j = 0, 0
for i in range(5):
    for j in range(5):
        arrF = ringmask(arrF, cntr, 0, 32)
        cntr += (0, 64)  # move horizontally to the next block (64 = 32 + 32 radius)
    cntr = (np.array(arrF.shape) / 16) + (16, 16)
    cntr += (64 * i, 0) # move vertically to the next block (64 = 32 + 32 radius)
img.imageWrite(arrF, 'ringmask_intermediateStage.png')
mask = np.equal(arrF, 255) # set all white pixels to true
arrG = img.imageRead(imgname='portrait.png', pilmode='L')
arrG[~mask] = 255 # using the inverse of ringmask_intermediateStage set the true pixels (edges) to 255
img.imageWrite(arrG, 'ringmask_Final.png')
