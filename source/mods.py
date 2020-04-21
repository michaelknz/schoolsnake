from tkinter import *
from snake_class import Snake
from apple_class import Apple
from timer import Timer
from bufs import Bufs
from score import Score

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
        if nbuf!=-1:
            if nbuf=='tplus':
                otimer.sec_col+=40
                otimer.min_col+=int(otimer.sec_col//60)
                otimer.sec_col=otimer.sec_col%60
        screen.root.update()