class Space(object):
	"""This class implements the coordinate Space on which Pobjects are placed."""
	def __init__(self):
		super(Space, self).__init__()
		self.pobjects = []
		self.pobjects_name_list = []
		self.pobjects_locations = []
		self.pobjects_attributes_list = []
		self.no_of_Pobjects = 0

	def add_Pobject(self, pobject, location, **kwargs):
		'''
		Adds a Pobject to the space.
		'''
		if kwargs is not None and 'stroke_linecap' not in kwargs:
			kwargs['stroke_linecap'] = 'round'
		elif kwargs is None:
			kwargs = {'stroke_linecap':'round'}

		self.pobjects.append(pobject)
		pobject.name = '%s_%d' % (pobject.__class__.__name__, self.no_of_Pobjects+1)
		self.pobjects_name_list.append(pobject.name)
		self.pobjects_locations.append(location)
		attribute_string = ''
		for attribute, value in kwargs.items():
			attribute_string += ' %s="%s"' % (attribute.replace('_','-'), value)
		self.pobjects_attributes_list.append(attribute_string)
		self.no_of_Pobjects += 1