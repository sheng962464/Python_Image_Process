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
    '''cumulative distribution function
    对一幅灰度图像进行直方图均衡化
    该函数有两个输入参数，一个是灰度图像，一个是直方图中使用小区间的数目。
    '''
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins)
    cdf = imhist.cumsum()  # cumulative distribution function
    cdf = 255 * cdf / cdf[-1]  # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


def compute_average(imlist):
    """
    计算图像列表的平均图像
    图像平均操作是减少图像噪声的一种简单方式，通常用于艺术特效。
    假设所有的图像具有相同的大小，我们可以将这些图像简单地相加，然后除以图像的数目，来计算平均图像。
    """

    # 打开第一幅图像，将其存储在浮点型数组中
    averageim = array(Image.open(imlist[0]), 'f')
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname + '...skipped')
    averageim /= len(imlist)
    # 返回 uint8 类型的平均图像
    return array(averageim, 'uint8')


def pca(X):
    """ 主成分分析：Principal Component Analysis
    输入：矩阵 X，其中该矩阵中存储训练数据，每一行为一条训练数据
    返回：投影矩阵（按照维度的重要性排序）、方差和均值
    """
    # 获取维数
    num_data,dim = X.shape
    # 数据中心化
    mean_X = X.mean(axis=0)
    X = X - mean_X
    if dim>num_data:
        # PCA- 使用紧致技巧
        M = dot(X,X.T) # 协方差矩阵
        e,EV = linalg.eigh(M) # 特征值和特征向量
        tmp = dot(X.T,EV).T # 这就是紧致技巧
        V = tmp[::-1] # 由于最后的特征向量是我们所需要的，所以需要将其逆转
        S = sqrt(e)[::-1] # 由于特征值是按照递增顺序排列的，所以需要将其逆转
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        # PCA- 使用 SVD 方法
        U,S,V = linalg.svd(X)
        V = V[:num_data] # 仅仅返回前 nun_data 维的数据才合理
        # 返回投影矩阵、方差和均值
    return V,S,mean_X