#!/usr/bin/env python3

""" Script for declaring the chess type """

from piece.knight import Knight
from piece.bishop import Bishop
from piece.queen import Queen
from piece.rook import Rook
from piece.king import King
from piece.pawn import Pawn
from enum import Enum

class ChessPieceColor(Enum):
	""" Class containing declaration for the chess piece"""
	white = "White"
	black = "Black"

class ChessPieceType(Enum):
	"""
		Class containing the enumeration of all the chess types
	"""
	king = King
	rook = Rook
	pawn = Pawn
	queen = Queen
	knight = Knight
	bishop = Bishop

class ChessPieceError(Exception):
	pass