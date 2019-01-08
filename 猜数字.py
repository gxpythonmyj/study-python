#猜数字游戏
#1、给定一个范围内的一个数让人来猜
# 2、提示小于目标数或大于目标数
# 3、猜中打印“恭喜你答对了”
#4、增加随机模块　import random
#5、猜对或退出之前随机生成的数字不能变（用次数限定)
#coding:utf-8
#输入数字：shuru_num;生成的数字：random_num;猜的次数：jihui_num
#参考代码来源：https://blog.csdn.net/changzizi/article/details/81943499
#引用随机模块
import random
#随机生成0到20之间的数字
random_num = random.randint(0,20)
#random_num =int(random_num)
#规定次数
jihui_num = 3
#打印游戏规则
print("猜字游戏，数字在0到20之间，你有｛3｝次机会".format(jihui_num))
#设制判断条件
while (jihui_num > 0):
    shuru_num = input("请输入一个数字：")
    #用isdigit函数判断输入的数字是否为十进制数字字符
    if shuru_num.isdigit():
        shuru_num =int(shuru_num)#这句是否是多余呢？尝度注掉后代码可运行，但输入数字后回车报类型错误TypeError: '<' not supported between instances of 'str' and 'int'。
        if shuru_num == random_num:
            print('您输入的数字:%d' % shuru_num)
            print('你真牛！')
            break
        elif shuru_num < random_num:
            print('您输入的数字小了！')
        elif shuru_num - random_num == 1 or random_num - shuru_num == 1:
            print("很接近了！")
        else:
            print('您输入的数字大了！')
        jihui_num -= 1
        if jihui_num ==0:
            print("您没有机会了")
            break
    else:
        print("您输入的不是数字，请重新输入")
print("游戏结束")






