 #!/usr/bin/env python

"""
	Script containing the bishop chess piece for the chess game
"""

from piece import Piece

class Bishop(Piece):

	def __init__(self, image_path, color):
		Piece.__init__(self, image_path, color)
		self.name, self.piecevalue = "bishop", 325