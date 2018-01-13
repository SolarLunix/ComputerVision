import gabor
import cv2 as cv

g = gabor.Gabor(ori=1, ksize=100)
result = g.create_filters()

print len(result)

for filt in result:
    cv.imshow("filter", filt)
    cv.waitKey(0)