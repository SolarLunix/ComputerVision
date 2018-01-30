import hog
import cv2 as cv

# Read in the test image
img = cv.imread("../Phantom.jpg")
img = cv.resize(img, (500, 500))

img2 = cv.imread("../Phantom_Melissa.jpg")
img2 = cv.resize(img2, (467, 350))

img3 = cv.imread("../Pixel_melissa.png")

hog = hog.HOG()
hog.run_hog(img)