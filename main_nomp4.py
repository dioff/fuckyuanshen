import cv2 
import pyautogui
import subprocess
import numpy as np
from PIL import ImageGrab
import pygame

# 初始化pygame
pygame.init()

while True:
    # 获取屏幕分辨率
    screen_width, screen_height = pyautogui.size()  
        
    # 截图
    print("正在检测屏幕...")
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(0,0,screen_width,screen_height))), cv2.COLOR_BGR2RGB)

    # 计算屏幕白色像素比例
    white_pixels = np.count_nonzero(screenshot == [255, 255, 255])
    total_pixels = screenshot.shape[0] * screenshot.shape[1]
    white_percentage = white_pixels / total_pixels * 100

    # 判断是否满足播放音频条件
    if white_percentage > 50:
        try:
            audio_path = "mp3/BGM_1.mp3"  # 修改为实际音频文件路径

            # 播放音频文件
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

            print("播放音频!")
            
            # 等待音频播放完成
            while pygame.mixer.music.get_busy():
                pass
            
        except Exception as e:
            print(f"Error: {e}")
