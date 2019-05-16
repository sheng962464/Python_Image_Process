from PIL import Image
from pylab import *


def test1():
    # 读取图像到数组中
    image_1 = array(Image.open('./素材/壁纸.jpg'))
    # 绘制图像
    imshow(image_1)
    # 一些点
    x = [100, 100, 400, 400]
    y = [200, 500, 200, 500]
    # 使用红色星状标记绘制点
    plot(x, y, 'r*')
    '''
    #############################################
    b   蓝色 blue
    g   绿色 green
    r   红色 red
    c   青色 cyan
    m   品红 magenta
    y   黄色 yellow
    k   黑色 black(取最后一个字母,避免与blue混淆)
    w   白色 white
    #############################################
    '-'     实线
    '--'    虚线
    ':'     点线
    #############################################
    '.'     点
    'o'     圆圈
    's'     正方形
    '*'     星号
    '+'     加号
    '×'     叉号
    #############################################
    '''
    # 绘制连接前两个点的线
    plot(x[:2], y[:2], 'ks:')
    # 添加标题，显示绘制的图像
    title('test:"example.jpg"')
    # 使坐标轴不显示
    # pylab.axis('off')
    show()


def test2():
    # 读取图像到数组中
    image_1 = array(Image.open('./素材/壁纸.jpg').convert('L'))
    # 新建一个图像
    figure()
    # 不使用颜色信息
    gray()
    # 在原点的左上角显示轮廓图像
    contour(image_1, origin='image')
    axis('equal')
    axis('off')
    # 绘制图片的直方图
    figure()
    # hist()只接受一维数组作为输入，在绘制直方图之前，必须先对图像进行压平处理
    # flatten()将任意数组按照行优先准则转换成一维数组
    # hist()的第二个参数指定小区间的数目。
    # 用一定数目的小区间(bin)来指定表征像素的范围，每个小区间会得到落入该小区间表示范围的像素数目。
    hist(image_1.flatten(), 128)
    show()

def test3():
    # 交互式标注，使用ginput()函数
    image_1 = array(Image.open('./素材/壁纸.jpg'))
    imshow(image_1)
    print('Please click 3 points')
    x = ginput(3)
    # 等待用户在绘图窗口的图像区域点击三次
    #  程序将这些点击的图标(x,y)自动保存在x列表里
    print('you clicked:',x)
    show()


if __name__ == '__main__':
    test3()
