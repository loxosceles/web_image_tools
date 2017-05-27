#!/usr/bin/env python

"""
web_resizer will find any jpg file in the current directory and leave a resized copy
in a seperate folder inside that directory.
ARGS: basewidth, the width of the resized image
"""

from PIL import Image
import glob, os, sys

extension = 'jpg'

def resize_img(percentage):
    for infile in glob.glob('*.' + extension):
        file_name, ext = os.path.splitext(infile)
        img = Image.open(infile)
        exif_data = img.info['exif']

        w, h = float(img.width), float(img.height)

        # rotate if necessary
        img = rotate(img)

        # calculate basewidth from percentage
        # size: The requested size in pixels, as a 2-tuple: (width, height)
        # if height bigger than width we have portrait
        if w < h:
            print("portrait")
            height = h * percentage
            width = (w / h) * height
            print(width, height)
        # if width bigger than height we have landscape
        else:
            print('landscape')
            width = w * percentage
            height = (h / w) * width 
            print(width, height)

        print("Printing image size")
        print("width: ", w)
        print("height: ", h)
            

        img = img.resize((int(width), int(height)))
        resolution = str(width).split('.')[0] + "x" + str(height).split('.')[0]
        save_dir = str(percentage).split('.')[-1] + '0%'

        if not os.path.isdir(save_dir):
           os.mkdir(save_dir) 

        img.save(save_dir + "/" + file_name + "_" + resolution + "." + extension, "JPEG", exif=exif_data)

        print_current_file(file_name)

def rotate(img):
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
                img.transpose(rotations[orientation])
    finally:
        return img 

def print_current_file(f):
        print("Resizing " + f)

def calc_height(orig_width, orig_height):
        temp = ( int(w_str) / float(orig_width) )
        return int( (float(orig_height) * temp) )

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("\nUsage: web_resizer PERCENT\n")
        print("Percent has to be given as a decimal between 0.01 and 0.99\n")
        sys.exit()

    # argument is percentage
    resize_percent = sys.argv[1]


    resize_img(float(resize_percent))
