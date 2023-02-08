import random
import time
import pyautogui

from FPSDetect import *
from ctypes import *
# 加载相关工具函数
from utils.FPSUtils import *


dll = cdll.LoadLibrary(r'lib/Dll.dll')  # 加载用C语言封装过的“易键鼠”dll


def shoot_screen():
    while True:
        img = pyautogui.screenshot(region=[LEFT, TOP, 1539, 1193])  # region为屏幕截取区域格式为（left，top，w，h）
        # 存储游戏过程中的截图的路径
        images_path = 'C:\\Users\\ChenJunzhe\\Desktop\\cs1.6\\FPSAutomaticAiming-main\\jietu'
        img.save(
            images_path + str(int(time.time())) + ''.join(
                random.sample('cs1.6', 2)) + '.jpg')  # 随机生成文件名
        time.sleep(0.5)


if __name__ == "__main__":
    # ssp = Process(target=shoot_screen, name="ssp", args=())
    # ssp.start()
    # mPid = PID(0, 0, 1.0, 0)  # PID 控制器参数：（真值，p，i，d）（有问题）
    while True:
        img = shoot_screen()
        # img = ScreenShout()  # 截取屏幕检测区域
        detections = detect(img)  # 送入yolo检测
        btc, btp = FindBestCenter(detections)  # 确定目标最优的射击中心
        if btc is not None:  # 如果屏幕区域有射击目标
            # dll.MoveTo2(int(LEFT + btc[0]), int(TOP + btc[1]))  # 调用易键鼠移动鼠标（此处更换为自己的）
            pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))
            # dll.MoveTo2(int(LEFT + btc[0]), int(TOP + btc[1]))  # 调用易键鼠移动鼠标（此处更换为自己的）
            # time.sleep(0.02)
            pyautogui.click(int(LEFT + btc[0]), int(TOP + btc[1]),button='left')
            print("移动鼠标！")

        # pyautogui.moveTo(int(LEFT), int(TOP))
        # time.sleep(0.2)
        # pyautogui.click(int(LEFT ), int(TOP ), button='left')
        # print("移动鼠标！")
