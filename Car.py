import pygame as pg


class Car():
	def __init__(self, size: tuple, start_coords: tuple, speed: int, color: tuple):

		# Текстурка предмета
		self.texture = pg.Surface(size)
		self.texture.fill(color)

		# Для проверки коллизий используется невидимый прямоугольник
		self.rect = pg.Rect(start_coords, size)

		self.speed = speed

	def update(self, core):
		"""
		В эту функцию передается главный класс программы - класс core.
		Это необходимо для того, чтобы данному методу были доступны
		абсолютно все части и классы программы. Сейчас это не обязательно,
		тут всё очень просто, но дальше, если будет прописываться коллизия
		с другими предметами, это очень поможет.
		"""

		if core.keyR:
			self.rect.x += self.speed
		if core.keyL:
			self.rect.x -= self.speed
		if core.keyU:
			self.rect.y -= self.speed
		if core.keyD:
			self.rect.y += self.speed

	def render(self, screen):

		# Текстура данного объекта помещается на экран
		screen.blit(self.texture, (self.rect.x, self.rect.y))
