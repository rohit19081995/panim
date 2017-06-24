import numpy as np

from Pobject import Pobject

class Arc(Pobject):
	'''
	This class implements an arc.
	'''
	def __init__(self, center=[0,0], rx=1, ry=1, start_angle=0, end_angle=360, phi=0, laf=False, sf=False):
		'''
		This class implements an arc (the SVG path).
		'''
		# SVG Path format:
		# A rx ry x-axis-rotation large-arc-flag sweep-flag x y
		
		start_angle = start_angle/180*np.pi
		end_angle = end_angle/180*np.pi
		phi = phi/180*np.pi

		r = rx*ry/(np.sqrt(ry**2*np.cos(start_angle)**2 + rx**2*np.sin(start_angle)**2))
		self.start_point = [r*np.cos(start_angle+phi)+center[0], -r*np.sin(start_angle+phi)+center[1]]

		r = rx*ry/(np.sqrt(ry**2*np.cos(end_angle)**2 + rx**2*np.sin(end_angle)**2))
		self.end_point = [r*np.cos(end_angle+phi)+center[0], -r*np.sin(end_angle+phi)+center[1]]
		# Moving to rx on x-axis
		self.pathstring = 'M %f %f' % (self.start_point[0], self.start_point[1])
		self.pathstring += 'A %f %f %f %d %d %f %f' % (rx, ry, phi, laf, sf, self.end_point[0], self.end_point[1])

class Ellipse(Pobject):
	'''
	This class creates an ellipse.
	'''
	def __init__(self, center=[0,0], size=[10,10]):
		self.center = center
		self.size = size
		self.direct_draw = True

	def crop(self, view):
		pass
		
	def draw(self, view):
		pass