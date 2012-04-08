'''
simple build script
'''
import os
import sys

#build UI
uilist = ["about.ui" , "dialog.ui"]

#build RES
reslist = ["sharenet.qrc"]

if len(sys.argv) == 1 :
    print "python build.py [build|clean]"
    exit()


if sys.argv[1] == 'clean':
    clean = True
else:
    clean = False
    
if not clean:
    print "start build..."
else:
    print "start clean..."

    

for uifile in uilist:
    if not clean:
        cmd = "pyuic4 ui\\"+ uifile + " -o src\\ui_"+ uifile.replace(".ui",".py")
    else:
        cmd = "del src\\ui_"+ uifile.replace(".ui",".py")
        
    print(cmd)
    os.system(cmd)

for res in reslist:
    if not clean:
        cmd = "pyrcc4   res\\"+ res + " -o src\\"+ res.replace(".qrc","_rc.py")
    else:
        cmd = "del src\\"+ res.replace(".qrc","_rc.py")
        
    print(cmd)
    os.system(cmd)


