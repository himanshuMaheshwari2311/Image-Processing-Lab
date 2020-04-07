import cv2 as cv2
import numpy as np

def main():
    img = cv2.imread('1.jpg', 0)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow("Image", img)
    cv2.imshow("Binary Threshold", thresh1)
    cv2.imshow("Truncated Threshold", thresh3)
    cv2.imshow("To Zero Threshold", thresh5)
    cv2.waitKey(0)

if __name__ == '__main__':
     main()