#!/usr/bin/env python

"""
	Script that runs the test got the script containing the Scene class
"""

import unittest 
from scene.place import Scene
from manage import App

class TestScene(unittest.TestCase):

	def setUp(self):
		print("Seen you")
		self.app = App()
		self.scene = Scene(self.app.screen)

	def test_scene(self):
		self.assertEqual(self.scene, self.scene)

	def test_default_widget_size(self):
		self.assertEqual(self.app.screen.get_size(), (640,640),'incorrect default size')