from scipy import misc
import numpy as np

if __name__ == '__main__':
  image = misc.imread('snapshot02_rect.png')
  
  gray = image[:, :, 0] + image[:, :, 1] + image[:, :, 2]
  indices = np.where(gray < 75)
  print(indices)
  image[indices[0], indices[1], 0] = 0
  image[indices[0], indices[1], 1] = 83
  image[indices[0], indices[1], 2] = 159
  
  misc.imsave('snapshot02_rect_color.png', image)
