import random
a=random.randint(1,101)
while True:
    b=eval(input("请猜一个100以内的数"))
    if b<1 or b>100:
        print("输入的数不在范围内")
        continue
    elif b>a:
        print("太大了")
        continue
    elif b<a:
        print("太小了")
        continue
    elif b==a:
        print("猜对了")
        break

