#!/usr/bin/env python

"""
web_resizer will find any jpg file in the current directory and leave a resized copy
in a seperate folder inside that directory.
ARGS: basewidth, the width of the resized image
"""

from PIL import Image
import glob, os, sys

extension = 'jpg'

def resize_img(basewidth):
    for infile in glob.glob('*.' + extension):
        file_name, ext = os.path.splitext(infile)
        img = Image.open(infile)

        hsize = calc_height(img.size[0], img.size[1])

        #if hasattr(img, '_getexif'):
        try:
            orientation = 0x0112
            exif = img._getexif()
            if exif is not None:
                orientation = exif[orientation]
                rotations = {
                    3: Image.ROTATE_180,
                    6: Image.ROTATE_270,
                    8: Image.ROTATE_90
                }
                if orientation in rotations:
                    img = img.transpose(rotations[orientation]).resize((hsize, basewidth))
                    resolution = str(hsize) + "x" + str(basewidth)
                else:
                    img = img.resize((basewidth, hsize))
                    resolution = str(basewidth) + "x" + str(hsize)
        except KeyError:
            img = img.resize((basewidth, hsize))
            resolution = str(basewidth) + "x" + str(hsize)

        save_dir = str(basewidth) + "x" + str(hsize)

        if not os.path.isdir(save_dir):
           os.mkdir(save_dir) 

        img.save(save_dir + "/" + file_name + "_" + resolution, "JPEG")

        print_current_file(file_name)

def print_current_file(f):
        print("Resizing " + f)

def calc_height(orig_width, orig_height):
        temp = ( int(w_str) / float(orig_width) )
        return int( (float(orig_height) * temp) )

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("\nUsage: web_resizer BASEWIDTH\n")
        sys.exit()

    w_str = sys.argv[1]

    resize_img(int(w_str))
