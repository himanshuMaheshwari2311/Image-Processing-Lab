import cv2
from matplotlib import pyplot as plt 
import numpy as np 

def main():
    img = cv2.imread('1.jpg')
    shar = cv2.GaussianBlur(img,(7,7),0)
    shar = cv2.addWeighted(img, 5, shar, -4, 0);
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([]), plt.axis('off')
    plt.subplot(122),plt.imshow(shar),plt.title('Sharpened')
    plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()