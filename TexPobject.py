import os
import datetime as dt
from xml.dom import minidom
import shutil
import re

from Pobject import Pobject

from constants import *

class TexPobject(Pobject):

    no_of_TexPobjects = 0

    def __init__(self, texstring, filename = 'temp', tex_dir = TEX_DIR):
        super().__init__()
        self.texstring = texstring
        TexPobject.no_of_TexPobjects += 1
        self.texPobject_number = TexPobject.no_of_TexPobjects
        self.tex_dir = '%s_%d/' % (tex_dir, TexPobject.no_of_TexPobjects)
        self.filename = '%s_%d' % (filename, TexPobject.no_of_TexPobjects)
        self.defs_string = ''
        self.create_dir()
        self.texwriter()
        self.tex_to_dvi()
        self.dvi_to_svg()
        self.parse_svg()

    ######################################################
    # THIS MIGHT BE EVIL
    ######################################################
    def __del__(self):
        self.close()

    def get_defs(self):
        self.parse_svg()
        return self.defs_string

    def get_pathstring(self, location):
        <use x='-72' xlink:href='#g0-89' y='-65.1922'/>
        return '<use x=\'%f\' y=\'%f\' xlink:href=\'TexPobject_%d\'' % (location[0], location[1], self.texPobject_number)

    def close(self):
        shutil.rmtree(self.tex_dir)

    def create_dir(self):
        os.makedirs(self.tex_dir)

    def texwriter(self, texstring = None):
        if texstring is not None:
            self.texstring = texstring
        with open(TEX_TEMPLATE, 'r') as tex_file:
            new_tex_str = tex_file.read().replace(TEXT_TO_REPLACE, self.texstring)
        with open(self.tex_dir + self.filename + '.tex', 'w+') as outfile:
            outfile.write(new_tex_str)

    def tex_to_dvi(self):
        commands = [
        "latex", 
        "-interaction=batchmode", 
        "-halt-on-error",
        "-output-directory=" + self.tex_dir,
        self.filename + '.tex',
        "> /dev/null"
        ]
        exit_code = os.system(" ".join(commands))
        if exit_code != 0:
            raise PanimException('TeX not converted to DVI.')

    def dvi_to_svg(self):
        commands = [
            "dvisvgm",
            self.tex_dir + self.filename + '.dvi',
            "-n",
            "-v",
            "0",
            "--bbox=min",
            "-o",
            self.tex_dir + self.filename + 'temp.svg',
            "> /dev/null"
        ]
        exit_code = os.system(" ".join(commands))
        if exit_code != 0:
            raise PanimException('DVI not converted to SVG.')

    def parse_svg(self):
        self.defs_string = ''
        with open(self.tex_dir + self.filename + 'temp.svg', 'r') as oldfile:
            contents = oldfile.readlines()
            [self._x, self._y, self._dx, self._dy] = [float(i) for i in contents[2].split('viewBox=')[1].split('\'')[1].split(' ')]
            contents.remove('</defs>\n')
            regex = re.compile(r"#{,1}g[0-9]*-[0-9]*")
            for line in contents[4:-2]:
                print(line)
                if '<g id=\'page1\'>\n' == line:
                    line = '<g id=\'TexPobject_%d\'>\n' % (TexPobject.no_of_TexPobjects)
                pattern = regex.findall(line)
                for word in pattern:
                    line = line.replace(word, '%s_%d' % (word, TexPobject.no_of_TexPobjects))
                self.defs_string += line
            self.defs_string += '</g transform=translate(%f %f)>' % (-self._x, -self._y)