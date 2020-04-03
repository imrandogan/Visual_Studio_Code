import numpy as np
import cv2 
#img= cv2.imread("top.jpg",1)#renkli okuma
img=cv2.imread("C:/Users/DELL/Documents/Visual Studio Code/Visual_Studio_Code/Visual Studio Code/lesson2/top.jpg",0) #gri okuma
cv2.imshow('image',img)# ekrana getirme
k= cv2.waitKey(0) &0XFF
while True:
    if k==27:# çıkış için escye basılmasını bekle
        cv2.destroyAllWindows()
    elif k==ord('s'): #s ye basıldığında kaydet çık
        cv2.imwrite('C:/Users/DELL/Documents/Visual Studio Code/Visual_Studio_Code/Visual Studio Code/lesson2/messigray.png',img)
        cv2.destroyAllWindows()
        