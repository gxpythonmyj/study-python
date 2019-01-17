#1、出现游戏一开始就game over的问题
#问题出在check_game_over函数中条件有误。
#2、出现游戏一开始就闪关不出界面问题
#问题出在if __name__ == "__main__":中“__main后没有双下划线
#按键名称key中的首字母不用大写报错如：'<key-Up>'
#3、报错
# Traceback (most recent call last):
# File "D:/PLRR/study-python/tkiner贪吃蛇.py", line 166, in <module>
#main()
# File "D:/PLRR/study-python/tkiner贪吃蛇.py", line 156, in main
#  world = WORLD(q)
#TypeError: __init__() takes 1 positional argument but 2 were given
#原因是class WORLD(Tk):
#    def __init__(self, queue):中括号里缺少了一个参数queue
#4、有游戏界面有食物没有蛇；报错：
#Exception in thread Thread-1:
#Traceback (most recent call last):
#  File "C:\Anaconda3\lib\threading.py", line 916, in _bootstrap_inner
#   self.run()
# File "D:/PLRR/study-python/tkiner贪吃蛇.py", line 103, in run
#  self.queue.put({'move': self.snake_points})
#AttributeError: 'Snake' object has no attribute 'snake_points'
#原因是：class Snake(threading.Thread):中
# self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]中points少了字母s
#5、游戏界面有蛇有食物，但蛇不动 报错：
#Exception in thread Thread-1:
#Traceback (most recent call last):
#  File "C:\Anaconda3\lib\threading.py", line 916, in _bootstrap_inner
#    self.run()
#  File "D:/PLRR/study-python/tkiner贪吃蛇.py", line 106, in run
#    self.move()
#  File "D:/PLRR/study-python/tkiner贪吃蛇.py", line 115, in move
#    if self.food.postion == new_snake_point:
#AttributeError: 'Food' object has no attribute 'postion'
#class Food():中def new_food(self):中的
#self.positon = x, y  # 存放食物的位置postion打错了
#增加重玩按钮时点“重玩”报错：
#Exception in Tkinter callback
#Traceback (most recent call last):
#  File "C:\Anaconda3\lib\tkinter\__init__.py", line 1699, in __call__
#    return self.func(*args)
#TypeError: __init__() missing 1 required positional argument: 'queue'

# #经验总结：
#1、练习敲代码直接在pycharm上撸；可以利用TAB键和pycharm录入内容记忆功能避免单词打错的问题。

import queue
import time
from tkinter import *
import threading
import random

class WORLD(Tk):
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False

        self.canvas = Canvas(self, width=500, height=300, bg='gray')
        self.canvas.pack()


        self.snake = self.canvas.create_line((0,0),(0,0),fill='#FFCC4C', width=10)
        self.food = self.canvas.create_rectangle(0,0,0,0,fill='#FFCC4C', outline='#FFCC4C')

        self.points_earned = self.canvas.create_text(450, 20, fill='white', text='SCORD: 0')
        self.queue_handler()

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()

                if task.get('move'):
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake, *points)

                if task.get('food'):
                    self.canvas.coords(self.food, *task['food'])

                elif task.get('points_earned'):
                    self.canvas.itemconfigure(self.points_earned,
                                              text='SCORE:{}'.format(task['points_earned']))

                    self.queue.task_done()

        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill='white', text='Game Over')
        quitbtn = Button(self, text='Quit', command=self.destroy)
        rebtn = Button(self, text='Begin', command=self.__init__)
        self.canvas.create_window(200, 180, anchor='nw', window=quitbtn)

class Food():
    def __init__(self, queue):
        self.queue = queue
        self.new_food()

    def new_food(self):
        x = random.randrange(5, 490, 10)
        y = random.randrange(5, 290, 10)

        self.postion = x,y
        self.exppos = x - 5, y - 5, x + 5, y + 5
        self.queue.put({"food": self.exppos})

class Snake(threading.Thread):
    def __init__(self, world, queue):
            threading.Thread.__init__(self)

            self.world = world
            self.queue = queue
            self.daemon = True#漏整句
            self.points_earned = 0
            self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]
            self.food = Food(queue)# 多self.
            self.direction = 'Left'# 漏整句
            self.start()

    def run(self):
        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({'move': self.snake_points})
            time.sleep(0.5)
            self.move()

    def key_pressed(self,e):
        self.direction = e.keysym

    def move(self):
            new_snake_point = self.calculate_new_coordinates()

            if self.food.postion == new_snake_point:
                self.points_earned += 1
                self.queue.put({'points_earned': self.points_earned})
                self.food.new_food()

            else:
                self.snake_points.pop(0)
                self.check_game_over(new_snake_point)
                self.snake_points.append(new_snake_point)

    def calculate_new_coordinates(self):
            last_x, last_y = self.snake_points[-1]
            if self.direction == "Up":
                new_snake_point = last_x, last_y - 10# 规定每次移动的跨度是10像素
            elif self.direction == 'Down':
                new_snake_point = last_x, last_y + 10
            elif self.direction == 'Left':
                new_snake_point = last_x - 10, last_y
            elif self.direction == 'Right':
                new_snake_point = last_x + 10, last_y

            return new_snake_point

    def check_game_over(self, snake_point):
        x, y = snake_point[0], snake_point[1]
        # if not用法
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})

def main():
    q = queue.Queue()
    world = WORLD(q)
    world.title('贪吃蛇')
    snake = Snake(world, q)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)
    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.mainloop()

if __name__ == "__main__":
     main()