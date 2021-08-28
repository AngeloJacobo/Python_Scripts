# About:
<p align="justify">
  &emsp;&emsp;The script "move_image.py" will look for all images(any image extensions) on the path "abs_path" then move those images in ./images/"month(Week_number)" [e.g. Aug(Week_2)].
This script will stricly run only at the first start-up of the computer at that day. The timestamp will be updated so any next restarts of the computer at that sameday will force the script to not run.  The motivation here is that only the images from the previous days will be moved meanwhile the new images today will not be touched until the next-day ensuring only the latest images are left at the directory.


&emsp;&emsp;This python script uses datetime module to get the current date for updating  the "timestamp.txt", mimetypes module to list all possible image extensions, glob module to list all image files, and os module to move files accordingly.
</p>

# Configure:  
abs_path = path where the images will be found
