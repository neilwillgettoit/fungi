import time
import os
import shutil

def hypha_dir():
    now = int(time.time())
    dirfmt = "/var/www/html/%04d"
    dirname = dirfmt % now

    print 'Current working Directory: ' + dirname

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    shutil.copy2('/var/www/html/index.html',dirname+'/index.html')

    with open(dirname+'/index.html', "a") as somefile:
        somefile.write(str(now) + "\n" + str(now) +  "\n" + str(now) + "\n" + str(now) + "\n")

    print "Spore to burst: http://[YOUR IP OR DOMAIN HERE]/" + str(now) + "/index.html"

hypha_dir()
