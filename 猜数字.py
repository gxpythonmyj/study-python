#猜数字游戏
#给定一个范围内的一个数让人来猜
# 提示小于目标数或大于目标数
# 猜中打印“恭喜你答对了”
#增加随机模块　import random
#猜对或退出之前随机生成的数字不能变
#coding:utf-8
import random
#random_number = random.randint(0,9)
def random_number():
    random_number = random.randint()
    return random_number
#print(random.randint(0,9))
x = random_number(0,20)
print('请输入任意一个整数数字:')

number = int(input())
if number ==x:
    print("你输入的数字是:%d"%number)
    print("恭喜你答对了！")
elif number > x and number - x > 3:
    print("大了！")
elif number < x and number - x <-3:
    print("小了！")
elif abs(number - x) <= 3:
    print("很接近了！")
else:
    print("还继续吗？")


