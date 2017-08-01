import numpy as np

from Pobject import Pobject
from BezierPobject import Curve

class Line(Curve):
	'''
	This class implements a line.
	'''
	def __init__(self, x1, y1, dx, dy, **kwargs):
		super().__init__(mode='jagged')
		self.start = [x1, y1]
		self.end = [dx,dy]

		# SVG Path format:
		# l x y

	def generate_points(self):
		self.points = [self.start, self.end]

	# def _scale(self, xscale=1, yscale=1):
	# 	self.x1 = self.x1*xscale
	# 	self.dx = self.dx*xscale
	# 	self.dy = self.dy*yscale
	# 	self.y1 = self.y1*yscale

class Arc(Curve):
	'''
	This class implements an arc.
	'''
	def __init__(self, rx=1, ry=1, start_angle=0, end_angle=2*np.pi, phi=0, no_of_points=10):
		self.rx = rx
		self.ry = ry
		self.start_angle = start_angle
		self.end_angle = end_angle
		self.phi = phi
		self.no_of_points = no_of_points
		super().__init__()

	def generate_points(self):
		points = []
		for i in range(self.no_of_points):
			theta = self.start_angle+(self.end_angle-self.start_angle)/(self.no_of_points-1)*i
			r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(theta)**2 + self.rx**2*np.sin(theta)**2))
			points.append([r*np.cos(theta+self.phi), -r*np.sin(theta+self.phi)])
		self.points = points

	# def _scale(self, xscale = 1, yscale = 1):
	# 	self.rx = self.rx*xscale
	# 	self.ry = self.ry*yscale

class Ellipse(Arc):
	'''
	This class creates an ellipse.
	'''
	def __init__(self, rx=1, ry=1, phi=0, no_of_points=10):
		super().__init__(rx, ry, 0, 2*np.pi, phi, no_of_points)

class CircularArc(Arc):
	'''
	This implements a circular arc.
	'''
	def __init__(self, r=1, start_angle=0, end_angle=360, phi=0, no_of_points=10):
		super().__init__(r, r, start_angle, end_angle, phi, no_of_points)

class Circle(CircularArc):
	'''
	This class implements a circle.
	'''
	def __init__(self, r=1, start_angle=0, end_angle=360, phi=0, no_of_points=10):
		super().__init__(r, 0, 2*np.pi, phi, no_of_points)