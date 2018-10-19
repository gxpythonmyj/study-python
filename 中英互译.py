from tkinter import *
from tkinter import messagebox
import requests
#创建窗口
root = Tk()
#给窗口设置标题
root.title('中英互译')
#设置窗口大小   参数用小写x连接
root.geometry('370x320+600+300')
#设置窗口弹出在屏幕上的位置  由于这步所调用的函数跟窗口大小设置的一样，因此可以将参数直接放到上一行中。
#root.geometry('+600+300')
#控件   晕打错label报错lable没有定义查半天   从视频看讲师有故意把人带入坑的嫌疑
#fg =''可调文字颜色
label = Label(root,text = '输入要翻译的内容：')
#把控件定位到窗口
label.grid()

#输入控件      第一行括号里规定的是字体和字号
entry = Entry(root,font = ('微软雅黑',16))
entry.grid(row = 0,column = 1)
label1 = Label(root,text = '翻译之后的结果：')
label1.grid(row =1, column =0)
entry1 = Entry(root,font = ('微软雅黑',16))
entry1.grid(row =1,column =1)
#按钮
button = Button(root,text ='翻译',width = '10')
#对齐方式sticky  N S E W 英文东南西北的简写
button.grid(row = 2,column = 0,sticky = W)
#退出触发  command = root.quit
button1 = Button(root,text = '退出',width = 10,command = root.quit)
button1.grid(row = 2,column = 1,sticky = E)


#显示窗口
root.mainloop()
