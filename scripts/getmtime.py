# Takes a file path "/path/to/file" as input and writes the mtime to both stdou and "/path/to/file.mtime

from os.path import getmtime
import sys

if (len(sys.argv) != 2):
    print("Prints file mtime on stdout and outputs it on /path/to/file.mtime")
    print("Argument: /path/to/file")
    exit()
    
filepath = sys.argv[1]
mtime = getmtime(filepath)
mtimefilename = filepath + ".mtime"

print(mtime)
mtimefp = open(mtimefilename, "w")
mtimefp.write(str(mtime))
mtimefp.close()
