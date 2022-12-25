#!/usr/bin/env python

"""
	Script that has an instance of every chess piece
"""

class Piece:

	def __init__(self, position):
		self.position = position
		self.bitwise = 0

	def __dict__(self):
		pass

	def move(self):
		pass

	def capture(self):
		pass

	def __str__(self):
		pass

"""
import path
import sys
 
# directory reach
directory = path.path(__file__).abspath()
 
# setting path
sys.path.append(directory.parent.parent)
 
# importing
from parentdirectory.geeks import geek_method
"""