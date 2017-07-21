#!/usr/bin/env python

""" Prepend containing folder names to files.

Renaming is done recursively from the point in the folder hirarchy wich is specified
by the path. Every level of the hirarchy shows up in the filename in order from root
to filename location.

Example: ./folder1/subfolder 1/image.png will rename all files under 'subfolder 1' into
folder1__subfolder_1-image.png.

Any blank space is replaced by a single underscore, also within folder names. As a
separator between folder levels a double underscore is used. 

The last specified folder on the path given to the programm will be the one where
under any files (up to the last level) will be renamed. Any directories which lead
to this last one will be left unchanged. 

Example: web_image_renamer folder1/subfolder\ 1 will only consider files under
'subfolder', any image files under 'folder1' will not be renamed. 

If no path is given, the current working directory will be the starting point. 

In order to prevent hazardous behaviour where a whole system could end up being
renamed the depth is limited to three levels when using an absolute path.

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
    """ Keep pathes and names in one place.

    """

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
    """
    """
    splitted_path = old_fn.split(new_fn.split('__')[-1])
    try:
        return new_fn + splitted_path[1]
    except:
        return new_fn + splitted_path[0]

if __name__ == "__main__":

    if len(sys.argv) > 2: print("Taking at most one argument") sys.exit(1)

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

            print(pobj.ppath + fn, pobj.ppath + temp)
            rename(pobj.path + fn, renamed_file)
