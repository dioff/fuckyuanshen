import cv2 
import pyautogui
import subprocess
import numpy as np
from PIL import ImageGrab


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

    # 判断是否满足播放视频条件
    if white_percentage > 50:
        try:
            video_path = ""  # 修改为实际视频文件路径
            subprocess.Popen(['ffplay', '-fs', '-autoexit', video_path])
            print("原神，启动！！！!")
            break
        except Exception as e:
            print(f"Error: {e}")
            break
