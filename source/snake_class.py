from tkinter import*
from screen import Screen

class Snake:
    def __init__(self,scr):
        self.scrn = scr
        self.Start()

    def Draw_Quad(self):
        a = self.scrn.canvas.create_polygon(self.coord, fill='red', outline='black')
        return a
    def Move_Quad(self,ref,x,y):
        self.scrn.canvas.move(ref,x,y)
    def Move_Snake(self):
        self.last_coord=self.body_pos[-1].copy()
        for i in range(len(self.body_pos)-1,0,-1):
            self.Move_Quad(self.body_ref[i], self.body_pos[i-1][0]-self.body_pos[i][0], self.body_pos[i-1][1]-self.body_pos[i][1])
            self.body_pos[i]=self.body_pos[i-1].copy()
        self.Move_Quad(self.body_ref[0], self.dir[0] * self.speed, self.dir[1] * self.speed)
        self.body_pos[0][0] += self.dir[0] * self.speed
        self.body_pos[0][1] += self.dir[1] * self.speed
        if self.body_pos[0]==self.last_coord:
            self.Is_Exit=True
        self.root.after(15)

    def KeyBoard(self,x,y):
        self.dir[0]=x
        self.dir[1]=y

    def S_Update(self):
        self.Move_Snake()
        self.Is_Game_Over()

    def Apple_Is_Eatten(self):
        self.body_pos.append(self.last_coord)
        a=self.Draw_Quad()
        self.body_ref.append(a)
        self.Move_Quad(a,self.last_coord[0],self.last_coord[1])

    def Is_Game_Over(self):
        for i in range(1,len(self.body_pos)):
            if self.body_pos[i]==self.body_pos[0]:
                self.Is_Exit=True
                break

    def Wall(self):
        for i in range(len(self.body_pos)):
            if self.body_pos[i][0]>=self.scrn.width:
                self.Move_Quad(self.body_ref[i],10-self.body_pos[i][0],0)
                self.body_pos[i][0]=10
            if self.body_pos[i][0]<=0:
                self.Move_Quad(self.body_ref[i], self.scrn.width - 10 - self.body_pos[i][0], 0)
                self.body_pos[i][0]=self.scrn.width-10
            if self.body_pos[i][1]>=self.scrn.height:
                self.Move_Quad(self.body_ref[i], 0, 10 - self.body_pos[i][1])
                self.body_pos[i][1] = 10
            if self.body_pos[i][1]<=0:
                self.Move_Quad(self.body_ref[i], 0, self.scrn.height - 10 - self.body_pos[i][1])
                self.body_pos[i][1] = self.scrn.height - 10

    def Start(self):
        self.last_coord = [0, 0]
        self.body_pos = []
        self.Is_Exit = False
        self.root = self.scrn.root
        self.speed = 10
        self.dir = [0, -1]
        self.body_pos.append([300, 300])
        self.body_ref = []
        self.coord = [0, 0, 10, 0, 10, 10, 0, 10]
        self.scrn.Create_Canvas()
        a = self.Draw_Quad()
        self.body_ref.append(a)
        self.scrn.canvas.move(self.body_ref[0], self.body_pos[0][0], self.body_pos[0][1])