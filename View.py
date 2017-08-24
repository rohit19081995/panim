import cairosvg

from Space import Space
from BezierPobject import BPobject
from TexPobject import TexPobject
from common import *
from constants import *

class View(object):
	"""
	This class draws the Pobjects in the view.
	"""
	def __init__(self, space, resolution = DEFAULT_VIDEO_RESOLUTION, center = [0,0], size = [8,6], **kwargs):
		super(View, self).__init__()
		self.resolution = resolution
		self.aspect_ratio = self.resolution[0]/self.resolution[1]
		self.space = space
		self.size = size
		self.center = center
		self.kwargs = kwargs

		if self.kwargs is not None and 'background' not in self.kwargs:
			self.kwargs['background'] = 'white'
		elif self.kwargs is None:
			self.kwargs = {'background':'white'}

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

	def move(self, center = None, dx = None, dy = None):
		'''
		Moves the viewport to the given coordinates or by given dx/dy. (Default is 0,0)
		'''
		if center is not None:
			self.center = center
		else:
			if dx is not None:
				self.center[0]+=dx
			if dy is not None:
				self.center[1]+=dy

	def zoom(self, scale):
		'''
		Zooms to the given scale.
		'''
		self.maintain_aspect(xlen = self.size[0]*scale)

	def capture_frame(self):
		'''
		Returns a png file as a bytes object.
		'''
		defs_string = ''
		start_string = '<svg xmlns=\'http://www.w3.org/2000/svg\' xmlns:xlink=\'http://www.w3.org/1999/xlink\' width="%d" height="%d" viewBox="%f %f %f %f" shape-rendering="geometricPrecision">' % (self.resolution[0],
																			  self.resolution[1],
																			  self.center[0]-self.size[0]/2,
																			  self.center[1]-self.size[1]/2,
																			  self.size[0],
																			  self.size[1])
		objects_string = '<path d="M%f %f h %f v %f h %f Z" fill="%s"/>' % (self.center[0]-self.size[0]/2,
																	self.center[1]-self.size[1]/2,
																	self.size[0],
																	self.size[1],
																	-self.size[0],
																	self.kwargs['background'])
		for pobject, location, attributes_string in zip(self.space.pobjects, self.space.pobjects_locations, self.space.pobjects_attributes_list):
			if isinstance(pobject, BPobject):
				objects_string += '<path d="'
				objects_string += 'M %f %f' % (location[0], location[1])
				objects_string += pobject.get_pathstring() + '"'
				objects_string += attributes_string
				objects_string += '/>'
			elif isinstance(pobject, TexPobject):
				defs_string += pobject.get_defs()
				objects_string += pobject.get_pathstring(location)
			else:
				raise NotImplementedError()
		svg_string = '%s<defs>\n%s</defs>%s</svg>' % (start_string, defs_string, objects_string)

		print(svg_string)

		return cairosvg.svg2png(svg_string), svg_string