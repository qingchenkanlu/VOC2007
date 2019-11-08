# coding=utf-8
import os  # 打开文件时需要
# from PIL import Image
import re


class BatchRename():
    def __init__(self):
        # 我的图片文件夹路径
        self.path = '/home/yusheng/data/processed/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 10000  # 图片编号从多少开始，不要跟VOC原本的编号重复了
        n = 6
        for item in filelist:
            if item.endswith('.jpg'):
                n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0) * n + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print 'converting %s to %s ...' % (src, dst)
                    i = i + 1
                except:
                    continue
        print 'total %d to rename & converted %d jpgs' % (total_num, i)


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
