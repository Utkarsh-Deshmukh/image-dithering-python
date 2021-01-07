# image-dithering-python
multiple python implementations for image dithering

image dithering - wikipedia definition:
Dither is an intentionally applied form of noise used to randomize quantization error, preventing large-scale patterns such as color banding in images. Dither is routinely used in processing of both digital audio and video data.

# implementation:
 ## method 1:
  ```pip install PyDither```
  
  ```
      import cv2
      import Dither

      img = cv2.imread('images/img1.jpg', 0)						# read image

      out = Dither.dither(img, 'simple2D', resize=True)			# perform image dithering
      cv2.imshow('dithered image', out)
      cv2.waitKey(0)
  ```
  
  ## method 2:
   Run the file main.py

# Results:
![readme1](https://user-images.githubusercontent.com/13918778/103830175-f213c900-502f-11eb-9939-050d0fb973ba.png)

# Theory:
this repository implements 3 different types of error diffusion based image dithering algorithms.

![image](https://user-images.githubusercontent.com/13918778/103832335-e970c200-5032-11eb-9d5a-97f9b6be7d16.png)

# License:
This project is licensed under the BSD 2 License - see the LICENSE.md file for details

