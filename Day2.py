import random
answer = random.randint(1,100)
while True:
    guess=int(input("请输入一个数："))
    if guess==answer:
        print("猜对了")
        break 
    elif guess<answer:
        print("猜小了")
    elif guess>answer:
        print("猜大了")

    
