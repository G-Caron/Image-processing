import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from scipy.signal import convolve

# Importation de l'image
image = img.imread('dog.png')
print("Type de l'image : ", type(image))
print("Taille de l'image : ", image.shape)

# Fonction effectuant un produit de convolution entre un filtre et une image RGB 
def convProduct(filtre) :        
    rgb = []
    for channel in range(3):
        c = convolve(image[:,:,channel], filtre, mode='valid')
        rgb.append(c)
    
    img2 = np.dstack((rgb[0], rgb[1], rgb[2]))   
    return img2

# Filtre Gaussien 10x10
f0 = np.full([10, 10], 1. / 100)
image0 = convProduct(f0)

# Amelioration de la nettete
f1 = np.array([ [ 0, -1, 0], 
                [-1, 5, -1], 
                [0, -1, 0] ])
image1 = convProduct(f1)            
                
# Repoussage - effet de perspective
f2 = np.array([ [-2,-1, 0], 
                [-1, 1, 1], 
                [ 0, 1, 2] ])
image2 = convProduct(f2)

# Detection des bords gauches
f3 = np.array([ [-1, 0, 1], 
                [-2, 0, 2], 
                [-1, 0, 1] ])
image3 = convProduct(f3)

# Detection des bords droits
# ~ f4 = np.array([ [ 1, 0,-1], 
                # ~ [ 2, 0,-2], 
                # ~ [ 1, 0,-1] ])
f4 = np.array([ [ 0, 1,-1, 0], 
                [ 1, 3,-3,-1], 
                [ 1, 3,-3,-1], 
                [ 0, 1,-1,0] ])
image4 = convProduct(f4)

# ~ # Affichage
fig, ax = plt.subplots(nrows=2,ncols=3)
ax[0,0].imshow(image)
ax[0,0].axis('off')
ax[0,0].set_title('Originale')

ax[0,1].imshow(image0)
ax[0,1].axis('off')
ax[0,1].set_title('Flou Gaussien')

ax[0,2].imshow(image1)
ax[0,2].axis('off')
ax[0,2].set_title('Renforcement de la nettete')

ax[1,0].imshow(image2)
ax[1,0].axis('off')
ax[1,0].set_title('Repoussage')

ax[1,1].imshow(image3)
ax[1,1].axis('off')
ax[1,1].set_title('Detection de contour gauche')

ax[1,2].imshow(image4)
ax[1,2].axis('off')
ax[1,2].set_title('Detection de contour droit')
plt.show()

#  Rotation
from scipy.ndimage import rotate
rgb = []
imgR = rotate(image[:,:,0], 30, reshape=False)
rgb.append(imgR)
imgG = rotate(image[:,:,1], 30, reshape=False)
rgb.append(imgG)
imgB = rotate(image[:,:,2], 30, reshape=False)
rgb.append(imgB)    
image0 = np.dstack((rgb[0], rgb[1], rgb[2]))

# Symetrie
rgb = []
imgR = np.fliplr(image[:,:,0])
rgb.append(imgR)
imgG = np.fliplr(image[:,:,1])
rgb.append(imgG)
imgB = np.fliplr(image[:,:,2])
rgb.append(imgB)
image1 = np.dstack((rgb[0], rgb[1], rgb[2]))


# Recadrage
lx = image.shape[0]
ly = image.shape[1]

rgb = []
imgR = image[lx // 4: - lx // 4, ly // 4: - ly // 4,0]
imgG = image[lx // 4: - lx // 4, ly // 4: - ly // 4,1]
imgB = image[lx // 4: - lx // 4, ly // 4: - ly // 4,2]
rgb.append(imgR)
rgb.append(imgG)
rgb.append(imgB)
image2 = np.dstack((rgb[0], rgb[1], rgb[2]))


# Affichage
fig, ax = plt.subplots(nrows=1,ncols=4)
ax[0].imshow(image)
ax[0].axis('off')
ax[0].set_title('Originale')

ax[1].imshow(image0)
ax[1].axis('off')
ax[1].set_title('Rotation')

ax[2].imshow(image1)
ax[2].axis('off')
ax[2].set_title('Symétrie')

ax[3].imshow(image2)
ax[3].axis('off')
ax[3].set_title('Recadrage')

plt.show()
