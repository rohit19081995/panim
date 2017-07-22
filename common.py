from constants import *

class PanimException(Exception):
	'''
	An exception class for Panim.
	'''
	pass

def is_closed(points):
    return np.linalg.norm(points[0] - points[-1]) < CLOSED_THRESHOLD