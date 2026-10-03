import random
answer = random.randint(1,100)
count=0
history=[]
while True:
    guess=int(input("请输入一个数："))
    history.append(guess)    
    count+=1
    if guess==answer:
        print("猜对了")
        break 
    elif guess<answer:
        print("猜小了")
    elif guess>answer:
        print("猜大了")
print(f"你一共猜了{count}次")    
print(f"历史猜测为：{history}")