import random
import tkinter
class RandomBall:
    """
    定义运动的球的类

    """
    def __init__(self,canvas,scrnwidth,scrheight):
        """
        canvas;画布,所有的内容都应该在画布上呈现出来，此处通过此变量传入scrnwidth/scrheight
        屏幕宽高
        """
        #球出现的初始位置要随机
        #xpos表示位置的x坐标(屏幕是一个二维空间，用x\y)
        self.xpos = random.randint(10,int(scrnwidth)-20)
        #ypos表示位置的y坐标
        self.ypos = random.randint(10,int(scrheight)-20)
        #定义球运动的速度
        #模拟运动：不断的擦掉原来的画，然后在一个新的地方再从新绘制
        #xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        #yvelocity模拟y轴方向运动
        self.yvelocity = random.randint(4, 20)
        #定义屏幕大小
        self.scrnwidth = scrnwidth
         #定义屏幕的高度
        self.scrheight = scrheight
        #定义球的大小，用半径表示
        self.radius = random.randint(20,120)
        #定义颜色
        #RGB红绿蓝表示法：三个数字，每个数字的值是0-255之间，表示三个颜色的大小
        c = lambda: random.randint(0,255)
        self.color ='#%02x%02%02x%'%(c(), c(), c())


    def create_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球（创建一个球）
        '''
        #tkinter没有画圆形函数
        #只有一个画椭圆函数，画椭圆需要定义两个坐标，
        #在一个长方形内画椭圆，我们只需要定义长方开形左上角和右下角就行
        #
        x1 = self.xpos - self.radius#碰右检测
        y1 = self.ypos + self.radius#碰左检测
        x2 = self.xpos + self.radius#碰上检测
        y2 = self.ypos - self.radius#碰下检测
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = self.color)
    def move_ball(self):
        #移动球的时候，需要控制球的方向
        #每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        #以下判断是会否撞墙
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity = -self.xvelocity
        if self.xpos - self.radius >= self.scrnwidth:
            self.xvelocity = -self.xvelocity
        if self.ypos + self.radius >= self.scrheight:
            self.yvelocity = -self.yvelocity
        if self.ypos + self.radius >= self.scrheight:
            self.yvelocity = -self.yvelocity
        #在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)
class ScreenSaver():
    '''
    定义屏保的类
    可以被启动
    '''
    balls = list()

    def __init__(self):

        self.num_balls = random.randint(6,20)
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        #取消条件（鼠标移动）
        self.root.bind('<Motion>', self.myquit)
        #取消条件（键盘输入）
        #得到屏幕参数（尺寸大小）
        w,h = self.root.winfo_screenwidth(), self.winfo_screenheight()

        self.canvas = tkinter.Canvas(self.root, width = 2, height = h)
        self.canvas.pack()

        for i in range(self.num_balls):
            ball = RandomBall(self.cavas, scrnwidth = w, scrnheight = h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

        def run_screen_saver():
            for ball in self.balls:
                ball.move_ball()
            self.cavas.after(200, self.run_screen_saver)

        def myquit(self, e):
            #撤消函数
            self.root.destroy()

if __name__ == "__main__":
    #启动屏保
    ss = ScreenSaver()
    ss.start()
