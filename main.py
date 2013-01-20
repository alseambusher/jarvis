#!/usr/bin/python
import cv
import sys
cv.NamedWindow('jarvis',cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage(sys.argv[1],cv.CV_LOAD_IMAGE_COLOR)
cv.ShowImage('jarvis',image)
cv.WaitKey(10000)
cv.SaveImage('jarvis',image)
