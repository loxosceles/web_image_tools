#!/usr/bin/env python

"""
web_resizer will find any jpg file in the current directory and leave a resized copy
in a seperate folder inside that directory.
ARGS: basewidth, the width of the resized image
"""

from PIL import Image
import glob, os, sys
import math
import argparse

extension = ['jpg','JPG', 'JPEG', 'jpeg', 'png', 'PNG']

def resize_img(percentage):

    image_files = []

    for imgfile in map(lambda x: '*.' + x, extension):
        image_files.extend(glob.glob(imgfile))

    for infile in image_files:
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
            height = h * math.sqrt(percentage)
            width = (w / h) * height
            print(width, height)
        # if width bigger than height we have landscape
        else:
            print('landscape')
            width = w * math.sqrt(percentage)
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

        img.save(save_dir + "/" + file_name + "_" + resolution + "." + ext, "JPEG", exif=exif_data)

        print_current_file(file_name)

def rotate(img):
    print("Rotating")
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

def check_value_validity(v, lower, upper):
    if v >= lower and v <= upper:
        return True
    return False  

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Scale image inside folder by percentage')

    # Add command line arguments, only the path is obligatory
    parser.add_argument('-p', '--percentage', help=
            'Percentage by which the images will be scaled')

    args = vars(parser.parse_args())

    # If keyword is not given as argument ask for it
    if args['percentage']:
        percent = float(args['percentage'])
    else:
        percent = float(input("Percentage of scaling: "))

    # Make sure percent is between 0.01 and 0.99

    if not check_value_validity(percent, 0.01, 0.99):
        print("\nPercent has to be given as a decimal between 0.01 and 0.99\n")
        sys.exit(0)

    resize_img(percent)
