import numpy as np

from Pobject import Pobject
from BezierPobject import Curve

from constants import *

class Line(Curve):
	'''
	This class implements a line.
	'''
	def __init__(self, x1, y1, dx, dy, **kwargs):
		super().__init__(mode='jagged')
		self.start = [x1, y1]
		self.end = [dx,dy]

	def generate_points(self):
		self.points = [self.start, self.end]

class Rectangle(Curve):
	'''
	This class implements a rectangle.
	'''
	def __init__(self, x, y, dx, dy, **kwargs):
		super().__init__(mode='jagged')
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.generate_points()

	def generate_points(self):
		self.points = [[self.x,self.y], [self.dx, 0], [0, self.dy], [-self.dx, 0], [0, -self.dy]]

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

class Function(Curve):

	def __init__(self, func, no_of_points=20, xscale=1, yscale=1, origin=[0,0]):
		super().__init__()
		self.func = func
		self.no_of_points = no_of_points
		self.generate_points()

	def generate_points(self):
		x = np.linspace(-X_EXTENT/4, X_EXTENT/4, self.no_of_points)
		y = self.func(x)
		print(y[1])
		self.points = [[x,y] for x,y in zip(x,y)]