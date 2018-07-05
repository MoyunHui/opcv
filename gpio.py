import RPi.GPIO as GPIO         ## 导入GPIO库
import time                     ## 导入time库

pin = 7                         ## 使用7号引脚
GPIO.setmode(GPIO.BOARD)        ## 使用BOARD引脚编号
GPIO.setup(pin, GPIO.OUT)       ## 设置7号引脚为输出通道

while True:
    GPIO.output(pin, GPIO.HIGH) ## 打开GPIO引脚（HIGH）
    time.sleep(1)               ## 等待1秒钟
    GPIO.output(pin, PGIO.LOW)  ## 关闭GPIO引脚（LOW）
    time.sleep(1)               ## 等待1秒钟

GPIO.cleanup()                  ## 清除，释放资源

