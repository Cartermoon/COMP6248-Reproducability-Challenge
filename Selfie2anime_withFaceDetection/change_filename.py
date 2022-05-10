import os




class BatchRename():
    '''批量重命名文件夹中的图片文件'''

    def __init__(self):
        self.path = './images1/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_sum = len(filelist)
        i = 1

        for item in filelist:
            # endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
            if item.endswith('.jpg'):
                # os.path.join 用于路径拼接，src为完整图片路径
                src = os.path.join(os.path.abspath(self.path), item)
                str1 = str(i)
                # Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
                # dst = os.path.join(os.path.abspath(self.path),str1.zfill(6)+'.jpg')
                dst = os.path.join(os.path.abspath(self.path), str1 + '.jpg')
                try:
                    os.rename(src, dst)
                    print('coverting %s to %s' % (src, dst))
                    i = i + 1
                except:
                    continue
            print('total %d to rename & converted %d jpgs' % (total_sum, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
