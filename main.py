import cv2
import numpy as np
class image_dither(object):
    def dither(self, img, method='floyd-steinberg', resize = False):
        if(resize):
            img = cv2.resize(img, (np.int(0.5*(np.shape(img)[1])), np.int(0.5*(np.shape(img)[0]))))
        if(method == 'simple2D'):
            img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
            rows, cols = np.shape(img)
            out = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
            for i in range(1, rows-1):
                for j in range(1, cols-1):
                    # threshold step
                    if(out[i][j] > 0.5):
                        err = out[i][j] - 1
                        out[i][j] = 1
                    else:
                        err = out[i][j]
                        out[i][j] = 0

                    # error diffusion step
                    out[i][j + 1] = out[i][j + 1] + (0.5 * err)
                    out[i + 1][j] = out[i + 1][j] + (0.5 * err)

            return(out[1:rows-1, 1:cols-1])

        elif(method == 'floyd-steinberg'):
            img = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
            rows, cols = np.shape(img)
            out = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    # threshold step
                    if (out[i][j] > 0.5):
                        err = out[i][j] - 1
                        out[i][j] = 1
                    else:
                        err = out[i][j]
                        out[i][j] = 0

                    # error diffusion step
                    out[i][j + 1] = out[i][j + 1] + ((7/16) * err)
                    out[i + 1][j - 1] = out[i + 1][j - 1] + ((3/16) * err)
                    out[i + 1][j] = out[i + 1][j] + ((5/16) * err)
                    out[i + 1][j + 1] = out[i + 1][j + 1] + ((1/16) * err)

            return (out[1:rows - 1, 1:cols - 1])

        elif (method == 'jarvis-judice-ninke'):
            img = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_REPLICATE)
            rows, cols = np.shape(img)
            out = cv2.normalize(img.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
            for i in range(2, rows - 2):
                for j in range(2, cols - 2):
                    # threshold step
                    if (out[i][j] > 0.5):
                        err = out[i][j] - 1
                        out[i][j] = 1
                    else:
                        err = out[i][j]
                        out[i][j] = 0

                    # error diffusion step
                    out[i][j + 1] = out[i][j + 1] + ((7 / 48) * err)
                    out[i][j + 2] = out[i][j + 2] + ((5 / 48) * err)

                    out[i + 1][j - 2] = out[i + 1][j - 2] + ((3 / 48) * err)
                    out[i + 1][j - 1] = out[i + 1][j - 1] + ((5 / 48) * err)
                    out[i + 1][j] = out[i + 1][j] + ((7 / 48) * err)
                    out[i + 1][j + 1] = out[i + 1][j + 1] + ((5 / 48) * err)
                    out[i + 1][j + 2] = out[i + 1][j + 2] + ((3 / 48) * err)

                    out[i + 2][j - 2] = out[i + 2][j - 2] + ((1 / 48) * err)
                    out[i + 2][j - 1] = out[i + 2][j - 1] + ((3 / 48) * err)
                    out[i + 2][j] = out[i + 2][j] + ((5 / 48) * err)
                    out[i + 2][j + 1] = out[i + 2][j + 1] + ((3 / 48) * err)
                    out[i + 2][j + 2] = out[i + 2][j + 2] + ((1 / 48) * err)

            return (out[2:rows - 2, 2:cols - 2])

        else:
            raise TypeError('specified method does not exist. available methods = "simple2D", "floyd-steinberg(default)", "jarvis-judice-ninke"')

if __name__ == '__main__':
    img = cv2.imread('images/img1.jpg', 0)
    dither_object = image_dither()
    out = dither_object.dither(img, 'jarvis-judice-ninke', resize=True)

    cv2.imshow('a', out)
    cv2.waitKey(0)