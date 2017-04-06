#!/usr/bin/env python
"""
Web Image Renamer

Rename a every image file inside a given folder and its subfolders. The resulting
image name will be showing the folder hierarchy in which the files are living.
Example: ./folder1/subfolder 1/image.png will rename all files under 'subfolder' into
folder1__subfolder_1-image.png.

Spaces will be taken, also within folder names. The path can be given explicitly
deeper inside the folder hierarchy and only files under the specified folder will be considered.
Example: web_image_renamer folder1/subfolder\ 1 will only consider files under
'subfolder', any image files under 'folder1' will not be renamed. 
"""
from os import rename, path, walk
import sys

ABS_PATH_LIMIT = 3
directory = './' # default
ext = ['JPG', 'jpg', 'png', 'PNG', 'TIFF', 'tiff']

class FilePathNotValidException(Exception):
    def __init__(self, message, *args):
        self.message = message 

class PathObj(object):

    def __init__(self, p):
        self.full_path = p

    def check_path_validity(self, val):
        if not path.isdir(val):
            raise FilePathNotValidException("File path not valid!")
            sys.exit(1)

        if not val.startswith(('/', './')):
            #val
            pass

    @property
    def full_path(self):
        return self._full_path

    @full_path.setter
    def full_path(self, val):

        self.check_path_validity(val)
        val = val.rstrip('/')
        self._full_path = val 
        self.path_as_list = val
        self.path = self.path_as_list 
        self.ppath = self.path_as_list
        self.path_to_name_prefix = self.path_as_list 

    @property
    def path(self):
        return self._path + '/'

    @path.setter
    def path(self, l):
        """ Take a list and concatenate the path as string"""
        self._path = '/'.join(l)

    @property
    def ppath(self): 
        if not self._ppath:
            return self._ppath
        else:
            return self._ppath + '/'

    @ppath.setter
    def ppath(self, l):
        """ Take a list and concatenate the pretty path as string"""
        if self._path_as_list[0] == '..':
            self._ppath = ''.join(l[2:])
        else:
            self._ppath = '/'.join(l)

    @property
    def path_to_name_prefix(self):
        return self._path_to_name_prefix

    @path_to_name_prefix.setter
    def path_to_name_prefix(self, l):
        """ Take a list and concatenate the name prefix as string"""

        try:
            self._path_to_name_prefix =\
                '__'.join(l[1:][-ABS_PATH_LIMIT:]).replace(' ', '_') + '-'
        except IndexError as e:
            self._path_to_name_prefix =\
                '__'.join(l[1:]).replace(' ', '_') + '-'
 
    @property
    def path_as_list(self):
        return self._path_as_list

    @path_as_list.setter
    def path_as_list(self, val):
        self._path_as_list = val.split('/')
        if self._path_as_list[0] == '.':
            self._path_as_list[0] =\
                path.abspath('./').split('/')[-1]
            self._path_as_list.insert(0, '..')


def trim_redund(old_fn, new_fn):
    
    splitted_path = old_fn.split(new_fn.split('__')[-1])
    try:
        return new_fn + splitted_path[1]
    except:
        return new_fn + splitted_path[0]

if __name__ == "__main__":

    if len(sys.argv) > 2:
        print("Taking at most one argument")
        sys.exit(1)

    if len(sys.argv) == 2:
        directory = sys.argv[1]

    for root, dirs, files in walk(directory, topdown='true'):
        pobj = PathObj(root)
        print('Dirs: '),
        print(dirs)
        print(root)
        print(files)

        for fn in files:

            temp = trim_redund(fn, pobj.path_to_name_prefix)
            renamed_file = pobj.path + temp

            print(fobj.ppath + fn, fobj.ppath + temp)
            rename(fobj.path + fn, renamed_file)
