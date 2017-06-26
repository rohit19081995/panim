import cairosvg

from Space import Space
from common import *
from constants import *

class View(object):
	"""
	This class draws the Pobjects in the view.
	"""
	def __init__(self, space, resolution = DEFAULT_VIDEO_RESOLUTION, center = [0,0], size = [8,6]):
		super(View, self).__init__()
		self.resolution = resolution
		self.aspect_ratio = self.resolution[0]/self.resolution[1]
		self.space = space
		self.size = size
		self.center = center

	def maintain_aspect(self, xlen = None, ylen = None):
		'''
		Generates coordinates based on resolution and one of xlen or ylen.
		'''
		if xlen is not None:
			self.size = [xlen, xlen/self.aspect_ratio]
		elif ylen is not None:
			self.size = [ylen*self.aspect_ratio, ylen]
		else:
			raise PanimException('Must pass either xlen or ylen.')

	def move(self, center = [0,0]):
		'''
		Moves the viewport to the given coordinates. (Default is 0,0)
		'''
		self.center = center

	def zoom(self, scale):
		'''
		Zooms to the given scale.
		'''
		self.maintain_aspect(xlen = self.size[0]*scale)

	def capture_frame(self):
		'''
		Returns a png file as a bytes object.
		'''
		svg_string = '<svg width="%d" height="%d" viewBox="%f %f %f %f" shape-rendering="geometricPrecision">' % (self.resolution[0],
																			  self.resolution[1],
																			  self.center[0]-self.size[0]/2,
																			  self.center[1]-self.size[1]/2,
																			  self.size[0],
																			  self.size[1])
		for pobject, location in zip(self.space.pobjects, self.space.pobjects_locations):
			svg_string += pobject.get_pathstring('m %f %f' % (location[0], location[1]))
		svg_string += '</svg>'

		return cairosvg.svg2png(svg_string)