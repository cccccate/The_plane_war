import pygame
import images


pygame.init()

#创建游戏窗口 480*700
screen = pygame.display.set_mode((480,700))

#绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(-10,-100))

#绘制英雄
hero = pygame.image.load("./images/hero.png")
screen.blit(hero,(150,300))


# 更新
pygame.display.update()

#定义rect记录英雄的初始位置
hero_rect=pygame.Rect(150,300,100,96) #xy坐标，高度宽度

#创建时钟对象
clock = pygame.time.Clock()


#让窗口维持不闪退
while True:

#指定内部代码执行的频率，每秒钟执行60次
    clock.tick(60)

#捕获事件,get()返回的是一个列表
    event_list = pygame.event.get()
    #为了避免输出大堆【】影响查看，此处加一个判断
    if len(event_list) > 0:
        print(event_list)

#修改英雄的位置
    hero_rect.y -= 0.5

#判断英雄的位置（如果英雄到达背景顶部，就从下面钻出来）
    if hero_rect.y <= 0:
        hero_rect.y = 700

#调用bilt方法绘制图像,先绘制背景图像,再绘制英雄
    screen.blit(bg,(-10,-100))
    screen.blit(hero,hero_rect)

#调用update方法更新显示
    pygame.display.update()
    pass

pygame.quit()

