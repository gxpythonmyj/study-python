#猜数字游戏
#给定一个范围内的一个数让人来猜
# 提示小于目标数或大于目标数
# 猜中打印“恭喜你答对了”
#coding:utf-8

print('请输入任意一个整数数字:')
number = int(input())
if number ==10:
    print("你输入的数字是:%d"%number)
    print("恭喜你答对了！")
elif number > 10:
    print("大了！")
elif number < 10:
    print("小了！")
elif number - 10 <= 3:
    print("很接近了！")
else:
    print("还继续吗？")


