from PIL import Image
from numpy import *


def GetImageList(FolderPath):
    List_Of_File = []
    if (os.path.isdir(FolderPath)):
        for file in os.listdir(FolderPath):
            List_Of_File.append(os.path.join(FolderPath, file))


def imresize(image, size):
    '''使用PIL对象重新定义图像数组的大小'''
    pil_im = Image.fromarray(uint8(image))
    return array(pil_im.resize(size))


def histeq(im, nbr_bins=256):
    '''
    对一幅灰度图像进行直方图均衡化
    该函数有两个输入参数，一个是灰度图像，一个是直方图中使用小区间的数目。
    '''
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()  # cumulative distribution function
    cdf = 255 * cdf / cdf[-1]  # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf
