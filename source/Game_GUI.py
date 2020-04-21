from PIL import Image, ImageTk
import tkinter

class GUI:
    def __init__(self, scr):
        self.scrn = scr
        self.Start_Screen()

    def Loop(self):
        while True:
            if self.Is_Over:
                break
            self.scrn.root.update()

    def Mode_1_Func(self):
        self.Is_Over=True
        self.mode_1=True

    def Mode_2_Func(self):
        self.Is_Over = True

    def Start_Screen(self):
        self.scrn.Destroy_Canvas()
        self.scrn.Create_Canvas()
        self.Is_Over = False
        self.quite = False
        self.mode_1 = False
        self.pilImage = Image.open("snake.jpg", "r")
        self.img = ImageTk.PhotoImage(self.pilImage)
        self.background_label = tkinter.Label(self.scrn.root, image=self.img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.start_mod1 = tkinter.Button(text="Classical Mode", background="brown", foreground="white", height=1, width=50, command=self.Mode_1_Func)
        self.start_mod2 = tkinter.Button(text="Advanture Mode", background="brown", foreground="white", height=1, width=50, command=self.Mode_2_Func)
        self.start_mod1.pack()
        self.start_mod2.pack()
        self.scrn.canvas.create_window((self.scrn.width // 2 - 170, self.scrn.height // 2 - 110), anchor="nw", window=self.start_mod1)
        self.scrn.canvas.create_window((self.scrn.width // 2 - 170, self.scrn.height // 2 - 70), anchor="nw", window=self.start_mod2)
        self.Loop()
        self.scrn.Destroy_Canvas()

    def End_Screen(self):
        self.Is_Over=False
        self.quite = False
        self.mode_1 = False
        self.scrn.Destroy_Canvas()
        self.scrn.Create_Canvas()
        self.background_label = tkinter.Label(self.scrn.root, image=self.img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.exit = tkinter.Button(text="Leave Game", background="brown", foreground="white", height=1, width=50, command=self.Leave_Func)
        self.continue_ = tkinter.Button(text="Continue", background="brown", foreground="white", height=1, width=50, command=self.Start_Screen)
        self.exit.pack()
        self.continue_.pack()
        self.scrn.canvas.create_window((self.scrn.width // 2 - 170, self.scrn.height // 2 - 70), anchor="nw", window=self.continue_)
        self.scrn.canvas.create_window((self.scrn.width // 2 - 170, self.scrn.height // 2 - 110), anchor="nw", window=self.exit)
        self.Loop()
        self.scrn.Destroy_Canvas()

    def Leave_Func(self):
        self.quite = True
        self.Is_Over = True