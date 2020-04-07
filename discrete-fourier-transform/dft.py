import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def main():
    img =  cv.imread('1.jpg')
    img_grayscale = cv.imread('1.jpg', 0)
    dft = cv.dft(np.float32(img_grayscale),flags = cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    spectrum = 20 * np.log(cv.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    # show results
    plt.subplot(121), plt.axis('off'), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    print "Done"

if __name__ == "__main__":
    main()