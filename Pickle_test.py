# pickle 模块可以接受几乎所有的 Python 对象，并且将其转换成字符串表示，该过程叫做封装（pickling）。
# 从字符串表示中重构该对象，称为拆封（unpickling）。这些字符串表示可以方便地存储和传输。

# 保存均值和主成分数据
import pickle
from PIL import Image
from numpy import *
from pylab import *
import ImageTools
imlist = []
im = array(Image.open(imlist[0])) # 打开一幅图像，获取其大小
m,n = im.shape[0:2] # 获取图像的大小
imnbr = len(imlist) # 获取图像的数目
# 创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten()
for im in imlist],'f')
# 执行 PCA 操作
V,S,immean = ImageTools.pca(immatrix)
# 显示一些图像（均值图像和前 7 个模式）
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))
    show()

# 保存上一节字体图像的平均图像和主成分
f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean,f)
pickle.dump(V,f)
f.close()


# 载入均值和主成分数据
f = open('font_pca_modes.pkl', 'rb')
immean = pickle.load(f)
V = pickle
f.close()

