import pygame as pg

from Testing.Const import *
from Testing.Car import Car


class Core(object):
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H
                                           ))
        self.clock = pg.time.Clock()

        self.running = True

        self.keyR = False
        self.keyL = False
        self.keyD = False
        self.keyU = False

        # Задний фон размером со всё окно программы
        self.bg = pg.Surface((WINDOW_W, WINDOW_H))
        # Заполняем его каким-либо цветом
        self.bg.fill((255, 255, 255))

        self._init_objects()

    def _init_objects(self):
        # Тут можно создавать различные объекты,
        # например: главный игрок, монстры вокруг него и т.п;
        # Я для примера создаю простенький прямоугольник

        self.car1 = Car(size=(100, 50),
                        start_coords=(100, 100),
                        speed=5,
                        color=BLACK)

    def main_loop(self):
        while self.running:
            self.input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def input(self):
        for e in pg.event.get():

            if e.type == pg.QUIT:
                self.running = False

            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    self.keyR = True
                elif e.key == pg.K_LEFT:
                    self.keyL = True
                elif e.key == pg.K_DOWN:
                    self.keyD = True
                elif e.key == pg.K_UP:
                    self.keyU = True

            elif e.type == pg.KEYUP:
                if e.key == pg.K_RIGHT:
                    self.keyR = False
                elif e.key == pg.K_LEFT:
                    self.keyL = False
                elif e.key == pg.K_DOWN:
                    self.keyD = False
                elif e.key == pg.K_UP:
                    self.keyU = False

    def update(self):

        # Передаем в метод машины класс 'core', то есть самого себя
        self.car1.update(self)

    def render(self):
        # Заливаем всё задним фоном
        self.screen.blit(self.bg, (0, 0))

        # Вызывается метод машины 'render', который помещает эту машину на
        # экран
        self.car1.render(self.screen)

        pg.display.update()
