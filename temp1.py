import sys
import os

i = 1
with open("rgb.txt", "w") as a:
    for path, subdirs, files in os.walk(r'./rgb'):
	files.sort()  
        for filename in files:
            f = os.path.join(path, filename)
	    if i % 5 == 1:
                # f = os.path.join(path, filename)
                a.write(str(filename)[:-4] + " " + str(f)[2:] + os.linesep)
	    else:
	        os.remove(f) 
            i = i + 1
