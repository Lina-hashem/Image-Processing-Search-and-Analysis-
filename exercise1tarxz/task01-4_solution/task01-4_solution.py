import numpy as np
import exercise1tarxz.Img as img

arrF = img.imageRead(imgname='asterix.png', pilmode='L')
arrG = img.imageRead(imgname='portrait.png', pilmode='L')

arrH = np.copy(arrF)
print(arrF.shape)

print(arrF[100:,200:].shape)
a = arrH[100:,200:]
arrH[100:356, 200:456] = arrG

img.imageWrite(arrH, 'Final_1.4.png')

