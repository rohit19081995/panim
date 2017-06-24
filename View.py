from Space import Space
from constants import *

class View(object):
	"""
	This class draws the Pobjects in the view.
	"""
	def __init__(self, resolution = DEFAULT_VIDEO_RESOLUTION, space, center = [0,0]):
		super(View, self).__init__()
		self.resolution = resolution
		self.space = space
		self.center = center
		self.xstart = center[0]-resolution[0]/2
		self.xend = center[0]+resolution[0]/2
		self.ystart = center[1]-resolution[1]/2
		self.yend = center[1]+resolution[1]/2

	# TODO: implement move method