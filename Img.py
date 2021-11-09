import imageio
import numpy as np
import scipy.ndimage as img


def imageRead(imgname, pilmode='L', arrtype=np.float):
    """
    read an image file into a numpy array
    imgname: str
    name of image file to be read
    pilmode: str
    for luminance / intesity images use ’L’
    for RGB color images use ’RGB’
    arrtype: numpy dtype
    use np.float, np.uint8, ...
    """

    return imageio.imread(imgname, pilmode=pilmode).astype(arrtype)


def imageWrite(arrF, imgname, arrtype=np.uint8):
    """
    write a numpy array as an image file
    the file type is inferred from the suffix of parameter imgname, e.g. ’.png’
    arrF: array_like
    array to be written
    imgname: str
    name of image file to be written
    arrtype: numpy dtype
    use np.uint8, ...
    """
    imageio.imwrite(imgname, arrF.astype(arrtype))
