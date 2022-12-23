#!/usr/bin/env python

""" Script for generating the bitboard """

class BoardGeneration():

	def __init__(self):
		""" Method for initializing the board """
		WP, WH, WQ, WN, WB, WK = "0L","0L","0L","0L","0L","0L"
		BP, BH, BQ, BN, BB, BK = "0L","0L","0L","0L","0L","0L"
		chessboard = [
			["r", "n", "b", "q", "k", "b", "n", "r"],
			["p", "p", "p", "p", "p", "p", "p", "p"],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			["P", "P", "P", "P", "P", "P", "P", "P"],
			["R", "N", "B", "Q", "K", "B", "N", "R"]
		]
		self.array_to_bitboard(chessboard, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK)

	def initiate_chess_960(self):
		pass

	def array_to_bitboard(self, chessboard, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		""" Method that converts a string to binary """
		Binary = None
		for i in range(64):
			Binary = "0"*65
			Binary = Binary[i+1] + "1" + "".join(list(Binary)[0:i])
			value = chessboard[int(i/8)][int(i%8)]
			if value == "P":
				WP += self.convert_string_to_bitboard(Binary)
			elif value == "R":
				WH += self.convert_string_to_bitboard(Binary)
			elif value == "N":
				WN += self.convert_string_to_bitboard(Binary)
			elif value == "B":
				WB += self.convert_string_to_bitboard(Binary)
			elif value == "Q":
				WQ += self.convert_string_to_bitboard(Binary)
			elif value == "K":
				WK += self.convert_string_to_bitboard(Binary)
			elif value == "p":
				BP += self.convert_string_to_bitboard(Binary)
			elif value == "r":
				BH += self.convert_string_to_bitboard(Binary)
			elif value == "n":
				BN += self.convert_string_to_bitboard(Binary)
			elif value == "b":
				BB += self.convert_string_to_bitboard(Binary)
			elif value == "q":
				BQ += self.convert_string_to_bitboard(Binary)
			elif value == "k":
				BK += self.convert_string_to_bitboard(Binary)
			else:
				pass
		self.draw_array(WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK)

	def convert_string_to_bitboard(self, binary):
		""" Method for converting string to bitboard """
		return bin(int(binary))

	def draw_array(self, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		""" Method to rediagramatize the chessboard to verify that they all remain in their exact position """
		chessboard = [[" " for j in range(8)] for j in range(8)]
		for i in range(64):
			if (((int(WP.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "P"
			if (((int(WH.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "R"
			if (((int(WQ.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "Q"
			if (((int(WN.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "N"
			if (((int(WB.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "B"
			if (((int(WK.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "K"
			if (((int(BP.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "p"
			if (((int(BH.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "r"
			if (((int(BQ.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "q"
			if (((int(BN.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "n"
			if (((int(BB.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "b"
			if (((int(BK.split("0b")[1]) >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "k"
		for i in chessboard:
			print(i)
		print(help(list))