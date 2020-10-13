# Image-compression-size
图片压缩，指定压缩后的大小 最后生成的图片会低于指定的大小  
过程是先使用 tinypng api先无损压缩，然后再resize指定压缩大小 注意resize是暴力压缩 之后图片会模糊  
可以选择是否用api


## 使用方法
### 一 下载image_compression.py到本地
### 二 申请一个自己的key

[点击此处](https://tinypng.com/developers)  申请一个key
### 三 把刚才申请的key替换一下
```
tinify.key = "在此处输入你的API——key"
```
### 四 命令行运行
```
python image_compression.py [filepath] [size] [tag]
```
filepath是路径  
size是大小 单位是kb  
tag是指定是否 用api进行无损压缩 值是1或0 默认是0  
如果不想用api 则此处tag参数可以不要 并且可以忽略第二第三步  
例如
```
python compress-with-tinypng.py /home/sample 500 1
```
