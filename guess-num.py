import random
start = input('請決定隨機數字開始值:')
end = input('請決定隨機數字結束值:')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
    count += 1 #count = count + 1
    num = input('請猜數字:')
    num = int(num)
    if num == r :
        print('你猜中了!')
        break
    elif num > r :
        print('你比答案大')
    elif num < r :
        print('你比答案小')
    print('這次是你猜的', count, '次')