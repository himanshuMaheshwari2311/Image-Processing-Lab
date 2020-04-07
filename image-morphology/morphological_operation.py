import cv2
from matplotlib import pyplot as plt
import numpy as np

def main():
    img = cv2.imread('2.jpg', 0)
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # erosion
    kernel = np.ones((11, 11), np.uint8)
    erosion = cv2.erode(thresh, kernel, iterations=1)
    # dilation
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    # Opening
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # Closing
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    # Display Images
    plt.subplot(321), plt.imshow(img, cmap = 'gray'), plt.axis('off')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(322),plt.imshow(thresh, cmap = 'gray')
    plt.title('Binary Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(323),plt.imshow(erosion, cmap = 'gray')
    plt.title('Eroded Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(324),plt.imshow(dilation, cmap = 'gray')
    plt.title('Dilated Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(325),plt.imshow(opening, cmap = 'gray')
    plt.title('Opening Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(326),plt.imshow(closing, cmap = 'gray')
    plt.title('Closing Image'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()