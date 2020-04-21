class Buf_Struct:
    def __init__(self,ref,type,x,y):
        self.ref=ref
        self.type=type
        self.x=x
        self.y=y

    def Set_coords(self,nx,ny):
        self.x=nx
        self.y=ny
