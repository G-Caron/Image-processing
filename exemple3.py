import cv2  
import numpy as np  
    
# Reading an image in default mode 
doc = cv2.imread(r'doc.png') 
dog = cv2.imread(r'dog.png') 
dogGray = cv2.imread(r'dog.png',cv2.IMREAD_GRAYSCALE)
# ~ print(dogGray.shape)
# ~ print(dogGray[0,0])
  

def defineGrid(image, nbPatchH=None, nbPatchW=None, height=None, width=None):
    
    if ( (nbPatchH and not nbPatchW) or (not nbPatchH and nbPatchW) or
        (height and not width) or (not height and width) or
        ((nbPatchH or nbPatchW) and (height or width)) or 
        not( nbPatchH or nbPatchW or height or width ) ):
        raise ValueError("On attend (nbPatchH and nbPatchW) xor (h  and W)")

    if (nbPatchH) :
        height = image.shape[0]//nbPatchH
        width = image.shape[1]//nbPatchW
    else : 
        nbPatchH = image.shape[0]//height
        nbPatchW = image.shape[1]//width
    print(height)
    print(width)
    print(nbPatchH)
    print(nbPatchW)
    
    # Initialisation grid
    grid = []
    for i in range(nbPatchH):
        grid.append([])
        for j in range(nbPatchW):
            grid[i].append({})

    # Calcul des bornes du patch
    for i in range(nbPatchH):
        for j in range(nbPatchW):
            grid[i][j]["top"] = i * height
            grid[i][j]["left"] = j * width
            grid[i][j]["bottom"] = (i+1) * height - 1
            grid[i][j]["right"] = (j+1) * width - 1

    return grid


# attention image est modifiée!!!
def insertPatch( image, top, bottom, left, right, color=[0,0,255]):
    
    if len(image.shape) == 2:
        image = np.repeat(image[:, :, np.newaxis], 3, axis=2)
        print(image.shape)  

    
    # Trait en haut
    image[top, left:right+1] = color

    # Trait à droite
    image[top:bottom+1, right] = color

    # Trait en bas 
    image[bottom, left:right+1] = color

    # Trait à gauche
    image[top:bottom+1, left] = color
    
    return image


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


def showGrid(image, grid):
    
    image2 = image.copy()
    nph = len(grid)
    npw = len(grid[0])
    
    for i in range(nph):
        for j in range(npw):
            insertPatch( image2, grid[i][j]["top"],grid[i][j]["bottom"],grid[i][j]["left"],grid[i][j]["right"])

    showImage(image2)




##################### APPLICATION 1 ###########################
########## TEST DE LA FONCTION insertPATCH

# Dimension du patch
# ~ t = 30
# ~ l = 100
# ~ b = 150
# ~ r = 350

# ~ doc2 = insertPatch(doc, t,b,l,r,[240,120,120])
# ~ showImage(doc2)
# ~ dog2 = insertPatch(dog, t,b,l,r)
# ~ showImage(dog2)
# ~ dog2Gray = insertPatch(dogGray, t,b,l,r)
# ~ showImage(dog2Gray)




##################### APPLICATION 2 ###########################
########## TEST DE LA FONCTION defineGrid

# ~ nph, npw = 3, 5
# ~ grid = defineGrid(doc, nbPatchH = nph, nbPatchW = npw)

# ~ for i in range(nph):
    # ~ for j in range(npw):
        # ~ nom = "grid(" + str(i) + "," + str(j) + ") - top left corner : [" + str(grid[i][j]["top"]) + ", " + str(grid[i][j]["left"]) + "] - bottom right corner : [" + str(grid[i][j]["bottom"]) + ", " + str(grid[i][j]["right"]) + "]"
        # ~ print(nom)
        # ~ showImage( doc[grid[i][j]["top"] : grid[i][j]["bottom"]+1, grid[i][j]["left"]:grid[i][j]["right"]+1 ], nom)


##################### APPLICATION 3 ###########################
########## TEST DE LA FONCTION showGrid
nph, npw = 8, 9
h, w = 180, 220
# ~ grid = defineGrid(doc, nbPatchH = nph, nbPatchW = npw)
grid = defineGrid(doc, height = h, width = w)


showGrid(doc,grid)
