#!/usr/bin/env python

""" Script for generating the bitboard """

import random

class BoardGeneration():

	def __init__(self):
		""" Method for initializing the board """
		WP, WH, WQ, WN, WB, WK = 0, 0, 0, 0, 0, 0
		BP, BH, BQ, BN, BB, BK = 0, 0, 0, 0, 0, 0
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
		WP, WH, WQ, WN, WB, WK = 0, 0, 0, 0, 0, 0
		BP, BH, BQ, BN, BB, BK = 0, 0, 0, 0, 0, 0
		chessboard = [
			[" ", " ", " ", " ", " ", " ", " ", " "],
			["p", "p", "p", "p", "p", "p", "p", "p"],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			[" ", " ", " ", " ", " ", " ", " ", " "],
			["P", "P", "P", "P", "P", "P", "P", "P"],
			[" ", " ", " ", " ", " ", " ", " ", " "],
		]

		# Step 1
		random1 = int(random.random() * 8)
		chessboard[0][random1] = "b"
		chessboard[7][random1] = "B"

		# Step 2
		random2 = int(random.random() * 8)
		while (random2%2 == random1%2):
			random2 = int(random.random() * 8)
		chessboard[0][random2] = "b"
		chessboard[7][random2] = "B"

		# Step 3
		random3 = int(random.random() * 8)
		while (random2==random3 or random1==random3):
			random3 = int(random.random() * 8)
		chessboard[0][random3] = "q"
		chessboard[7][random3] = "Q"

		# Step 4
		random4a, counter, loop = int(random.random() * 5), 0, 0
		while counter - 1 < random4a:
			if chessboard[0][loop] == " ":
				counter += 1
			loop += 1
		chessboard[0][loop - 1] = "n"
		chessboard[7][loop - 1] = "N"
		random4b, counter, loop = int(random.random() * 4), 0, 0
		while counter - 1 < random4b:
			if chessboard[0][loop] == " ":
				counter += 1
			loop += 1
		chessboard[0][loop - 1] = "n"
		chessboard[7][loop - 1] = "N"

		# Step 5
		j = 0
		for i in range(8):
			if chessboard[0][i] == " ":
				if j == 0:
					chessboard[0][i] = "r"
					chessboard[7][i] = "R"
				if j == 1:
					chessboard[0][i] = "k"
					chessboard[7][i] = "K"
				if j == 2:
					chessboard[0][i] = "r"
					chessboard[7][i] = "R"
				j += 1
			if j >= 3:
				break
		self.array_to_bitboard(chessboard, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK)

	def array_to_bitboard(self, chessboard, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		""" Method that converts a string to binary """
		Binary = None
		for i in range(64):
			Binary = "0"*64
			Binary = Binary[i+1:] + "1" + "".join(list(Binary)[0:i])
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
		# print(WP, WH, WN, WB, WQ, WK, BP, BH, BN, BB, BQ, BK)
		self.draw_array(WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK)

	def convert_string_to_bitboard(self, binary):
		""" Method for converting string to bitboard """
		if binary[0] == "0":
			return self.generate_decimal(binary)
		return self.generate_decimal("1" + binary[2:]) * 2

	def draw_array(self, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		""" Method to rediagramatize the chessboard to verify that they all remain in their exact position """
		chessboard = [[" " for j in range(8)] for j in range(8)]
		for i in range(64):
			if (((WP >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "P"
			if (((WH >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "R"
			if (((WQ >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "Q"
			if (((WN >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "N"
			if (((WB >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "B"
			if (((WK >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "K"
			if (((BP >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "p"
			if (((BH >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "r"
			if (((BQ >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "q"
			if (((BN >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "n"
			if (((BB >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "b"
			if (((BK >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "k"
		for i in chessboard:
			print(i)

	def generate_decimal(self, binary):
		""" Function for deriving the denary form of the binary """
		w = 0
		for i in range(len(binary)):
			w += int(binary[-(i + 1)]) * (2 ** i)
		return w

