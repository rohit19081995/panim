from common import *
from Space import Space

class Pobject(object):
	"""This class implements all objects that can be displayed"""
	def __init__(self, space, center = [0,0], size = [10,10]):
		super(Pobject, self).__init__()
		if not isinstance(space, Space):
			raise PanimException('space is not an instance of %s' % Space.__name__)
		self.space = space
		self.center = center
		self.size = size
		self.hidden = False
		self.direct_draw = False

	def hide(self):
		'''
		Hides the Pobject.
		'''
		self.hidden = True

	def unhide(self):
		'''
		Unhides the Pobject.
		'''
		self.hidden = False

	def crop(self, view):
		'''
		Crops the Pobject to the given View.
		'''
		pass

	def draw(self, view):
		'''
		Draws the Pobject on the given View.
		'''
		pass