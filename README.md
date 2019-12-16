# Crab
鉴于在小程序开发过程中找不到可以用的图片裁剪API就自己写了一个。。

当然只是用在一小段时间所以没有添加太多功能

main.py中port可修改为自己想要使用的端口

添加了https协议认证，修改keyfile与certfile为证书文件路径即可

# 传入参数
传入方式为POST请求

参数形式：
```
{
  base64code: ImageBase64Code,
  array: positionArray
}
```
ImageBase64Code为图片的base64编码，positionArray为要进行裁剪的坐标数组，(x_1,y_1)、(x_2,y_2)分别对应左上角和右上角坐标

# 返回参数
返回成功参数为如下形式：
```
{
  errMsg: msg,
  resPhoto: resArray
}
```
分别对应错误信息和返回的图片base64数组
