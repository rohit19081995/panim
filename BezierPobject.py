import numpy as np

from Pobject import Pobject
from common import *

class BPobject(Pobject):
	'''This class implements a single path object made of lines, cubic bezier curves and move_to commands.'''
	def __init__(self):
		super().__init__()
		self.sub_BPobjects = []
		self.sub_BPobjects_locations = []
		self.generate_points()

	def generate_points(self):
		for bPobject in self.sub_BPobjects:
			bPobject.generate_points()
		self.get_points_and_mode()

	def get_points_and_mode(self):
		points = []
		points_modes = []
		for bPobject, location in zip(self.sub_BPobjects, self.sub_BPobjects_locations):
			points.append([location])
			points_modes.append('move')
			p, pm = bPobject.get_points_and_mode()
			points.extend(p)
			points_modes.extend(pm)

		self.points = points
		self.points_modes = points_modes
		return points, points_modes

	def get_pathstring(self):
		points_list, points_modes_list = self.get_points_and_mode()
		points_list = points_list
		points_modes_list = points_modes_list
		pathstring = ''
		for i in range(len(points_list)):
			points = points_list[i]
			mode = points_modes_list[i]
			if mode == 'smooth':
				if not is_closed([points[0], points_list[i-1][-1]]):
					pathstring += 'm %f %f' % (points[0][0], points[0][1])
				p1arr, p2arr = get_smooth_handle_points(points)
				for p0, p1, p2, p3 in zip(points[:-1], p1arr, p2arr, points[1:]):
					pathstring += 'c %f,%f %f,%f %f,%f' % (p1[0]-p0[0], p1[1]-p0[1], p2[0]-p0[0], p2[1]-p0[1], p3[0]-p0[0], p3[1]-p0[1])
			elif mode == 'jagged':
				if not is_closed([points[0], points_list[i-1][-1]]):
					pathstring += 'm %f %f' % (points[0][0], points[0][1])
				for point in points[1:]:
					pathstring += 'l %f %f' % (point[0], point[1])
			elif mode == 'move':
				pathstring  += 'M %f %f' % (points[-1][0], points[-1][1])
			else:
				raise PanimException('Invalid mode %s'%mode)
		return pathstring

	def scale(self, scale):
		self._scale(xscale=scale, yscale=scale)

	def xscale(self, scale):
		self._scale(xscale=scale)

	def yscale(self, scale):
		self._scale(yscale=scale)

	def _scale(self, xscale=1, yscale=1):
		for segment_index in range(len(self.points)):
			for point_index in range(len(self.points[segment_index])):
				self.points[segment_index][point_index][0]*=xscale
				self.points[segment_index][point_index][1]*=yscale

class Curve(BPobject):
	'''Implements a continuous cubic bezier curves'''
	def __init__(self, points=None, mode='smooth'):
		self.points = None
		self.mode = mode

	def get_points_and_mode(self):
		points = self.get_points()
		if points is None:
			raise PanimException('Points is None')
		return [points], [self.mode]

	def get_points(self):
		return self.points

class Move(BPobject):
	'''Implements a Move command'''
	def __init__(self, coordinates):
		self.points = points
		self.mode = 'move'

	def get_points_and_mode(self):
		points = self.get_points()
		if points is None:
			raise PanimException('Please implement a get_points function')
		return [points], [self.mode]

	def get_points(self):
		return self.points