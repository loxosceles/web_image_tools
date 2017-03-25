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

class UrlNotValidException(Exception):
    def __init__(self, message, *args):
        self.message = message 

class FileObj():

    def __init__(self, p):
        self.full_path = p

    @property
    def full_path(self):
        return self._full_path

    @full_path.setter
    def full_path(self, val):

        if not val.startswith(('/', './')):
            raise UrlNotValidException("URL not valid!")
            sys.exit(1)

        self._full_path = val 
        fp = path.split(val)
        self.path_as_list = fp[0]

        self.path = self.path_as_list 
        
        self.fn = fp[1]
        self.parent_dir_name = fp[0]
        self.path_to_name_prefix = self.path_as_list 

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, l):
        """ Take a list and concatenate the path as string"""
        self._path = '/'.join(l)

    @property
    def path_to_name_prefix(self):
        return self._path_to_name_prefix

    @path_to_name_prefix.setter
    def path_to_name_prefix(self, l):
        """ Take a list and concatenate the name prefix as string"""

        # Prepend path with parent directory name if relative path
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
                path.abspath('./').replace(' ', '_').split('/')[-1]
            self._path_as_list.insert(0, '..')


root_dir = './' # default
ext = ['JPG', 'jpg', 'png', 'PNG', 'TIFF', 'tiff']

def rename_files(directory=root_dir):
    """
    Walk through a directory and renames every file prepending 
    folder hierarchy.
    """
    for root, dirs, files in walk(directory, topdown='true'):
        files = filter_ext(ext, files, root)
        #root = normalize_path(root)

        for file in files:

            #renamed_file = trim_redund(file, new_path_name)
            # renamed_file = fobj.path + '/' + 

            #rename(file, renamed_file)
            print((file, renamed_file))


def filter_ext(ext_list, file_list, parentdir):
    """ 
    Add relative path to files and filter for allwed 
    extentions.
    """
    for filename in file_list:
        filename = path.join(parentdir, filename) 
        if filename.endswith(tuple(ext_list)):
            yield filename

def trim_redund(t1, t2):
    t2 = t2.replace('/', '').replace('__-', '').replace('.', '').replace(' ', '_')
    t1 = t1.replace(' ', '_')
    print(t1)
    print(t2)
    splitted_path = t1.split(t2.replace('__', ''))
    try:
        return './' + t2 + splitted_path[1]
    except:
        return t1

if __name__ == "__main__":

    #import pdb; pdb.set_trace()


    if len(sys.argv) > 2:
        print("Taking at most one argument")
        sys.exit(1)
    elif len(sys.argv) == 2:
        fobj = FileObj(sys.argv[1])
    else:
        fobj = FileObj('./')

    rename_files(fobj.full_path)

