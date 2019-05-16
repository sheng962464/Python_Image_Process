from PIL import Image

# 读取图片
image_1 = Image.open('./素材/壁纸.jpg')
print(image_1.size)
print(image_1.mode)
# show的标准版本效率不高，因为它将图像保存到临时文件并调用xv工具显示图像。
# 如果你没有安装xv，它甚至不会工作。 它对于调试和测试非常方便。
image_1.show()
# 图像的颜色转换
# 常见模式为灰度图像为“L”（亮度），真彩色图像为“RGB”，印刷四色为“CMYK”。
image_2 = Image.open('./素材/壁纸.jpg').convert('L')
# 图像的保存
image_2.save('./输出结果/壁纸convert.png')
# 创建文件的缩略图
image_3 = Image.open('./素材/壁纸.jpg')
image_3.thumbnail((500, 500))
image_3.save('./输出结果/壁纸thumbnail.jpg')
# 裁剪指定区域
image_4 = Image.open('./素材/壁纸.jpg')
box = (100, 100, 400, 400)  # 四元组的坐标依次是(左,上,右,下)
region = image_4.crop(box)  # region也是一个图片对象
region.save('./输出结果/壁纸region.jpg')
region = region.transpose(Image.ROTATE_180)
# 当粘贴区域时，区域的大小必须完全匹配。
# 但是模式不需要匹配。模式不匹配时会在粘贴之前自动转换。
image_4.paste(region, box)  # 将region放回image_4中去
image_4.save('./输出结果/壁纸crop.jpg')
# 指定图像的大小
image_5 = image_1.resize((500, 500))
image_5.save('./输出结果/壁纸resize.jpg')
'''
resize()与thumbnail()的区别:
原图片的尺寸为 (3833 * 1440)
resize()后图片尺寸为 (500 * 500)
thumbnail()后图片尺寸为 (500 * 187) 等比例缩放
'''
# 图像旋转，逆时针方向
image_6 = image_1.rotate(45)
image_6.save('./输出结果/壁纸rotate.jpg')
