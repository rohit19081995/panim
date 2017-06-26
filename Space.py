class Space(object):
	"""This class implements the coordinate Space on which Pobjects are placed."""
	def __init__(self):
		super(Space, self).__init__()
		self.pobjects = []
		self.pobjects_name_list = []
		self.pobjects_locations = []
		self.no_of_Pobjects = 0

	def add_Pobject(self, pobject, location):
		'''
		Adds a Pobject to the space.
		'''
		self.pobjects.append(pobject)
		pobject.name = '%s_%d' % (pobject.__class__.__name__, self.no_of_Pobjects+1)
		self.pobjects_name_list.append(pobject.name)
		self.pobjects_locations.append(location)
		self.no_of_Pobjects += 1