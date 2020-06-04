lower = int(input("输入区间最小得值："))

upper = int(input("输入区间最大得值"))

for num in range(lower,upper +1):

    #输入大于1

    if num >1:
        for i in range(2,num):

            if (num%i) == 0:
                break

        else:
            print(num)

