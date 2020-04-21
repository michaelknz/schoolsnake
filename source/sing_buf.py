class Buf_Struct:
    def __init__(self,ref,type,x,y,timer_obj):
        self.ref=ref
        self.type=type
        self.x=x
        self.y=y
        self.timer_obj=timer_obj

    def Set_coords(self,nx,ny):
        self.x=nx
        self.y=ny
