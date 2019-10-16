'''
r=input("请输入圆的半径：")
r=int(r)
s=r*r*3.14
l=2*3.14*r
print("面积为："+str(s))
print("周长为："+str(l))
'''

  # 求绝对值
num = input("输入一个数字：")
num=float(num)
if num>=0:
    print("%s 的绝对值为：%s" %(num,num))
else:
    print("%s 的绝对值为：%s" %(num,-num))