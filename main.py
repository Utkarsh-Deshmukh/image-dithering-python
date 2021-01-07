import cv2
import numpy as np
import Dither


if __name__ == '__main__':
    img = cv2.imread('images/img1.jpg', 0)  # read image

    out = Dither.dither(img, 'simple2D', resize=True)  # perform image dithering
    cv2.imshow('dithered image', out)
    cv2.waitKey(0);