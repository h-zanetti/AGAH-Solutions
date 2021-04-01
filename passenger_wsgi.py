import sys, os

INTERP = "/home/wwagah/hs_website/bin/python"

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from project.wsgi import application
