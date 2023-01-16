#!/usr/bin/env python

"""
	Script containing the moves for the chess engine
"""
import timeit
from typing import List, Tuple, Sequence
from enum import Enum
# from engine import a

class Moves(object):
	"""docstring for Moves"""
	def __init__(self):
			Rank 8 Represents the Top of the chessboard
		""" 
			Method to initiate the Moves class. C (uppercase) would be used to represent the chess piece.

			Variables:
				:vari @self.RANK_8 [int] This variable contains all the chess pieces on the top value.
				Before:
					["C", "C", "C", "C", "C", "C", "C", "C"],
					[" ", " ", " ", " ", " ", " ", " ", " "],
					[" ", " ", " ", " ", " ", " ", " ", " "],
					[" ", " ", " ", " ", " ", " ", " ", " "],
					[" ", " ", " ", " ", " ", " ", " ", " "],
					[" ", " ", " ", " ", " ", " ", " ", " "],
					[" ", " ", " ", " ", " ", " ", " ", " "],
					[" ", " ", " ", " ", " ", " ", " ", " "]
		"""
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
		self.rankmaster8 = [255, 65280, 16711680, 4278190080, 1095216660480, 280375465082880, 71776119061217280, 18374686479671623680]
		self.filemaster8 = {72340172838076673, 144680345676153346, 289360691352306692, 578721382704613384, 1157442765409226768, 2314885530818453536, 4629771061636907072, 9259542123273814144}

	def possible_moves_white_console(self, history, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		self.NOT_WHITE_PIECES = ~(WP|WH|WQ|WN|WB|WK|BK)
		self.BLACK_PIECES = (BP|BH|BQ|BN|BB)
		self.EMPTY = ~(WP|WH|WQ|WN|WB|WK|BP|BH|BQ|BN|BB|BK)
		self.time_expermiment(WP)
		movies = self.possible_wp(history, WP, BP)
		return movies

	def visuals(self, lst: Sequence[list]) -> dict:
		pieces = {}
		for i in lst:
			try:
				if ChessPieceType(i):
					if pieces.get(i.symbol):
						pieces[i.symbol] += i.decimal
					else:
						pieces[i.symbol] = i.decimal
			except Exception as e:
				raise ChessTypeError("Chess Piece Type not found")
		self.possible_moves_white_visuals("history", **pieces)
		return pieces

	def possible_moves_white_visuals(self, history, **kwargs):
		self.NOT_WHITE_PIECES = ~(kwargs["WP"]|kwargs['WH']|kwargs['WQ']|kwargs['WN']|kwargs['WB']|kwargs['WK']|kwargs['BK'])
		self.BLACK_PIECES = (kwargs["BP"]|kwargs["BH"]|kwargs["BQ"]|kwargs["BN"]|kwargs["BB"])
		self.EMPTY = ~(kwargs["WP"]|kwargs["WH"]|kwargs["WQ"]|kwargs["WN"]|kwargs["WB"]|kwargs["WK"]|kwargs["BP"]|kwargs["BH"]|kwargs["BQ"]|kwargs["BN"]|kwargs["BB"]|kwargs["BK"])
		self.time_expermiment(kwargs['WP'])
		movies = self.possible_wp(history, kwargs['WP'])
		return movies

	def possible_wp(self, history, WP, BP):
		"""
			Method is meant to predict the possible moves that a particular white pawn can make. 

			Args:
				:param @history [List[Time, str, Tuple, ChessPieceType]] - This is a list of tuples. Each tuple contains
				the moves made while the chess game is on. This was enabled due to enable people make the en passant move in 
				the chess software. Due to the way python's lists were structured, list can only be updated. The format of the
				history will be 
				< 	Time-move-was-taken
					Which-side-took-the-move
					position-before-the-move-was-taken
					position-after-the-move-was-taken
					instance-of-chess-board-after-the-move-was-taken
						chess-piece-name
						chess-piece-decimal
						chess-piece-bitwise
				>
				:param @WP [ChessPieceType] - This argument contains the pawn instance of the chess piece that was clicked.
		"""
		list_of_white_pawn_moves = []

		# This first section of the possible wp is for the pawn to capture right
		"""
			WP is the mathematical position of the pawn that we want to move.
			WP is left wise shift to 7 because it attempting at a right capture
			Before:
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", "P", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "]
			After:
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", "*", " ", " "],
			[" ", " ", " ", " ", "P", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "]
			* (asterisks) - represents the possible capture on the right.
			Then it makes a bitwise exclusive "and" with Black_Piece variable
			If there is a possible capture on the right, Operation moves to the next bitwise operation. 
			Else, The operation for the part is done
			The next step it takes is to make a bitwise AND operation against a bitwise not Rank 8 position

		"""
		PAWN_MOVES = (WP>>7)&self.BLACK_PIECES&~self.RANK_8&~self.FILE_A
		possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		while possibility != 0:
			i = self.count_trailing_zeros(PAWN_MOVES)
			list_of_white_pawn_moves.append(((int(i/8+1),int(i%8-1)),(int(i/8),int(i%8))))
			PAWN_MOVES&=~possibility
			possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# This second section is for calculating the possible moves for the white pawn to capture left
		# PAWN_MOVES = (WP >> 9) & self.BLACK_PIECES &~ self.RANK_8 &~ self.FILE_H
		# possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		# while possibility != 0:
		# 	i = self.count_trailing_zeros(PAWN_MOVES)
		# 	list_of_white_pawn_moves.append(((int(i/8+1),int(i%8-1)),(int(i/8),int(i%8))))
		# 	PAWN_MOVES&=~possibility
		# 	possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# This third section id for calculating the possible moves for the white pawn to take one step forward
		# PAWN_MOVES = (WP >> 8) & self.EMPTY &~ self.RANK_8
		# possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		# while possibility != 0:
		# 	i = self.count_trailing_zeros(PAWN_MOVES)
		# 	list_of_white_pawn_moves.append(((int(i/8+1),int(i%8)),(int(i/8),int(i%8))))
		# 	PAWN_MOVES&=~possibility
		# 	possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# This fourth section is for calcuting the possible moves for the white pawn to take two steps forward
		# PAWN_MOVES = (WP >> 16) & self.EMPTY & (self.EMPTY >> 8) & self.RANK_4
		# possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		# while possibility != 0:
		# 	i = self.count_trailing_zeros(PAWN_MOVES)
		# 	list_of_white_pawn_moves.append(((int(i/8+2),int(i%8)), (int(i/8),int(i%8))))
		# 	PAWN_MOVES&=~possibility
		# 	possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# Promotion Section
		# This fifth section is for the pawn promotion when it captures the enemy from the right
		# PAWN_MOVES = (WP >> 7) & self.BLACK_PIECES & self.RANK_8 &~ self.FILE_A
		# possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		# while possibility != 0:
		# 	i = self.count_trailing_zeros(PAWN_MOVES)
		# 	list_of_white_pawn_moves.append(((int(i%8-1),int(i%8),"QP"),(int(i%8-1),int(i%8),"RP"),(int(i%8-1),int(i%8),"BP"),(int(i%8-1),int(i%8),"NP")))
		# 	PAWN_MOVES&=~possibility
		# 	possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# This Sixth section is for the pawn promotion when it captures the enemy from the left
		# PAWN_MOVES = (WP >> 9) & self.BLACK_PIECES & self.RANK_8 &~ self.FILE_H
		# possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		# while possibility != 0:
		# 	i = self.count_trailing_zeros(PAWN_MOVES)
		# 	list_of_white_pawn_moves.append(((int(i%8+1),int(i%8), "QP"), (int(i%8+1),int(i%8),"RP"),(int(i%8+1),int(i%8),"BP"),(int(i%8+1),int(i%8),"NP")))
		# 	PAWN_MOVES&=~possibility
		# 	possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# The seventh section is for the pawn to be promoted when it moves one step forward with out capture
		# PAWN_MOVES = (WP >> 8) & self.EMPTY & self.RANK_8
		# possibility = PAWN_MOVES&~(PAWN_MOVES-1)
		# while possibility != 0:
		# 	i = self.count_trailing_zeros(PAWN_MOVES)
		# 	list_of_white_pawn_moves.append(((int(i%8-1),int(i%8),"QP"),(int(i%8-1),int(i%8),"RP"),(int(i%8-1),int(i%8),"BP"),(int(i%8-1),int(i%8),"NP")))
		# 	PAWN_MOVES&=~possibility
		# 	possibility=PAWN_MOVES&~(PAWN_MOVES-1)

		# # This section is for calculating enpassant
		# if len(history) >= 4:
			# oldpawn = history[-1]
			# Assuming that the histroy variable is a list.
			# The statement above is meant to incicate that we are collecting the last digits in the histroy
			# The statement below says confirming that the last history is an instance of a pawn and it is a black pawn,
			# We can move on to the next step. Else, no siginificant move would be made.
			# if oldpawn.name == "BP":
				# Trying to explain a code that was written in java in python. 
				# charat returns the instanr of the 
				# 6 - 6
				# if oldpawn.old[1] - oldpawn.new[1] == 2:
					# possibility = (WP << 1)&BP&RANK_5&~FILE_A&filemaster8[oldpawn.new[1]]
					# if possibility != 0:
						# i = self.count_trailing_zeros(PAWN_MOVES)
					# 	list_of_white_pawn_moves.append(((int(i%8-1),int(i%8),"E"), (int(i/8), int(i%8+1))))
					# possibility = (WP >> 1)&BP&RANK_5&~FILE_H&filemaster8[oldpawn.new[1]]
					# if possibility != 0:
					# 	i = self.count_trailing_zeros(PAWN_MOVES)
					# 	list_of_white_pawn_moves.append(((int(i%8+1),int(i%8),"E"), (int(i/8), int(i%8-1))))

		return list_of_white_pawn_moves

	def count_trailing_zeros(self, value: int) -> int:
		zeros = str(value)
		return len(zeros) - len(zeros.rstrip('0'))

	def draw_bitboard(self, bitBoard):
		chessboard = [[" " for j in range(8)] for j in range(8)]
		urshift = lambda val, n : (val % 0x10) >> n
		for i in range(64):
			if ((urshift(bitBoard, i) & 1) == 1):
				chessboard[i/8][i%8] = "P"

		for i in chessboard:
			print(i)

	def time_expermiment(self, WP: int) -> None:
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
		
# class ChessPieceColor(Enum):
# 	""" Class containing declaration for the chess piece"""
# 	white = "White"
# 	black = "Black"

# class ChessPieceType(Enum):
# 	"""
# 		Class containing the enumeration of all the chess types
# 	"""
# 	king = King
# 	rook = Rook
# 	pawn = Pawn
# 	queen = Queen
# 	knight = Knight
# 	bishop = Bishop

# class ChessPieceError(Exception):
# 	pass