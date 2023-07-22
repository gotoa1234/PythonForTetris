import pygame
import random
import sys

# 遊戲標題
TITLE_NAME = "俄羅斯方塊-Python範例遊戲"

# 定義常數
SCREEN_WIDTH = 300  #螢幕寬度
SCREEN_HEIGHT = 600 #螢幕高度
BOARD_WIDTH = 10    #版塊寬的格子數
BOARD_HEIGHT = 20   #版塊高的格子數
BLOCK_SIZE = BOARD_WIDTH + BOARD_HEIGHT #版塊總數

# 主程式
def main():
    global isCanMove

    # 初始化
    pygame.init() # 初始化Pygame程序 
    pygame.mixer.init() # 初始化Pygame的音頻
    clock = pygame.time.Clock()# 遊戲更新畫面頻率

    # 創建遊戲視窗
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 設置視窗標題
    pygame.display.set_caption(TITLE_NAME)  

    # 標記遊戲是否正在進行中
    isCanMove = True
    isPlaying = True  

    while isPlaying:  # 遊戲進行中才執行遊戲迴圈
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  # 如果使用者按下視窗的關閉按鈕，結束程式
                  pygame.quit()
                  sys.exit()
 
    # 或者條件達到跳出，結束程式
    pygame.quit()    
    sys.exit() 

if __name__ == "__main__":
    main()