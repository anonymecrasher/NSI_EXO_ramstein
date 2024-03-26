## importation des module
import cv2
import numpy as np
## declaration des fonction
def affiche_immage(image):
    img = cv2.imread(image)
    cv2.imshow('Super image de manchot', img)
    cv2.waitKey(0)
    cv2.destroyallwindows()
    
def rotation_image(image):
    if len(image) == 1:
        return image
    else:
        
        img = np.copy(image)
        
        long = len(img)
        mi = long//2
        so1 = np.copy(img[:mi,:mi])
        so2 = np.copy(img[mi:,:mi])
        so4 = np.copy(img[:mi,mi:])
        so3 = np.copy(img[mi:,mi:])
        so1,so2,so3,so4 = so4,so1,so2,so3
        so1,so2,so3,so4 = rotation_image(so1),rotation_image(so2), rotation_image(so3), rotation_image(so4)
        img[:mi,:mi],img[mi:,:mi],img[:mi,mi:],img[mi:,mi:] = so1,so2,so4,so3
        return img
        
        
        
        
    
    
## declaration de class

## fonction principal
def main():
    img = np.copy(cv2.imread("manchot.png"))
    cv2.imshow('', rotation_image(img))
    cv2.waitKey(0)
    cv2.destroyallwindows()

## programme principal
if __name__ == '__main__':
    main()