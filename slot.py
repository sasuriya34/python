#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from re import X
import tkinter as tk
from tkinter.constants import LEFT
import time
import random
from functools import partial

class Column(tk.Frame):
    playTime=True
    closing=False
    tick=10
    number = 0
    def __init__(self, master, x, y) -> None:
        super().__init__(master)
        self.pack()

        self.startTime=time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.x = x
        self.y = y
        self.canvas = tk.Canvas(master,width=90,height=100,bg="skyblue")
        self.option_add('*font', ('FixedSys', 14))
        self.canvas.place(x=self.x, y=self.y)

        tk.Button(master,text="ストップ",command=self.stopButtonClick).place(x=self.x+5, y=self.y+110)

        self.buff = tk.StringVar()

        master.after(50,self.update)

    def stopButtonClick(self):
        if self.closing:
            self.tick *= 2
        elif self.playTime:
            self.closing = True
        elif not self.playTime:
            self.closing = False

        print(str(self.tick))
        if self.playTime:
            self.stopTime=time.time()-self.startTime
            self.playTime=False

    def update(self):
        self.canvas.delete("all")
        num = random.randint(0, 9)
        self.buff.set(str(num))
        #print(self.buff.get())
        self.canvas.create_text(15,0,text=self.buff.get(), anchor="nw", font=("Helvetica",100))
        if self.closing:
            self.tick *= 2
        if self.playTime:
            self.elapsedTime=time.time()-self.startTime
            self.canvas.create_text(0,90,text=round(self.elapsedTime,1),font=("Helvetica",90,"bold"),fill="black",tag="Time",anchor="e")
        else:
            self.canvas.create_text(0,90,text=round(self.stopTime,1),font=("Helvetica",90,"bold"),fill="black",tag="Time",anchor="e")

        #print(str(self.tick))
        if self.tick >= 1000:
            self.tick = 10
            self.number = num
            self.playTime = False
            return num

        self.master.after(1000 - (1000 - self.tick),self.update)

    def startButtonClick(self):
        self.tick = 10
        self.closing = False
        if not self.playTime:
            self.startTime=time.time()-self.elapsedTime
            self.playTime=True
            self.after(1000 - (1000 - self.tick),self.update)
    

class Main():
    playTime = False
    def __init__(self) -> None:

        win = tk.Tk()
        win.geometry("300x200")
        win.title("スロット")
        win.config(bg="black")
        col1 = Column(master=win, x=0, y=10)
        col2 = Column(master=win, x=100, y=10)
        col3 = Column(master=win, x=200, y=10)
        cols = [col1, col2, col3]
        button = tk.Button(win,text="スタート", command=partial(self.startButtonClick, cols)).place(x=100, y=160)
        #button.pack(side=LEFT, anchor=tk.N, pady=25)
        #button.bind("<ButtonRelease-1>", self.startButtonClick)
        win.mainloop()

    def startButtonClick(self, e):
        if not self.playTime:
            self.playTime = True
            for col in e:
                col.startButtonClick()
        else:
            self.playTime = False
            if e[0].number == e[1].number == e[2].number:
                print("大当たり！！！")
            else:
                print("はずれ")
        # ss:str = "X:{0}  Y:{1}  text={2}".format(e.x, e.y, e.widget["text"])
        # print(ss)                                   # コールバック関数には マウス座標などの情報が引き渡される

if __name__ == "__main__":
  Main()