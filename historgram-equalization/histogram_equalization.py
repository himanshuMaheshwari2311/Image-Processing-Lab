import cv2
from matplotlib import pyplot as plt
import numpy as np

def main():
    img = cv2.imread('1.jpg', 0)
    # histogram  of image
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max() 
    plt.plot(cdf_normalized, color = 'r')
    plt.hist(img.flatten(),256,[0,256], color = 'b'), plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()
    # equalization
    cv2.imshow("Original Image", img)
    res = cv2.equalizeHist(img)
    cv2.imwrite('res.png',res)
    cv2.imshow("Result Image", res)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()