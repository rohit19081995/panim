import numpy as np

from Pobject import Pobject

class Line(Pobject):
	'''
	This class implements a line.
	'''
	def __init__(self, x1, y1, x2, y2, **kwargs):
		super().__init__()
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.direct_draw = True

		# SVG Path format:
		# l x y

	def get_direct_pathstring(self):
		pathstring = 'm %f %f l %f %f ' % (self.x1, self.y1, self.x2, self.y2)
		return pathstring

	def _scale(self, xscale=1, yscale=1):
		self.x1 = self.x1*xscale
		self.x2 = self.x2*xscale
		self.y2 = self.y2*yscale
		self.y1 = self.y1*yscale

class Arc(Pobject):
	'''
	This class implements an arc.
	'''
	def __init__(self, rx=1, ry=1, start_angle=0, end_angle=360, phi=0, **kwargs):
		super().__init__(**kwargs)
		self.rx = rx
		self.ry = ry
		self.start_angle = start_angle
		self.end_angle = end_angle
		self.phi = phi
		self.direct_draw = True

		r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(self.start_angle)**2 + self.rx**2*np.sin(self.start_angle)**2))
		self.start_point = [r*np.cos(self.start_angle+self.phi), -r*np.sin(self.start_angle+self.phi)]

		r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(self.end_angle)**2 + self.rx**2*np.sin(self.end_angle)**2))
		self.end_point = [r*np.cos(self.end_angle+self.phi), -r*np.sin(self.end_angle+self.phi)]

		# SVG Path format:
		# l rx ry x-axis-rotation large-arc-flag sweep-flag x y

	def get_direct_pathstring(self):
		r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(self.start_angle)**2 + self.rx**2*np.sin(self.start_angle)**2))
		self.start_point = [r*np.cos(self.start_angle+self.phi), -r*np.sin(self.start_angle+self.phi)]

		r = self.rx*self.ry/(np.sqrt(self.ry**2*np.cos(self.end_angle)**2 + self.rx**2*np.sin(self.end_angle)**2))
		self.end_point = [r*np.cos(self.end_angle+self.phi), -r*np.sin(self.end_angle+self.phi)]

		if np.abs((self.end_angle-self.start_angle)) > np.pi:
			laf = True
		else:
			laf = False
		# Moving to rx on x-axis
		# pathstring = '<path d="'
		pathstring = 'm %f %f ' % (self.start_point[0], self.start_point[1])
		pathstring += 'a %f %f %f %d %d %f %f ' % (self.rx, self.ry, -self.phi*180/np.pi, laf, False, self.end_point[0]-self.start_point[0], self.end_point[1]-self.start_point[1])
		# for attribute, value in self.svg_attributes.items():
		# 	pathstring += ' %s="%s"' % (attribute.replace('_','-'), value)
		# pathstring += '/>'

		return pathstring

	def _scale(self, xscale = 1, yscale = 1):
		self.rx = self.rx*xscale
		self.ry = self.ry*yscale

class Ellipse(Pobject):
	'''
	This class creates an ellipse.
	'''
	def __init__(self, rx=1, ry=1, start_angle=0, end_angle=2*np.pi, phi=0, **kwargs):
		super().__init__(**kwargs)
		self.sub_Pobjects = [
							Arc(rx=rx, ry=ry, start_angle=start_angle, end_angle=(end_angle-start_angle)*2/3, phi=phi, **kwargs),
							Arc(rx=rx, ry=ry, start_angle=(end_angle-start_angle)/3, end_angle=end_angle, phi=phi, **kwargs)
							]
		self.sub_Pobjects_locations = [[0,0], [0,0]]
		self.start_angle = start_angle
		self.end_angle = end_angle
		self.phi = phi
		self.direct_draw = False
		

	def set_start_angle(self, start_angle):
		start_angle = start_angle % (2*np.pi)
		self.start_angle=start_angle
		self.sub_Pobjects[0].start_angle=start_angle
		self.sub_Pobjects[0].end_angle=(self.end_angle-start_angle)*2/3
		self.sub_Pobjects[1].start_angle=(self.end_angle-start_angle)/3

	def set_end_angle(self, end_angle):
		if end_angle > 2*np.pi:
			end_angle = end_angle % (2*np.pi)
		self.end_angle=end_angle
		self.sub_Pobjects[0].end_angle=(end_angle-self.start_angle)*2/3
		self.sub_Pobjects[1].start_angle=(end_angle-self.start_angle)/3
		self.sub_Pobjects[1].end_angle=end_angle

	def set_phi(self, phi):
		self.phi=phi
		self.sub_Pobjects[0].phi=phi
		self.sub_Pobjects[1].phi=phi

	def set_rx(self, rx):
		self.rx=rx
		self.sub_Pobjects[0].rx=rx
		self.sub_Pobjects[0].rx=rx

	def set_ry(self, ry):
		self.rx=ry
		self.sub_Pobjects[0].ry=ry
		self.sub_Pobjects[0].ry=ry