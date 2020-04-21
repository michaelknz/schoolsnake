from tkinter import*

class Score:
    def __init__(self,screen):
        self.scrn=screen
        self.score=0
        self.score_var=StringVar()
        self.Set_Score()
        self.label=Label(screen.root, textvariable=self.score_var)
        self.label.pack()
        self.scrn.canvas.create_window((screen.width-90, 0), anchor="nw", window=self.label)
        self.Set_Score()

    def Set_Score(self):
        self.score_var.set("Score: "+str(self.score)+" "*(15-len(str(self.score))))

    def Apple_Is_Eatten(self):
        self.score+=1
        self.Set_Score()