import datetime as dt
import subprocess as sp

from constants import *

class Camera(object):
	"""This class takes pictures and videos in a View."""
	def __init__(self, view, camera_dir = DEFAULT_VIDEO_DIRECTORY):
		super(Camera, self).__init__()
		self.view = view
		self.camera_dir = camera_dir
		self.pipe = None

	def save_frame(self, filename):
		with open('%s%s_%s.png' % (self.camera_dir, filename, dt.datetime.now().strftime('%Y%m%d%H%M%S')), 'wb') as file:
			pngstring,_ = self.view.capture_frame()
			file.write(pngstring)

	def start_recording(self, filename, resolution=DEFAULT_VIDEO_RESOLUTION):
		if self.pipe is not None:
			raise PanimException('You cannot record 2 videos at the same time with the same camera.')
		else:
			command = [
	            FFMPEG_BIN,
	            '-y',                # overwrite output file if it exists
	            '-f', 'image2pipe',
	            '-codec', 'png',
	            '-s', '800x600',
	            '-i', '-',      # The input comes from a pipe
	            '-an',          # Tells FFMPEG not to expect any audio
	            '%s%s_%s.mp4' % (self.camera_dir, filename, dt.datetime.now().strftime('%Y%m%d%H%M%S')),
	        ]
			self.pipe = sp.Popen( command, stdin=sp.PIPE, stderr=sp.PIPE)

	def capture_frame(self):
		if self.pipe is None:
			raise PanimException('Start recording before capturing frames.')
		pngstring,_ = self.view.capture_frame()
		self.pipe.stdin.write(pngstring)

	def stop_recording(self):
		if self.pipe is None:
			raise PanimException('Start recording before you stop recording.')
		self.pipe.stdin.close()