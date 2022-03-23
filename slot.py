from re import X
import tkinter as tk
import time

class Column(tk.Frame):
    def __init__(self, master, x, y) -> None:
        super().__init__(master)
        self.pack()

        self.startTime=time.time()
        self.stopTime=0.0
        self.elapsedTime=0.0
        self.playTime=False

        self.x = x
        self.y = y
        self.canvas = tk.Canvas(master,width=90,height=100,bg="white")
        self.canvas.place(x=self.x, y=self.y)

        tk.Button(master,text="ストップ",command=self.stopButtonClick).place(x=self.x+5, y=self.y+110)
        master.after(50,self.update)

    def stopButtonClick(self):
        if self.playTime:
            self.stopTime=time.time()-self.startTime
            self.playTime=True

    def update(self):
        self.canvas.delete("all")
        if self.playTime:
            self.elapsedTime=time.time()-self.startTime
            self.canvas.create_text(0,90,text=round(self.elapsedTime,1),font=("Helvetica",90,"bold"),fill="black",tag="Time",anchor="e")
        else:
            self.canvas.create_text(0,90,text=round(self.stopTime,1),font=("Helvetica",90,"bold"),fill="black",tag="Time",anchor="e")

        self.master.after(50,self.update)

    def startButtonClick(self):
        if not self.playTime:
            self.startTime=time.time()-self.elapsedTime
            self.playTime=True

def startButtonClick(self):
    if not self.playTime:
        self.playTime = True

def main():
    win = tk.Tk()
    win.geometry("300x200")
    win.title("スロット")
    win.config(bg="black")
    playtime = False
    col1 = Column(master=win, x=0, y=10)
    col2 = Column(master=win, x=100, y=10)
    col3 = Column(master=win, x=200, y=10)
    tk.Button(win,text="スタート",command=startButtonClick).place(x=100, y=160)
    win.mainloop()

if __name__ == "__main__":
  main()