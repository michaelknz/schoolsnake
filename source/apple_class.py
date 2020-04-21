from random import randint
from screen import Screen

class Apple:
    def __init__(self,scr):
        self.scrn=scr
        self.del_pos=2
        self.Start()

    def Random_Num(self,digit1,digit2):
        return randint(digit1,digit2)

    def Move_Apple(self,x,y):
        self.scrn.canvas.move(self.apple_ref,x,y)

    def Draw_Apple(self):
        a = self.scrn.canvas.create_polygon(self.apple_vert_pos, fill='red', outline='black')
        return a

    def Apple_Is_Eatten(self):
        old_apple_pos=self.apple_pos.copy()
        self.apple_pos[0]=self.Random_Num(2,self.scrn.width//10-self.del_pos)*10
        self.apple_pos[1]=self.Random_Num(2,self.scrn.height//10-self.del_pos)*10
        self.Move_Apple(self.apple_pos[0]-old_apple_pos[0],self.apple_pos[1]-old_apple_pos[1])

    def Start(self):
        self.apple_pos = []
        self.apple_vert_pos = [0, 0, 10, 0, 10, 10, 0, 10]
        self.apple_ref = self.Draw_Apple()
        self.apple_pos.append(self.Random_Num(2, self.scrn.width // 10 - 2) * 10)
        self.apple_pos.append(self.Random_Num(2, self.scrn.height // 10 - 2) * 10)
        self.Move_Apple(self.apple_pos[0], self.apple_pos[1])