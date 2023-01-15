#!/usr/bin/env python

"""
	Script that runs the test got the script containing the Scene class
"""

import unittest 
from scene.place import Scene
from manage import App

class TestScene(TestCase):

	def setUp(self):
		print("Seen you")
		self.scene = Scene(App.screen)

	def test_scene(self):
		self.assertEqual(self.scene, self.scene)

	def test_default_widget_size(self):
		self.assertEqual(self.widget.size(), (50,50),'incorrect default size')