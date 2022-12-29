#!/usr/bin/env python

"""
	Script for running the whole game
"""

from engine.boardgeneration import BoardGeneration
from piece.knight import Knight
from piece.bishop import Bishop
from piece.queen import Queen
from piece.rook import Rook
from piece.king import King
from piece.pawn import Pawn
from scene import place, dir_path
import random
import pygame
import scene

class App:
	""" Create a single-window app with multiple Scenes. """

	def __init__(self):
		""" initiatize pygame and the application. """
		pygame.init()
		self.clock = pygame.time.Clock()
		App.screen = pygame.display.set_mode((640, 640))
		App.name = pygame.display.set_caption("Chess 2D Game")
		App.running = True
		self.__scene = 0
		self.white_piece, self.black_piece, color = [], [], "black"
		path = f"{dir_path}/media/image/image_1/"

		self.board = BoardGeneration(False, True)
		if self.board.choose:
			self.array = self.board.initiate_normal_chess()
		else:
			self.array = self.board.initiate_chess_960()

	def run(self):
		"""Run the main event loop."""
		scen = place.Scene(App.screen)
		places_pressed = []
		while App.running:
			self.clock.tick(40)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					App.running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					places_pressed.append(event)
				elif event.type == pygame.MOUSEBUTTONUP:
					# print(event)
					pass

			App.screen.fill(pygame.Color('gray'))
			scen.display_image()
			for i in self.array:
				i.display(App.screen)
			# App.t.draw()
			pygame.display.update()

		pygame.quit()
if __name__ == '__main__':
	App().run()