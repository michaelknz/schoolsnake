from tkinter import*

class Screen:
    def __init__(self, w, h, del_x, del_y, col):
        self.root = Tk()
        self.width = w
        self.color = col
        self.height = h
        self.del_x = del_x
        self.del_y = del_y
        self.root.title("Snake")
        self.root.resizable(height=False,width=False)
        self.root.geometry(str(self.width)+"x"+str(self.height)+"+"+str(self.del_x)+"+"+str(self.del_y))
        self.root.attributes('-toolwindow', True)
        self.Create_Canvas()

    def Canvas_Pack(self):
        self.canvas.pack()

    def Destroy_Canvas(self):
        self.canvas.destroy()

    def Create_Canvas(self):
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg= self.color)
        self.Canvas_Pack()