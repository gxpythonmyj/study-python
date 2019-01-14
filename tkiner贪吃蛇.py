import queue
import time
from tkinter import *
import threading
import random
class Food():
    def __init__(self, queue):
    # queue队列
        self.queue = queue
        self.new_food()
    def new_food(self):
        x = random.randrang(50, 480, 10)  # 10是补尝值
        y = random.randrang(80, 640, 10)
    # 需要注意的是：控制耦合度，尽量低耦合
    # 消息队列，它的任务是存储消息并提供交换服务
        self.positon = x, y  # 存放食物的位置
        self.queue.put({"food": self.postion})
class Snake(threading.Thread):
    def __init__(self, world, queue):
            threading.Thread.__init__(self)
            # 世界的调用
            self.word = word
            # 消息队列
            self.queue =queue
            # 分值
            self.points_earned = 0
         # 食物
            self.food = Food(self.queue)
        # 描述蛇的点
            self.snake_point = [(495, 55), (485, 55), (465, 55), (455, 55)]
        # 开始
            self.star()
    def run(self):
        # 如果游戏结束
        if self.world.is_game_over:
        # 则删除
                self._delete()

        while not self.world.is_game_over:
                self.queue.put({"move": self.snake_points})
        # 控制蛇的速度
                time.sleep(0.5)
                self.move()
    def move(self):
    # 重新计算蛇头位置
            new_snake_point = self.cal_new_pos()
    # 蛇头位置跟食物位置相同
            if self.food.postion == new_snake_point:
    # 每吃一个食物的分值
                self.points_earned += 1
    # 给队列发一个加分消息，在屏幕右上角显示得分值
                self.queue.put({"points_earned": self.points_earned})
    # 食物被吃则重新生成新的
                self.food.new_food()
            else:
    # 需要注意蛇的信息保存方式
    # 每次移动是发展删除存放的最前位置，并在后面追加***重点
    # 弹出蛇尾
                self.snake_points.pop(0)
        # 判断程序是否退出，因为新的蛇可能撞墙（传入新的蛇头位置）
                self.check_game_over(new_snake_point)
        # 发送停止消息
                self.snake_points.append(new_snake_point)
    def cal_new_position(self):
            last_x, last_y = self.snake_points[-1]
            if self.direction == "Up":
                new_snake_point = last_x, last_y + 10  # 规定每次移动的跨度是10像素
            elif self.direction == 'Down':
                new_snake_point = last_x, last_y - 10
            elif self.direction == 'Left':
                new_snake_point = last_x - 10, last_y
            elif self.direction == 'Right':
                new_snake_point = last_x + 10, last_y
            return new_snake_point
    def check_game_over(self, snake_point):
        #
            x, y = snake_point[0], snake_point[1]
        # if not用法
            if not -5 < x < 505 or -5 < y < 315 or snake_point in self.snake_point:
                self.queue.put({'game_over': True})
class world(Tk):
   # 调用父类的构造函数
    def __init__(self):
            Tk.__init__(self)
            self.queue
        # 开始时game_over为假
            self.is_game_over = False
        # 画板
            self.canvas = Canvas(self, width=500, height=300, bg='red')
        # 固定画板
            self, pack()
        # 传入蛇和食物
        # 蛇的颜色宽度起始位置
            self.snake
            self.cavas.create_line((0, 0), (0, 0), fill="black", width=10)
        # 画食物小长方形
            self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', outline='FFCC4C')
            self.points_earned = self.canvas.create_text(450, 20, fill='white', text='SCORD: 0')
        # 队列信息处理
            self.queue_handler()
    def queue_handler(self):
        # 需要不断从消息队列中拿到消息，所以使用死循环
            try:
                while True:
                    task = self.queue.get(block=False)
                    if task.get("game_over"):
                        self.game_over()
                    if task.get("move"):
                        points = [x for point in task['move'] for x in point]
                    # 重新绘制蛇（用系统函数）
                        self.canvas.coords(self.snake, *points)
                    # 食物
                    if task.get("food"):
                    #food = [x for food in task['food'] for x in food]  一味的仿上一句代码，不知所以，哈哈哈。
                        self.canvas.coords(self.food, *foods)
                    # 得分
                    elif task.get('points_earned'):
                        self.canvas.itemconfigure(self.points_earned, text='SCORE: {}'.format(task['points_earned']))
            except queue.Empty:
                if not self.is_game_over:
                        self.canvas.after(100, self.queue_handler)
                #
    def game_over(self):
            self.is_game_over = True
            self.canvas.create_text("Game Over")
        # 退出调用消毁函数
            qb = Button(self, text="Quit", command=self.destroy)
        # 重玩重新调用构造函数
            rb = Button(self, text="Again", command=self.__init__)
            self.canvas.create_window(200, 180, anchor='nw', window=quitbtn)
def main():
    q = queue.Queue()
    world = world(q)
    world.title("贪吃蛇")
    snake = Snake(world, q)
    world.bind('<key-Up>', snake.key_pressed)
    world.bind('<key-Down>', snake.key_pressed)
    world.bind('<key-Left>', snake.key_pressed)
    world.bind('<key-Right>', snake.key_pressed)
    world.mainloop()
if __name__ == "__main__":
    main()


