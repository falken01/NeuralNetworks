import pygame
import neat
from . import Bird
from . import Base
from . import Pipe
import time
import os
import random


class Game:
    WIN_WIDTH = 550
    WIN_HEIGHT = 800
    BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))


    def __init__(self):
        pygame.font.init()
        self.stat_font = pygame.font.SysFont("comicsans", 50)
        self.score = 0


    def draw_window(self,win, bird, pipes, base, score):
        win.blit(self.BG_IMG,(0,0))
        for pipe in pipes:
            pipe.draw(win)

        text = self.stat_font.render("Score: "+str(score),True,(255,255,255))
        win.blit(text, (self.WIN_WIDTH - 10 - text.get_width(),10))
        bird.draw(win)
        base.draw(win)
        pygame.display.update()


        base.draw(win)
    def main(self):
        pipes = [Pipe.Pipe(700)]
        bird = Bird.Bird(230,350)
        base = Base.Base(730)
        win = pygame.display.set_mode((self.WIN_WIDTH,self.WIN_HEIGHT))
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #bird.move()
            add_pipe=False
            rem = []
            for pipe in pipes:
                if pipe.collide(bird):
                    pass
                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True
                pipe.move()

            if add_pipe:
                self.score += 1
                pipes.append(Pipe.Pipe(700))

            for r in rem:
                pipes.remove(r)

            if bird.y+bird.img.get_height() >= 730:
                pass

            base.move()
            self.draw_window(win, bird, pipes, base, self.score)
        pygame.quit()
        quit()
