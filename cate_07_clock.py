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
screen.blit(hero,(200,500))

hero = pygame.image.load("./images/enemy.png")
screen.blit(hero,(100,200))

# 更新
pygame.display.update()

i=0

#创建时钟对象
clock = pygame.time.Clock()


#让窗口维持不闪退
while True:
    clock.tick(1)
    print(i)
    i += 1
    pass

pygame.quit()

