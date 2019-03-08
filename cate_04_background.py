import pygame

pygame.init()

#创建游戏窗口 480*700
screen = pygame.display.set_mode((480,700))

#绘制背景图像
#加载
bg = pygame.image.load("./images/background.png")
#绘制
screen.blit(bg,(-10,-100))
#更新
pygame.display.update()


#让窗口维持不闪退
while True:
    pass

pygame.quit()

