#!/usr/bin/env python

"""
	Script that has an instance of every chess piece
"""

class Piece:
	"""
		Parent class for the chess pieces
	"""

	def __init__(self, position):
		"""
			Method for declaraing and initiating the chess piece

			Parameters:
				self.position: Containing the position of the chess piece at all times
				self.bitwise: Containing the position of the chess piece in bitwise at all times
				self.__name: Containing the name of the chess piece
		"""
		self.position = position
		self.bitwise = 0
		self.__name = name

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