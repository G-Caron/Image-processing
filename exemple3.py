import cv2  
import numpy as np  
    
# Reading an image in default mode 
doc = cv2.imread(r'doc.png') 
dog = cv2.imread(r'dog.png') 
dogGray = cv2.imread(r'dog.png',cv2.IMREAD_GRAYSCALE)
print(dogGray.shape)
print(dogGray[0,0])
  
# COIN HAUT GAUCHE DU PATCH
cornerTL = [30,100]

# COIN BAS DROITE DU PATCH
cornerBR = [150,350]


def insertPatch( image, cornerTL, cornerBR, color=[0,0,255]):
    
    if len(image.shape) == 2:
        image2 = np.repeat(image[:, :, np.newaxis], 3, axis=2)
        print(image2.shape)  
    else:
        image2 = image.copy()
    
    # Trait en haut
    image2[cornerTL[0], cornerTL[1]:cornerBR[1]+1] = color

    # Trait à droite
    image2[cornerTL[0]:cornerBR[0]+1, cornerBR[1]] = color

    # Trait en bas 
    image2[cornerBR[0], cornerTL[1]:cornerBR[1]+1] = color

    # Trait à gauche
    image2[cornerTL[0]:cornerBR[0]+1, cornerTL[1]] = color
    
    return image2

def showImage(image, nomImage = ""):
    # ~ # Window name in which image is displayed 
    window_name = nomImage
      
    # Using cv2.imshow() method  
    # Displaying the image  
    cv2.imshow(window_name, image) 
      
    #waits for user to press any key  
    #(this is necessary to avoid Python kernel form crashing) 
    cv2.waitKey(0)  
      
    #closing all open windows  
    cv2.destroyAllWindows()  


doc2 = insertPatch(doc, cornerTL, cornerBR,[240,120,120])
showImage(doc2)
dog2 = insertPatch(dog, cornerTL, cornerBR)
showImage(dog2)
dog2Gray = insertPatch(dogGray, cornerTL, cornerBR)
showImage(dog2Gray)
