 #!/usr/bin/env python

"""
	Script containing the King chess piece for the chess game
"""

from piece import Piece

class King(Piece):

	def __init__(self, image_path):
		Piece.__init__(self, image_path)
		self.name, self.piecevalue = "King", 32767