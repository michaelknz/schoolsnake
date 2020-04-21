from random import randint
from sing_buf import Buf_Struct

class Bufs:
    def __init__(self,screen):
        self.scrn=screen
        self.ver_time_buf=50
        self.bufs_buffer=[]
        self.MAX_RAND=10000
        self.del_pos=2
        self.buf_vert_pos = [0, 0, 10, 0, 10, 10, 0, 10]

    def Gen_Rand_Int(self, digit1, digit2):
        return randint(digit1,digit2)

    def Is_Gen(self):
        rnum=self.Gen_Rand_Int(0,self.MAX_RAND)
        if rnum % self.ver_time_buf==0:
            x=self.Gen_Rand_Int(2,self.scrn.width//10-self.del_pos)*10
            y=self.Gen_Rand_Int(2,self.scrn.height//10-self.del_pos)*10
            r=self.scrn.canvas.create_polygon(self.buf_vert_pos,fill='blue',outline='black')
            self.scrn.canvas.move(r,x,y)
            self.bufs_buffer.append(Buf_Struct(r,'tplus',x,y))

    def Is_Buffed(self, head_pos):
        for i in range(len(self.bufs_buffer)):
            if(head_pos[0]==self.bufs_buffer[i].x and head_pos[1]==self.bufs_buffer[i].y):
                self.scrn.canvas.delete(self.bufs_buffer[i].ref)
                ret=self.bufs_buffer[i].type
                del self.bufs_buffer[i]
                return ret
            return -1
