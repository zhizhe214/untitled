'''
提出产品需求，形成技术方案

由于是练习，所以是没有让每个人根据自己的生活经验来提需求。
而是直接给定了产品需求：用Python代码模拟单行的滚动广告。
初步形成的技术方案是：print+字符串+循环+time模块（控制滚动速度）。

# 运行前可将第8行改为 for i in range(20) 控制一下循环次数。
2
# 或者，可以直接运行，然后用“刷新网页”这种方法强行打断程序。



    import time
sleep_time=1;
add='撸起袖子加油干！'
show=''
for i in range(len(add)):
    time.sleep(sleep_time)
    show+=add[i]
    print(show)
'''
import os, time
def main():  # 用函数封装，可复用性会高一些（可在其他的.py文件里调用该函数。）
    content = ' 风变编程，陪你一起学Python '  # 广告词可自定义。
    while True:
        os.system('clear')  # 完成清屏：清屏和打印结合起来，形成滚动效果。
        print(content)
        content = content[1:] + content[0]  # 这行代码相当于：将字符串中第一个元素移到了最后一个。
        time.sleep(0.25)  # 你可以改下时间，体会“循环周期”和“滚动速度”之间的关联。

if __name__ == '__main__':  # 类里面学到的检测方法，在函数中其实也可以用。
    main()


