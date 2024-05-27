import sys
import os
import pygame
from pygame.locals import QUIT
from threading import Timer

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (4000, 60)

# 初始化
pygame.init()
# 建立 window 視窗畫布，大小為 800x600
window_surface = pygame.display.set_mode((2000, 1200))
# 設置視窗標題為 Hello World:)
pygame.display.set_caption('Hello World:)')
# 清除畫面並填滿背景色
window_surface.fill((255, 255, 255))

# 宣告 font 文字物件
head_font = pygame.font.Font("./Fira_Code/FiraCode-VariableFont_wght.ttf", 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('''山aaabbbbccccddddeeeeffffgggghhhhiiii''', True, (0, 0, 0))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
window_surface.blit(text_surface, (0, 0))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()









# 事件迴圈監聽事件，進行事件處理
while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
