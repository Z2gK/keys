import sys

# Mapping for keyvalue to actual key
codedict = {2:"1",3:"2",4:"3",5:"4",6:"5",7:"6",8:"7",9:"8",10:"9",11:"0"}

if (len(sys.argv) != 2):
    print("Argument: filename of keypress file")
    exit()

fp = open(sys.argv[1])
keyup = True
for line in fp:
    a = line.strip().split(",")

    if ((a[0] == "1") and (a[2] == "1")):
        # key down event
        keyup = False
        pressedval = a[1]
        pressed = codedict[int(pressedval)]
        starttime = float(a[3])
    if ((a[0] == "1") and (a[2] == "0") and (a[1] == pressedval) and (keyup == False)):
        # key up event
        duration = float(a[3]) - starttime
        print("key: {}; duration: {}".format(pressed, duration))
        keyup = True
        
        
fp.close()
