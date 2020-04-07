import cv2 
import numpy as np
from matplotlib import pyplot as plt

def main():
    img = cv2.imread('water_coins.jpg')
    cv2.imshow("Original Image", img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # remove small noises using opening
    kernel = np.ones((3,3), np.uint8)
    img_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
    # increase object boundary as we are not sure of background
    sure_bg = cv2.dilate(img_open, kernel, iterations=3)
    # foreground detection
    dist_transform = cv2.distanceTransform(img_open, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    # boundary where bg and fg meet
    unknown = cv2.subtract(sure_bg, sure_fg)
    _, markers = cv2.connectedComponents(sure_fg)
    markers += 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(img, markers)
    img[markers == -1] = [255,0,0]
    cv2.imshow("Segmented Image", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
