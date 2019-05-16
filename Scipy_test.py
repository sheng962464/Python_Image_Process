from PIL import Image
from numpy import *
from scipy.ndimage import filters

im = array(Image.open('./素材/壁纸.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
