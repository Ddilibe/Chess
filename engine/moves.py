#!/usr/bin/env python

"""
	Script containing the moves for the chess engine
"""

import timeit
from typing import List, Tuple, Sequence
from chesstype import ChessPieceType

class Moves(object):
	"""docstring for Moves"""
	def __init__(self):
		""" Method to initiate the Moves class """
		self.FILE_A=72340172838076673
		self.FILE_H=-9187201950435737472
		self.FILE_AB=217020518514230019
		self.FILE_GH=-4557430888798830400
		self.RANK_1=-72057594037927936
		self.RANK_4=1095216660480
		self.RANK_5=4278190080
		self.RANK_8=255
		self.CENTRE=103481868288
		self.EXTENDED_CENTRE=66229406269440
		self.KING_SIDE=-1085102592571150096
		self.QUEEN_SIDE=1085102592571150095
		self.KING_B7=460039
		self.KNIGHT_C6=43234889994
		self.NOT_WHITE_PIECES = None
		self.BLACK_PIECES = None
		self.EMPTY = None

	def possible_moves_white_console(self, history, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		self.NOT_WHITE_PIECES = ~(WP|WH|WQ|WN|WB|WK|BK)
		self.BLACK_PIECES = (BP|BH|BQ|BN|BB)
		self.EMPTY = ~(WP|WH|WQ|WN|WB|WK|BP|BH|BQ|BN|BB|BK)
		self.time_expermiment(WP)
		movies = self.possible_wp(history, WP)
		return movies

	def visuals(self, lst: Sequence[List[]]) -> dict:
		pieces = {}
		for i in lst:
			try:
				if ChessPieceType(i):
					if pieces.get(i.symbol):
						pieces[i.symbol] += i.decimal
					else:
						pieces[i.symbol] = i.decimal
			except Exception as e:
				raise ChessTypeError()
		self.possible_moves_white_visuals("history", **pieces)
		return pieces

	def possible_moves_white_visuals(self, history, **kwargs):
		self.NOT_WHITE_PIECES = ~(kwargs["WP"]|kwargs['WH']|kwargs['WQ']|kwargs['WN']|kwargs['WB']|kwargs['WK']|kwargs['BK'])
		self.BLACK_PIECES = (kwargs["BP"]|kwargs["BH"]|kwargs["BQ"]|kwargs["BN"]|kwargs["BB"])
		self.EMPTY = ~(kwargs["WP"]|kwargs["WH"]|kwargs["WQ"]|kwargs["WN"]|kwargs["WB"]|kwargs["WK"]|kwargs["BP"]|kwargs["BH"]|kwargs["BQ"]|kwargs["BN"]|kwargs["BB"]|kwargs["BK"])
		self.time_expermiment(kwargs['WP'])
		movies = self.possible_wp(history, kwargs['WP'])
		return movies

	def possible_wp(self, history, WP):
		list_of_white_pawn_moves = ""

		# This first section of the possible wp is for the pawn to capture right
		PAWN_MOVES = (WP>>7)&self.BLACK_PIECES&~self.RANK_8&~self.FILE_A
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i/8+1) + str(i%8-1) + str(i/8) + str(i%8)
			i += 1

		# This second section is for calculating the possible moves for the white pawn to capture left
		PAWN_MOVES = (WP >> 9) & self.BLACK_PIECES &~ self.RANK_8 &~ self.FILE_H
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i/8+1) + str(i%8-1) + str(i/8) + str(i%8)
			i += 1

		# This third section id for calculating the possible moves for the white pawn to take one step forward
		PAWN_MOVES = (WP >> 8) & self.EMPTY &~ self.RANK_8
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i/8+1) + str(i%8) + str(i/8) + str(i%8)
			i += 1

		# This fourth section is for calcuting the possible moves for the white pawn to take two steps forward
		PAWN_MOVES = (WP >> 16) & self.EMPTY & (self.EMPTY >> 8) & self.RANK_4
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i/8+2) + str(i%8) + str(i/8) + str(i%8)

			i+= 1

		# Promotion Section
		# This fifth section is for the pawn promotion when it captures the enemy from the right
		PAWN_MOVES = (WP >> 7) & self.BLACK_PIECES & self.RANK_8 &~ self.FILE_A
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i%8-1) + str(i%8) + "QP" + str(i%8-1) + str(i%8) + "RP" + str(i%8-1) + str(i%8) + "BP" + str(i%8-1) + str(i%8) + "NP"
			i += 1

		# This Sixth section is for the pawn promotion when it captures the enemy from the left
		PAWN_MOVES = (WP >> 9) & self.BLACK_PIECES & self.RANK_8 &~ self.FILE_H
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i%8+1) + str(i%8) + "QP" + str(i%8+1) + str(i%8) + "RP" + str(i%8+1) + str(i%8) + "BP" + str(i%8+1) + str(i%8) + "NP"
			i += 1

		# The seventh section is for the pawn to be promoted when it moves one step forward with out capture
		PAWN_MOVES = (WP >> 8) & self.EMPTY & self.RANK_8
		i = self.count_trailing_zeros(PAWN_MOVES)
		while i < 64 - self.count_trailing_zeros(PAWN_MOVES):
			if (((PAWN_MOVES>>i)&1)==1):
				list_of_white_pawn_moves+= "" + str(i%8-1) + str(i%8) + "QP" + str(i%8-1) + str(i%8) + "RP" + str(i%8-1) + str(i%8) + "BP" + str(i%8-1) + str(i%8) + "NP"
			i += 1

		return list_of_white_pawn_moves

	def count_trailing_zeros(self, value):
		zero = 0
		# print(bin(value).split("0b")[1])
		if len(str(value)) > 1:
			for i in range(len(bin(value).split("0b")[1])):
				if str(value)[-i+1] != str(0):
					print(i)
					break
				zero += 1
		return zero

	def draw_bitboard(self, bitBoard):
		chessboard = [[" " for j in range(8)] for j in range(8)]
		urshift = lambda val, n : (val % 0x10) >> n
		for i in range(64):
			if ((urshift(bitBoard, i) & 1) == 1):
				chessboard[i/8][i%8] = "P"

		for i in chessboard:
			print(i)

	def time_expermiment(self, WP):
		looplength = 1000
		cal1, cal2 = self.etmethoda(looplength, WP), self.etmethodb(looplength, WP)
		print(f"That took {timeit.timeit(str(cal1), number=1)} to complete for the first method")
		print(f"That took {timeit.timeit(str(cal2), number=1)} to complete for the second method")

	def etmethoda(self, looplength, WP):
		for loop in range(looplength):
			PAWN_MOVES = (WP >> 7) & self.BLACK_PIECES &~ self.RANK_8 &~ self.FILE_A
			list_of_white_pawn_moves = ""
			for i in range(64):
				if ((PAWN_MOVES >> i) & 1) == 1:
					list += "" + (i/8+1) + (i%8-1) + (i/8) + (i%8)

	def etmethodb(self, looplength, WP):
		for loop in range(looplength):
			PAWN_MOVES = (WP >> 7) & self.BLACK_PIECES &~ self.RANK_8 &~ self.FILE_A
			list_of_white_pawn_moves, possibility = "", PAWN_MOVES &~ (PAWN_MOVES - 1)
			while possibility != 0:
				index = self.count_trailing_zeros(possibility)
				list += "" + (index/8+1) + (index%8-1) + (index/8) + (index%8)
				PAWN_MOVES &=~ possibility
				possibility = PAWN_MOVES &~ (PAWN_MOVES - 1)


	def in_figures(self, value: int) -> None:
		for i in range(8):
			try:
				print(str(bin(value)).split("0b")[1][i*8: (i+1)*8])
			except Exception:
				pass

	# def urshift(self, value):
	# 	"""
	# 		Abbrv for Unsigned Right Bit Shift Operator
	# 		Method for trying to implement the unsigned right bit shift operator in java
	# 	"""
		
