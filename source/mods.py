from tkinter import *
from snake_class import Snake
from apple_class import Apple
from timer import Timer
from bufs import Bufs
from score import Score
from leader_table import Leader_Table

def mode_1(screen):
    snake = Snake(screen)
    apple = Apple(screen)

    def Key_Board_Ev(event):
        if event.keysym == 'd':
            snake.KeyBoard(1, 0)
        if event.keysym == 'a':
            snake.KeyBoard(-1, 0)
        if event.keysym == 'w':
            snake.KeyBoard(0, -1)
        if event.keysym == 's':
            snake.KeyBoard(0, 1)

    screen.root.bind('<Key>', Key_Board_Ev)

    while True:
        snake.S_Update()
        if snake.Is_Exit:
            break
        if snake.body_pos[0] == apple.apple_pos:
            apple.Apple_Is_Eatten()
            snake.Apple_Is_Eatten()
        snake.Wall()
        screen.root.update()

def mode_2(screen):
    leader_table=Leader_Table(screen)
    snake = Snake(screen)
    apple = Apple(screen)

    def Key_Board_Ev(event):
        if event.keysym == 'd':
            snake.KeyBoard(1, 0)
        if event.keysym == 'a':
            snake.KeyBoard(-1, 0)
        if event.keysym == 'w':
            snake.KeyBoard(0, -1)
        if event.keysym == 's':
            snake.KeyBoard(0, 1)

    screen.root.bind('<Key>', Key_Board_Ev)

    otimer=Timer(screen)
    bufs=Bufs(screen)
    score=Score(screen)

    while True:
        otimer.Update()
        snake.S_Update()
        if(otimer.min_col<0 or snake.Is_Exit):
            break
        if snake.body_pos[0] == apple.apple_pos:
            apple.Apple_Is_Eatten()
            snake.Apple_Is_Eatten()
            bufs.Is_Gen()
            score.Apple_Is_Eatten()
        snake.Wall()
        nbuf=bufs.Is_Buffed(snake.body_pos[0])
        bufs.Clean_buf()
        if nbuf!=-1:
            if nbuf=='tplus':
                otimer.sec_col+=40
                otimer.min_col+=int(otimer.sec_col//60)
                otimer.sec_col=otimer.sec_col%60
            if nbuf=='lucky':
                ind=bufs.Gen_Rand_Int(0,1)
                if ind==1:
                    score.score+=100
                    score.Set_Score()
                else:
                    break
        screen.root.update()
    leader_table.Update_T(score.score)