from common import *

class Pobject(object):
	"""This class implements all objects that can be displayed"""
	def __init__(self, hidden = False, **kwargs):
		super().__init__()
		self.hidden = hidden
		self.direct_draw = False
		self.sub_Pobjects = []
		self.sub_Pobjects_locations = []
		self.svg_attributes = kwargs

		if self.svg_attributes is not None and 'stroke_linecap' not in self.svg_attributes:
			self.svg_attributes['stroke_linecap'] = 'round'
		elif self.svg_attributes is None:
			self.svg_attributes = {'stroke_linecap':'round'}

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

	def get_pathstring(self, movestring): # Will be implemented in each directly drawable Pobject subclass.
		'''
		Returns the pathstring to draw.
		'''
		if not self.direct_draw:
			pathstring = ''
			for pobject, location in zip(self.sub_Pobjects, self.sub_Pobjects_locations):
				loc = movestring.split(' ')[1:]
				loc[0] = float(loc[0])+location[0]
				loc[1] = float(loc[1])+location[1]
				pathstring += pobject.get_pathstring('m %s %s' % (loc[0], loc[1]))
		else:
			pathstring = '<path d="'
			pathstring += '%s' % (movestring)
			pathstring += self.get_direct_pathstring()
			for attribute, value in self.svg_attributes.items():
				pathstring += ' %s="%s"' % (attribute.replace('_','-'), value)
			pathstring += '/>'
		return pathstring


	def _scale(self, xscale = 1, yscale = 1):
		'''
		Scales the Pobject by the given scale.
		'''
		if not self.direct_draw:
			self.sub_Pobjects_locations = [[x*xscale, y*yscale] for [x,y] in self.sub_Pobjects_locations]
			for pobject in self.sub_Pobjects:
				pobject._scale(xscale, yscale)
		else:
			raise PanimException('The general definition of scale only works for Pobjects that cannot be drawn directly.')

	def scale(self, scale):
		self._scale(xscale=scale, yscale = scale)

	def xscale(self, scale):
		self._scale(xscale=scale)

	def yscale(self, scale):
		self._scale(yscale=scale)
