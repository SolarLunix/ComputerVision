import gabor
import cv2 as cv

# Read in the test image
img = cv.imread("../Phantom.jpg")
img = cv.resize(img, (500, 500))

img2 = cv.imread("../Phantom_Melissa.jpg")
img2 = cv.resize(img2, (467, 350))

img3 = cv.imread("../Pixel_melissa.png")

# Initialise the gabor class and create filters
g = gabor.Gabor(n_filters=20)
result = g.create_filters()


# Apply filters to image
g_img = g.apply_filters(img)
cv.imshow("Phantom", g_img)

g_img = g.apply_filters(img2)
cv.imshow("Phantom and Melissa", g_img)

g_img = g.apply_filters(img3)
cv.imshow("Pixel and Melissa", g_img)
cv.waitKey(0)