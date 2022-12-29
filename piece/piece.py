#!/usr/bin/env python

"""
	Script that has an instance of every chess piece
"""

import pygame

class Piece(object):
	"""
		Parent class for the chess pieces
	"""

	def __init__(self, image_path):
		"""
			Method for declaraing and initiating the chess piece

			Parameters:
				self.position: Containing the position of the chess piece at all times
				self.bitwise: Containing the position of the chess piece in bitwise at all times
				self.__name: Containing the name of the chess piece
				self.image_path: Containing the path to the image
		"""
		self.position = 0
		self.bitwise = 0
		self.__name = None
		self.image_path = image_path
		self.decimal = 0

	def __dict__(self):
		""" Method for the ditionary representation of the class """

		pass

	def move(self):
		pass

	def capture(self):
		pass

	def __str__(self, name):
		""" Method for changing the string representation of the class """
		return f"<{Piece} -- {name}>"

	def display(self, app):
		""" Method for displaying the chess piece on the board """
		img = pygame.image.load(self.image_path)
		app.blit(img, self.position)

	def generate_position(self, width, height):
		""" Method for generating the position using the bitwise """
		one = self.bitwise
		ones = self.bitwise.index("1")
		ones = 64 - ones
		ones = "".join((oct(ones)).split("0o")[1])
		print(ones, width, height)
		if ones == "100":
			self.position = (width/80, height/80)
			return
		if len(ones) == 1:
			if int(ones) <= 8:
				self.position = (0, height/int(ones))
			else:
				self.position = (20, height/int(ones))
			return
		try:
			width = width/int(list(ones)[0])
		except Exception as e:
			pass
		else:
			width = 0
		try:
			height = height/int(list(ones)[1])
		except Exception as e:
			pass
		else:
			height = 0
		self.position = (width , height)




"""
import path
import sys
 
# directory reach
directory = path.path(__file__).abspath()
 
# setting path
sys.path.append(directory.parent.parent)
 
# importing
from parentdirectory.geeks import geek_method
"""