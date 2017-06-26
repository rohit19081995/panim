import numpy as np

from Pobject import Pobject

class Arc(Pobject):
	'''
	This class implements an arc.
	'''
	def __init__(self, rx=1, ry=1, start_angle=0, end_angle=360, phi=0, **kwargs):
		'''
		This class implements an arc (the SVG path).
		'''
		super().__init__()
		self.rx = rx
		self.ry = ry
		self.start_angle = start_angle/180*np.pi
		self.end_angle = end_angle/180*np.pi
		self.phir = phi/180*np.pi
		self.phi = phi
		self.laf = True
		self.sf = False
		self.direct_draw = True
		self.kwargs = kwargs

		# SVG Path format:
		# A rx ry x-axis-rotation large-arc-flag sweep-flag x y

	def get_pathstring(self, movestring):
		r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(self.start_angle)**2 + self.rx**2*np.sin(self.start_angle)**2))
		self.start_point = [r*np.cos(self.start_angle+self.phir), -r*np.sin(self.start_angle+self.phir)]

		r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(self.end_angle)**2 + self.rx**2*np.sin(self.end_angle)**2))
		self.end_point = [r*np.cos(self.end_angle+self.phir), -r*np.sin(self.end_angle+self.phir)]
		# Moving to rx on x-axis
		pathstring = '<path d="'
		pathstring += '%s m %f %f ' % (movestring, self.start_point[0], self.start_point[1])
		pathstring += 'A %f %f %f %d %d %f %f "' % (self.rx, self.ry, -self.phi, self.laf, self.sf, self.end_point[0], self.end_point[1])
		for attribute, value in self.kwargs.items():
			pathstring += ' %s="%s"' % (attribute, value)
		pathstring += '/>'

		return pathstring

	def _scale(self, xscale = 1, yscale = 1):
		self.rx = self.rx*xscale
		self.ry = self.ry*yscale

class Ellipse(Pobject):
	'''
	This class creates an ellipse.
	'''
	def __init__(self, rx=1, ry=1, start_angle=0, end_angle=360, phi=0, **kwargs):
		super().__init__(**kwargs)
		self.direct_draw = False
		self.sub_Pobjects = [
							Arc(rx=rx, ry=ry, start_angle=start_angle, end_angle=end_angle/2, phi=phi, **kwargs),
							Arc(rx=rx, ry=ry, start_angle=end_angle/2, end_angle=end_angle, phi=phi, **kwargs)
							]
		self.sub_Pobjects_locations = [[0,0], [0,0]]