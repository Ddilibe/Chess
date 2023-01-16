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
	print(f"Black Piece:\n \tBlack Pawn: {d.BP}\n\tBlack Rock: {d.BH}\n\tBlack Queen: {d.BQ}\n\tBlack Knight: {d.BN}\n\tBlack Bishop: {d.BB}\n\tBlack king: {d.BK}\n")
	# Trying to derive the history format
	history = [
		{
		"time" : 24,
		"Side": "White",
		"old" : ()
		}
	]
	print(c.possible_moves_white_console("", 36028797018963968, d.WH, d.WQ, d.WN, d.WB, d.WK, d.BP, d.BH, d.BQ, d.BN, d.BB, d.BK))
	print(f"White Piece: {d.WP}\nBlack Piece: {c.BLACK_PIECES}\nRANK 8: {c.RANK_8}\nFILE A: {c.FILE_A}")
	d.draw_array()
	d.draw_array()
