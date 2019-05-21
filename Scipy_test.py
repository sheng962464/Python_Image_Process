from PIL import Image
from numpy import *
from scipy.ndimage import filters

def test1():
    im = array(Image.open('./素材/壁纸.jpg').convert('L'))
    im2 = filters.gaussian_filter(im,5)

def test2():
    im = array(Image.open('empire.jpg'))
    im2 = zeros(im.shape)
    for i in range(3):
        im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
        im2 = uint8(im2)