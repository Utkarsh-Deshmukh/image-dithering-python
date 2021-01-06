import cv2
import numpy as np
from openDither import image_dither
if __name__ == '__main__':
    img = cv2.imread('images/img1.jpg', 0)
    dither_object = image_dither()
    out = dither_object.dither(img, 'jarvis-judice-ninke', resize=True)

    cv2.imshow('a', out)
    cv2.waitKey(0)