from curses import window
import tkinter as tk
import time

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()


        master.geometry("300x150")
        master.title("時計")
        master.config(bg="white")

        self.canvas = tk.Canvas(master,width=290,height=80,bg="skyblue")
        self.option_add('*font', ('FixedSys', 14))
        self.canvas.place(x=3,y=10)
        self.canvas.create_line(50, 50, 50, 50,dash=(1,1))

        self.buff = tk.StringVar()
        self.buff.set('')

        self.label = tk.Label(textvariable=self.buff.get()).pack()
        self.canvas.pack()
        print(self.label)
        
        master.after(1000,self.update)
    
    # 時刻の表示
    def update(self):
        #self.canvas.delete("Time")
        self.buff.set(time.strftime('%I:%M:%S'))
        print(self.buff.get())
        self.canvas.create_text(100,40,text=self.buff.get())
        self.master.after(1000,self.update)

def main():
  win = tk.Tk()
  app = Application(master=win)
  app.mainloop()

if __name__ == "__main__":
  main()
