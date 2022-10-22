import cv2
import math

path = 'img.png'
img = cv2.imread(path)
pointsList = []

def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 2 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/2)*2]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),2,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])


def distanceCalculate(pointsList):
    pt1, pt2 = pointsList[-2:]
    print(pt1 , pt2)
    """p1 and p2 in format (x1,y1) and (x2,y2) tuples"""
    dis = ((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2) ** 0.5
    
    
    print("Distance =", dis,'pixel')
            

    
while True:
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:
        distanceCalculate(pointsList)

        break   

    cv2.imshow('Image',img)
    
    cv2.setMouseCallback('Image',mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)

           
        
