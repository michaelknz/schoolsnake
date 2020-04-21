import time
from tkinter import*

class Timer:
    def __init__(self,screen):
        self.scrn=screen
        self.time_col=120
        self.min_col=self.time_col//60
        self.sec_col=self.time_col%60
        self.time_var=StringVar()
        self.Set_time()
        self.label=Label(screen.root, textvariable=self.time_var)
        self.label.pack()
        self.scrn.canvas.create_window((0,0), anchor="nw", window=self.label)
        self.Set_time()
        self.last_time=time.clock()
        self.cur_time=self.last_time
        self.del_time=0

    def Set_time(self):
        self.time_var.set(str(self.min_col)+':'+str(int(self.sec_col//10))+str(int(self.sec_col%10)))

    def Update(self):
        self.cur_time=time.clock()
        self.del_time=self.cur_time-self.last_time
        self.sec_col-=self.del_time
        while self.sec_col<0:
            self.sec_col+=60
            self.min_col-=1
        self.Set_time()
        self.last_time=self.cur_time