#!/usr/bin/env python

""" Script for generating the bitboard """

import random

class BoardGeneration():

	def __init__(self, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK):
		""" Method for initializing the board """
		self.WP, self.WH, self.WQ, self.WN, self.WB, self.WK = WP, WH, WQ, WN, WB, WK
		self.BP, self.BH, self.BQ, self.BN, self.BB, self.BK = BP, BH, BQ, BN, BB, BK
		self.WP.decimal, self.WH.decimal, self.WQ.decimal, self.WN.decimal, self.WB.decimal, self.WK.decimal = 0, 0, 0, 0, 0, 0
		self.BP.decimal, self.BH.decimal, self.BQ.decimal, self.BN.decimal, self.BB.decimal, self.BK.decimal = 0, 0, 0, 0, 0, 0
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
		# self.array_to_bitboard(chessboard, WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK)

	def initiate_chess_960(self):
		self.WP.decimal, self.WH.decimal, self.WQ.decimal, self.WN.decimal, self.WB.decimal, self.WK.decimal = 0, 0, 0, 0, 0, 0
		self.BP.decimal, self.BH.decimal, self.BQ.decimal, self.BN.decimal, self.BB.decimal, self.BK.decimal = 0, 0, 0, 0, 0, 0
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
		self.array_to_bitboard(chessboard)

	def array_to_bitboard(self, chessboard):
		""" 
		Method that converts a string to binary

		Explanation:
			First of all, Binary variable name is declared
			The following steps is what took place in the for loop

			Step 1:
			The binary variable is assigned to a string containing 64 zeros
			Binary = "000000000000000000000000000000000000000000000000000000000000000"

			Step 2:
			For every value of i, it creates the bitwise format for the value
			if i = 1:
				Binary = "000000000000000000000000000000000000000000000000000000000000010"
			if i = 2:
				Binary = "000000000000000000000000000000000000000000000000000000000000100"

			Step 3:
			Since the loop is to run 64 times and the bitboard representation of the board is 64, 
			the section of the board is identified.

			Step 4:
			This step compares the positions gotten in the board and the value and converts it to decimal
			number before assigning it to a variable.

		"""
		Binary, general_list = None, []
		for i in range(64):
			Binary = "0"*64
			Binary = Binary[i+1:] + "1" + "".join(list(Binary)[0:i])
			value = chessboard[int(i/8)][int(i%8)]
			if value == "P":
				self.WP.decimal += self.convert_string_to_bitboard(Binary)
				self.WP.bitwise = Binary
				general_list.append(self.WP)
			elif value == "R":
				self.WH.decimal += self.convert_string_to_bitboard(Binary)
				self.WH.bitwise = Binary
				general_list.append(self.WH)
			elif value == "N":
				self.WN.decimal += self.convert_string_to_bitboard(Binary)
				self.WN.bitwise = Binary
				general_list.append(self.WN)
			elif value == "B":
				self.WB.decimal += self.convert_string_to_bitboard(Binary)
				self.WB.bitwise = Binary
				general_list.append(self.WB)
			elif value == "Q":
				self.WQ.decimal += self.convert_string_to_bitboard(Binary)
				self.WQ.bitwise = Binary
				general_list.append(self.WQ)
			elif value == "K":
				self.WK.decimal += self.convert_string_to_bitboard(Binary)
				self.WK.bitwise = Binary
				general_list.append(self.WK)
			elif value == "p":
				self.BP.decimal += self.convert_string_to_bitboard(Binary)
				self.BP.bitwise = Binary
				general_list.append(self.BP)
			elif value == "r":
				self.BH.decimal += self.convert_string_to_bitboard(Binary)
				self.BH.bitwise = Binary
				general_list.append(self.BH)
			elif value == "n":
				self.BN.decimal += self.convert_string_to_bitboard(Binary)
				self.BN.bitwise = Binary
				general_list.append(self.BN)
			elif value == "b":
				self.BB.decimal += self.convert_string_to_bitboard(Binary)
				self.BB.bitwise = Binary
				general_list.append(self.BB)
			elif value == "q":
				self.BQ.decimal += self.convert_string_to_bitboard(Binary)
				self.BQ.bitwise = Binary
				general_list.append(self.BQ)
			elif value == "k":
				self.BK.decimal += self.convert_string_to_bitboard(Binary)
				self.BK.bitwise = Binary
				general_list.append(self.BK)
			else:
				pass
		# print(WP, WH, WN, WB, WQ, WK, BP, BH, BN, BB, BQ, BK)
		# self.draw_array(WP, WH, WQ, WN, WB, WK, BP, BH, BQ, BN, BB, BK)
		return (general_list)

	def convert_string_to_bitboard(self, binary):
		""" Method for converting string to bitboard """
		if binary[0] == "0":
			return self.generate_decimal(binary)
		return self.generate_decimal("1" + binary[2:]) * 2

	def draw_array(self):
		""" 
			Method to rediagramatize the chessboard to verify that they all remain in their exact position 
			This method was implemented to make sure that the idea behind the board remains the same and bug free.
			
			Explanation:
				First of all, it creates a 2-dimensional list containing empty string types.
				Then it goes through a loop in a range of 64

				It then takes I and compares i with all the arguments passed in
				It compares it through bitwise operations.

				It takes one of the argument and right shift it the number of times i is then bitwise and it to 1.
				If the value gotten is one, the it records it on the empty chess board

		"""
		chessboard = [[" " for j in range(8)] for j in range(8)]
		for i in range(64):
			if (((self.WP.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "P"
			if (((self.WH.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "R"
			if (((self.WQ.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "Q"
			if (((self.WN.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "N"
			if (((self.WB.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "B"
			if (((self.WK.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "K"
			if (((self.BP.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "p"
			if (((self.BH.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "r"
			if (((self.BQ.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "q"
			if (((self.BN.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "n"
			if (((self.BB.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "b"
			if (((self.BK.decimal >> i) & 1) == 1):
				chessboard[int(i/8)][int(i%8)] = "k"
		for i in chessboard:
			print(i)

	def generate_decimal(self, binary):
		""" Function for deriving the denary form of the binary """
		w = 0
		for i in range(len(binary)):
			w += int(binary[-(i + 1)]) * (2 ** i)
		return w

