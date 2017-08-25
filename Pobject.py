from common import *

class Pobject(object):
	"""This class implements all objects that can be displayed"""
	def __init__(self, hidden=False):
		super().__init__()
		self.hidden = hidden
		self.sub_Pobjects = []
		self.sub_Pobjects_locations = []

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

	# def get_pathstring(self, movestring): # Will be implemented in each directly drawable Pobject subclass.
	# 	'''
	# 	Returns the pathstring to draw.
	# 	'''
	# 	if not self.direct_draw:
	# 		pathstring = ''
	# 		for pobject, location in zip(self.sub_Pobjects, self.sub_Pobjects_locations):
	# 			loc = movestring.split(' ')[1:]
	# 			loc[0] = float(loc[0])+location[0]
	# 			loc[1] = float(loc[1])+location[1]
	# 			pathstring += pobject.get_pathstring('M %s %s' % (loc[0], loc[1]))
	# 	else:
	# 		pathstring = '%s' % (movestring)
	# 		pathstring += self.get_direct_pathstring()
	# 	return pathstring


	def _scale(self, xscale = 1, yscale = 1):
		'''
		Scales the Pobject by the given scale.
		'''
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
