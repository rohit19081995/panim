import os
from xml.dom import minidom

from Pobject import Pobject

from constants import *

class TexPobject(Pobject):

    def __init__(self, texstring, filename = 'temp'):
        super().__init__()
        self.texstring = texstring
        self.filename = filename
        self.texwriter()
        self.tex_to_dvi()
        self.dvi_to_svg()

    def texwriter(self, texstring = None):
        if texstring is not None:
            self.texstring = texstring
        with open(TEX_TEMPLATE, 'r') as tex_file:
            new_tex_str = tex_file.read()#.replace(TEXT_TO_REPLACE,texstring)
        with open(TEX_DIR + self.filename + '.tex', 'w+') as outfile:
            outfile.write(new_tex_str)

    def tex_to_dvi(self):
        commands = [
        "latex", 
        "-interaction=batchmode", 
        "-halt-on-error",
        "-output-directory=" + TEX_DIR,
        self.filename + '.tex',
        "> /dev/null"
        ]
        exit_code = os.system(" ".join(commands))
        if exit_code != 0:
            raise PanimException('TeX not converted to DVI.')

    def dvi_to_svg(self):
        commands = [
            "dvisvgm",
            TEX_DIR + self.filename + '.dvi',
            "-n",
            "-v",
            "0",
            "--bbox=min",
            "-o",
            TEX_DIR + self.filename + 'temp.svg',
            "> /dev/null"
        ]
        exit_code = os.system(" ".join(commands))
        if exit_code != 0:
            raise PanimException('DVI not converted to SVG.')
        self.move_defs_to_bottom()

    def move_defs_to_bottom(self):
        with open(TEX_DIR + self.filename + 'temp.svg', 'r') as oldfile, open(TEX_DIR + self.filename + '.svg', 'w+') as newfile:
            contents = oldfile.readlines()
            print(contents)
            contents.remove('</defs>\n')
            contents.insert(-1, '</defs>\n')
            for line in contents:
                newfile.write(line)