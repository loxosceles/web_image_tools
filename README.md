# Web Image Tools
## Tools for web image processing

### Web Resizer
  Takes one argument and resizes every single image file in the current folder. The
  argument will always define the longer side of the picture, width or height,
  depending on the orientation.

  Aspect ratio will be calculated automatically and independently for every
  single image independently. 
  
  If the image provieds valid EXIF data this will be used
  to determine if we're dealing with a landscape or portrait format. An image is
  processed as landscape in any case and will be rotated after resizing if it was
  taken as portrait. 
  
  Finally the new resolution will be concatenated to the new
  filename and saved within a folder which is also named after the new resolution.

  #### Usage
  web_resizer WIDTH
  
  #### Example

    web_resizer 1000

  Will result in a 1000x750 resolution for landscape and 750x1000 for portrait. The
  folder containing these new images will be named 1000x750.

### Web Image Renamer
  Renames every image file inside a given folder hierarchy prepending that folders
  name to the filename. For every subfolder the parent folders will be part of the
  new file name, representing the path to that file.
  The top folder can be given as an argument or the tool will asume the current
  folder.

  Example:
  
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

  #### Usage
  
 
