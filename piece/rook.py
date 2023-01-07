#!/usr/bin/env python

"""
	Script containing the Rook chess piece for the chess game
"""

from piece import Piece

class Rook(Piece):

	def __init__(self, image_path, color, symbol):
		Piece.__init__(self, image_path, color, symbol)
		self.name, self.piecevalue = "rook", 500