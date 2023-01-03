#!/usr/bin/env python

"""
	Script for running the whole game
"""

from engine.boardgeneration import BoardGeneration
from scene import place, dir_path
from piece.knight import Knight
from piece.bishop import Bishop
from piece.queen import Queen
from piece.rook import Rook
from piece.king import King
from piece.pawn import Pawn
from enum import Enum
import random
import pygame
import scene

class ChessPieceColor(Enum):
	white = "White"
	black = "Black"

class ChessPieceType(Enum):
	"""
		Class containing the enumeration of all the chess types
	"""
	king = King
	rook = Rook
	pawn = Pawn
	queen = Queen
	knight = Knight
	bishop = Bishop

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
		scen, clicked = place.Scene(App.screen), 0
		places_pressed = []
		while App.running:
			self.clock.tick(40)
			pressed = 0
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					App.running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					recent_pos, pressed = pygame.mouse.get_pos(), 1
					clicked += 1
				elif event.type == pygame.MOUSEBUTTONUP:
					# print(event)
					pass
			App.screen.fill(pygame.Color('gray'))
			scen.display_image()
			base8 = lambda a, b : (int(a/80)*80, int(b/80)*80)
			for i in self.array:
				try:
					if pressed == 1 :
						recent_int = base8(*recent_pos)
						if i.selected == True and clicked == 2: 
							setattr(i, "position", recent_int )
							i.selected = False
							# print("it has moved")
							# print(i.position, recent_int, clicked, i)
						elif clicked == 1 and i.position == recent_int:
							i.selected = True
							# print("it has been selected")
							# print(i.position, recent_int, clicked, i)
				except Exception as e:
					pass
				i.display(App.screen)
			if clicked >= 2:
				clicked = 0

			# App.t.draw()
			pygame.display.update()

		pygame.quit()
if __name__ == '__main__':
	App().run()