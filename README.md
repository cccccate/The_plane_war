# python项目实战——飞机大战
python基础内容都已学完，一些实用的小项目也设计并实现了几个，但是在设计项目的过程中发现自己对于一些知识点，真正想用的时候很不顺手，所以跟着学习视频做一个完整的飞机大战项目，捡起那些已经被自己遗忘的知识点  
## 目标  
强化面向对象程序设计  
使用pygame模块  
## 运行环境   
linux系统  
安装pygame模块  
```
pip3 install pygame
```
注：pip3 install与pip install的区别：pip调用的是系统安装的pip，对应python2.7版本，并安装文件在相关路径下，直接pip3调用的是python3下的pip，并安装文件在相应目录下  
验证pygame是否安装成功  
```
python3 -m pygame.examples.aliens
```
## 程序设计过程  
### 1 游戏的初始化和退出  
pygame.init和pygame.quit  
注意：init方法主要针对图像绘制窗口处理等模块进行初始化的，对于下文中的Rect方法（只是封装了一些数字计算），不执行pygame.init()也可以直接使用  
[初始化和退出](cate_01_init.py)
### 2 坐标系  
描述坐标系的四个参数（x,y,width,height)  
pygame.Rect专门用来描述矩形区域  
[rect描述坐标系](cate_02_rect.py)  
### 3 创建游戏主窗口  
pygame的模块pygame.display用于创建，管理游戏窗口  
```
pygame.display.set_mode() # 初始化并创建一个游戏窗口  
pygame.display.update() # 刷新窗口内容  
```
```
set_mode(resolution(0,0),flags=0,depth=0) # 缺省参数（已有默认值，调用时可以不指定）
```
 set_mode方法的返回结果是游戏的窗口，后续需要在这个窗口上进行操作，所以要创建一个变量来接受set_mode的返回值，resolution指定屏幕的宽和高  
 ```
 screen = pygame.display.set_mode((480,700))
 ```
 [创建游戏主窗口](cate_03_setmode.py)  
### 4 简单的游戏循环  
启动游戏后，不会立即退出（闪退）,游戏循环就是无限循环  
```
while True:
  pass
```


