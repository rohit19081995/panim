import types

from Pobject import Pobject
from Space import Space

class SVGobject(Pobject):
	'''
	This class implements SVG Paths and stores coordinates in the space.
	'''
	def __init__(self, space, center = [0,0], size = [10,10], svg_string = None, svg_file = None):
		super(SVGobject, self).__init__(space, center, size)
		if type(svg_string) is types.StringType:
			self.svg_string = svg_string
		elif type(svg_file) is types.FileType:
			self.svg_file = svg_file
		elif type(svg_file) is types.StringType and svg_file[:-3] == '.svg':
			with open(svg_file, 'r') as myfile:
				self.svg_string = myfile.read()