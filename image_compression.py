# -*- coding: utf-8 -*-

"""脚本功能说明：使用 tinypng api先无损压缩，然后再resize指定压缩大小"""
from PIL import Image
import os, shutil
import os
import sys
import tinify


#tinify.key = "在此处输入你的API—key"
tinify.key = "VrxjpkJ02mzz84Zx70nCZz6yYqyXnh6Y"

def get_file_dir(file):
    """获取文件目录通用函数"""
    fullpath = os.path.abspath(os.path.realpath(file))
    return os.path.dirname(fullpath)


def check_suffix(file_path):
    """检查指定文件的后缀是否符合要求"""
    file_path_lower = file_path.lower()
    return (file_path_lower.endswith('.png')
            or file_path_lower.endswith('.jpg')
            or file_path_lower.endswith('.jpeg'))


def compress_by_tinypng(input_file,size,tag):
    """使用 tinypng 进行压缩，中文前面的 u 是为了兼容 py2.7"""
    if not check_suffix(input_file):
        print(u'只支持png\\jpg\\jepg格式文件：' + input_file)
        return
    size=int(size)*1024
    file_name = os.path.basename(input_file)

    target_size = os.path.getsize(input_file)
    while (target_size > size):
        if(tag==1):
            tag=0
            try:
                source = tinify.from_file(input_file)
                source.to_file(input_file)

            except tinify.errors.AccountError:
                print(u'Key 使用量已超，请更新 Key，并使用命令[Usage] %s [filepath] [key]运行'
                      % os.path.basename(sys.argv[0]))
            print(u'文件无损压缩成功：' + input_file)



        try:
            sImg = Image.open(input_file)
            w, h = sImg.size
            dImg = sImg.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)  # 设置压缩尺寸和选项，注意尺寸要用括号
            dImg.save(input_file)  # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
            target_size = os.path.getsize(input_file)
        except Exception:
            print( "失败！")
    print(u'文件压缩成功：' + input_file)
    old_size = os.path.getsize(input_file)
    print(u'压缩后文件大小：%d 字节' % old_size)



def check_path(input_path,size,tag):
    """如果输入的是文件则直接压缩，如果是文件夹则先遍历"""
    if os.path.isfile(input_path):
        compress_by_tinypng(input_path)
    elif os.path.isdir(input_path):
        dirlist = os.walk(input_path)
        for root, dirs, files in dirlist:
            for filename in files:
                compress_by_tinypng(os.path.join(root, filename),size,tag)
    else:
        print(u'目标文件(夹)不存在，请确认后重试。')



if __name__ == '__main__':
    len_param = len(sys.argv)
    if len_param != 3 and len_param!=4:
        print('[Usage] %s [filepath]' % os.path.basename(sys.argv[0]))
    elif len_param == 3:
        tinify.key = sys.argv[2]
        check_path(sys.argv[1],sys.argv[2],0)
    else:

        check_path(sys.argv[1], sys.argv[2],sys.argv[3])
