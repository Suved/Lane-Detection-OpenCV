import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('/home/suved/Desktop/ip.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imwrite('/home/suved/Desktop/t2.png',dst)
dst2=cv2.Canny(dst,100,200)
dst2[0:344]=0
#dst2[0:344]=0
cv2.imwrite('/home/suved/Desktop/t2.png',dst2)

#e=cv2.threshold(dst2,157,300,cv2.THRESH_BINARY)
img2=img.copy()
Lines = cv2.HoughLinesP(dst2, rho=2, theta=np.pi/180,threshold=-20,minLineLength = 4, maxLineGap = 2)
if(Lines!=None):
   for line in Lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
#cv2.line(img,(0,0),(25,25),(255,0,0),3)
cv2.imwrite('/home/suved/Desktop/t2.png',img)
