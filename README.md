# Web Image Tools

## Tools for web image processing

### Web Resizer

Resize images by a given percentage.

#### Description

Takes one argument and resizes every single image file in the current folder based
on the percentage given. Percentage has to be a value between 0.01 and 0.99.

Web Resizer takes care of the aspect ratio and the orientation.

If the image provides valid EXIF data this will be used to determine if we're
dealing with a landscape or portrait format. An image is processed as landscape in
any case and will be rotated after resizing if it was taken as portrait. 

Finally the new resolution will be concatenated to the new
file name and saved within a folder which is also named after the new resolution.

#### Usage

    usage: web_resizer [-h] [-p PERCENTAGE]

###### Examples 
Resize images in current working directory by 40%

    web_resizer -p 0.4

Will ask for scaling percentage and given a valid input resizes images inside
current working directory by that percentage

    web_resizer

### Web Image Renamer
  Recursively renames every image file inside a given folder hierarchy prepending the
  containing folder name(s) to the file name. 

#### Description

  Web Image Renamer applies some intelligence to its job in a sense that it avoids
  repeated renaming, i.e. when run several times on the same directories and files.

  A relative or absolute path can be given as an argument but is not necessary. In
  case Web Image Renamer doesn't encounter one, it assumes the current directory as a
  staring point and descends every directory which it finds on that level until it
  finds one or several image files which will be renamed. Every image file on any of
  these levels will be renamed as well.

  The maximum of path prepending is 3 by default. Going further does probably not
  make very much sense since folders which are up more than 3 levels from that
  particular image file are not likely to be useful for classifying it. 
  This also prevents affecting files outside your image folders in case you happen to
  execute Web Image Renamer from let's say you root directory.

#### Usage

  The top folder can be given as an argument or the tool will asume the current
  folder.

###### Example:
  
  Given the following path:

    Photos/South America/Columbia/Bogota/123.jpg
    
  Running the tool from South America without any argument or from a random folder
  with 'Photos/South America' as argument, the result will be:

    Photos/South America/Columbia/Bogota/South_America__Colombia__Bogota__123.jpg
  
  Photos on any level of this photo hierarchy will be renamed as well.
  The idea is to prevent mixing up photos with different purposes, like e.g.
  thumbnails which live inside a folder with originals under an extra thumbnail
  folder.
  
  So, if we had a folder 'thumbnails' under the 'Bogota' folder we would get for a
  specific file:

    South_America__Colombia__Bogota__thumbnails__123.jpg
  
 
