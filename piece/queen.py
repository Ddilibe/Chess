#!/usr/bin/env python

"""
	Script containing the Queen chess piece for the chess game
"""

from piece import Piece

class Queen(Piece):

	name = "queen"
	def __init__(self, image_path, color, symbol):
		super().__init__( image_path, color, symbol)
		self.name, self.piecevalue = "queen", 975