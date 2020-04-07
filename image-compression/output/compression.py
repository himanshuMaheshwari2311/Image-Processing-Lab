import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    img = cv2.imread("1.jpg", 1)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),50]
    result,encimg = cv2.imencode('1.jpg', img, encode_param)
    decimg = cv2.imdecode(encimg, 1)
    plt.subplot(121), plt.imshow(img), plt.title('Original Image')
    plt.xticks([]), plt.yticks([]), plt.axis('off')
    plt.subplot(122), plt.imshow(decimg), plt.title('Compressed Image')
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.imwrite('compress1.jpg',decimg)

if __name__ == '__main__':
    main()