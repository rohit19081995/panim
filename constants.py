from pconstants import * # The pconstants file is ignored by git.

DEFAULT_VIDEO_RESOLUTION = [800,600]
CLOSED_THRESHOLD = 0.01
Y_EXTENT = 6
X_EXTENT = (DEFAULT_VIDEO_RESOLUTION[0]/DEFAULT_VIDEO_RESOLUTION[1])*Y_EXTENT

TEX_TEMPLATE = r'template.tex'
TEXT_TO_REPLACE = r'YourTextHere'

FFMPEG_BIN = r'ffmpeg'

UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1