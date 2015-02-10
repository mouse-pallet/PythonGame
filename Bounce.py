from Tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos= self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.game_start=False
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<Button-1>',self.start_game)

    def start_game(self,evt):
        self.game_start=True
       
    def turn_left(self,evt):
        self.x = -2

    def turn_right(self,evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        elif pos[2] >= self.canvas_width:
            self.x=0

class Timer:
    def __init__(self,canvas):
        self.time=0
        self.timer_text=canvas.create_text(20,20,text=str(self.time),font=('Times',25))

    def count(self,canvas):
        self.time+=1
        canvas.itemconfig(self.timer_text,text=str(self.time))

tk=Tk()
tk.title("GAME")
tk.resizable(0,0)
tk.wm_attributes("-topmos",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

paddle=Paddle(canvas,"blue")
ball=Ball(canvas,paddle,"red")
timer=Timer(canvas)

rooptime=1

start_text=canvas.create_text(100,150,text='click to start game',font=('Times',20),state='hidden')

while True:
    if paddle.game_start==False and ball.hit_bottom == False:
       canvas.itemconfig(start_text,state='normal')
    if paddle.game_start==True and ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(start_text,state='hidden')
        if rooptime%90==0:
                timer.count(canvas)
    if ball.hit_bottom == True:
        time.sleep(0.5)
        canvas.create_text(100,150,text='Game Over',font=('Times',20))
    tk.update_idletasks()
    tk.update()
    rooptime+=1
    time.sleep(0.01)
