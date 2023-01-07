#!/usr/bin/env python

"""
	Script for testing already created Functionalities
"""

if __name__ == '__main__':
	# Section for testing the board generation part

	# Testing the board generation class instance
	"""
	from boardgeneration import BoardGeneration
	board = BoardGeneration(True, False)
	print("This is the original")
	board.initiate_normal_chess()
	board = BoardGeneration(True, False)
	print("This is the chess 960")
	board.initiate_chess_960()
	"""
	from moves import Moves
	from boardgeneration import BoardGeneration
	d = BoardGeneration(False, False)
	c = Moves()
	# print(c.RANK_8, c.BLACK_PIECES, c.FILE_A, d.WP)
	d.initiate_normal_chess()
	# print((d.BP|d.BH|d.BQ|d.BN|d.BB), d.WP)
	print(c.possible_moves_white("", 1125899906842624, d.WH, d.WQ, d.WN, d.WB, d.WK, d.BP, d.BH, d.BQ, d.BN, d.BB, d.BK))
