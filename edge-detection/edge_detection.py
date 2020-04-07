import cv2
from matplotlib import pyplot as plt

def main():
    img = cv2.imread('1.jpg', 0)
    edges = cv2.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap = 'gray'), plt.axis('off')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()