from numpy import *
import pylab
from PIL import Image


def test1():
    # 图像通常被编码成无符号的八位整数(uint8)
    im = array(Image.open('./素材/壁纸.jpg'))
    print(im.shape, im.dtype)
    # 对图像进行灰度化处理，并在创建数组时使用额外的参数"f"
    # 灰度图像没有颜色信息，所以在形状元组中，只有两个数值
    im = array(Image.open('./素材/壁纸.jpg').convert('L'), 'f')
    print(im.shape, im.dtype)


def test2():
    im1 = array(Image.open('./素材/壁纸.jpg').convert('L'))
    im2 = 255 - im1  # 对图像进行反处理
    im3 = (100.0 / 255) * im1 + 100  # 将图像的像素值变换到(100,200)的区间
    im4 = 255 * (im1 / 255.0) ** 2  # 对图像像素值求平方后得到的图像
    # pylab.figure()
    # pylab.gray()
    # pylab.contour(im1,origin = 'image')
    # pylab.show()
    print(int(im1.min()), int(im1.max()))
    # array()变换的相反操作可以使用PIL的fromarray()函数完成
    # 如果你不确定数据的类型，安全起见，应该先转换回来
    pil_im1 = Image.fromarray(uint8(im1))
    pil_im1.save('./素材/壁纸fromarray.jpg')

def test3():
    # 直方图均衡化
    # 直方图均衡化是指将一幅图像的灰度直方图变平，使变换后的图像中每个灰度值的分布概率都相同。
    # 在对图像做进一步处理之前，直方图均衡化通常是对图像灰度值进行归一化的一个非常好的方法，并且可以增强图像的对比度。
    # 直方图均衡化的变换函数是图像中像素值的累积分布函数
    # 简写为 cdf，将像素值的范围映射到目标范围的归一化操作
    pass


if __name__ == '__main__':
    test2()
