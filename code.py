import cv2 
import numpy 
from matplotlib import pyplot as plt 

def reduce_greys_levels(matrix_image, flag): 
    matrix_image = flag * numpy.floor((matrix_image)/flag);
    print (item)
    print (matrix_image)
    return matrix_image

skull_image = cv2.imread('imagenes/skull.bmp',cv2.IMREAD_COLOR)
plt.figure()
plt.imshow(skull_image)
plt.title('Original image')
plt.axis('off')

reduce_level = [1, 2, 4, 8, 16, 32] 
n = len(reduce_level) 

for item in reduce_level: 
    modifed_image = reduce_greys_levels(skull_image, item);
    #plt.figure(figsize = 12)
    plt.figure()
    plt.imshow(modifed_image)
    plt.axis('off')
    
    print (modifed_image)
    

