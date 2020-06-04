# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。


#通过用户输入得数字计算阶乘


#输入
num =  int(input("请输入一个数字:"))

factorial = 1

#产看输入是负数 0  或者 正数

if num <0:
    print("不好意思，负数没有阶乘")
elif num == 0:
    print("0 的阶乘位1")

else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("%d 的阶乘为 %d" %(num,factorial))