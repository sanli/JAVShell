#
# python script to running simple http stress test
# by 'ab'
#
import sys

if len(sys.argv) < 2:
    print '''please give URL, as
load.py http://192.168.1.110'''
    sys.exit()

url = sys.argv[1]

print "URL=%s" % (url)
# start to do test
from subprocess import check_output,CalledProcessError


for round in [20,50,100,200]:
    retry = True
    while retry:
        try:
            print ' '.join(['./ab' ,'-n', '1000',  '-c',  str(round), url])
            output = check_output(['./ab' ,'-n', '1000',  '-c',  str(round), url])
            retry = False
        except CalledProcessError :
            print "has error, retry..."

    print output
    
