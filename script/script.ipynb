import cv2
import numpy as np
import matplotlib.pyplot as plt

#contour sorting function
def get_contour_areas(contours):
    # returns the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

#load image
#image = cv2.imread('./Downloads/test.jpg')
image = cv2.imread('./images/scan.jpg')
original_image = image.copy()
rows,cols,ch = image.shape
cv2.imshow('Original Scan', image)
cv2.waitKey()

#a grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#get canny edges
edges = cv2.Canny(gray, 30, 200)
#cv2.imshow('Edges', edges)
#cv2.waitKey()

#contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Canny Edges After Contouring', edges)
cv2.waitKey()

# Sort contours large to small
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

#print(sorted_contours[0][3][0][1])
#get corner indices
max_y = sorted_contours[0][0][0][1];
max_y_index = 0;

min_y = sorted_contours[0][0][0][1];
min_y_index = 0;

max_x = sorted_contours[0][0][0][0];
max_x_index = 0;

min_x = sorted_contours[0][0][0][0];
min_x_index = 0;

counter = 0;
while counter < sorted_contours[0].shape[0]:
    x = sorted_contours[0][counter][0][0];
    y = sorted_contours[0][counter][0][1];
    if (y > max_y):
        max_y = y
        max_y_index = counter
        
    if (y < min_y):
        min_y = y
        min_y_index = counter
        
    if (x > max_x):
        max_x = x
        max_x_index = counter
        
    if (x < min_x):
        min_x = x
        min_x_index = counter
    counter = counter + 1

#corner definition
c1 = (sorted_contours[0][max_x_index][0][0],sorted_contours[0][max_x_index][0][1])
c2 = (sorted_contours[0][min_x_index][0][0],sorted_contours[0][min_x_index][0][1])
c3 = (sorted_contours[0][max_y_index][0][0],sorted_contours[0][max_y_index][0][1])
c4 = (sorted_contours[0][min_y_index][0][0],sorted_contours[0][min_y_index][0][1])
    

        
#print countour with largest area (will most likely return paper)
cv2.drawContours(original_image, sorted_contours[0], -1, (255,0,0), 3)
cv2.circle(original_image, c1 , 8, (0, 50, 255), -1)
cv2.circle(original_image, c2, 8, (0, 255, 255), -1)
cv2.circle(original_image, c3, 8, (0, 255, 0), -1)
cv2.circle(original_image, c4, 8, (255, 255, 0), -1)
cv2.imshow('Paper Contour with Labeled Corners', original_image)
cv2.waitKey(0)


#construct new points for affine transformation
width = (((c1[0] + c4[0])**2) + ((c1[1] + c4[1])**2))**(0.5)
height = (((c1[0] + c3[0])**2) + ((c1[1] + c3[1])**2))**(0.5)
nc1 = [width,0]
nc2 = [0,height]
nc3 = [width,height]
nc4 = [0,0]

#construct arrays of transformed points

points_A = np.float32([np.asarray(c1), np.asarray(c2), np.asarray(c3), np.asarray(c4)])
points_B = np.float32([nc1, nc2, nc3, nc4])

print("A: "),
print(points_A)

print("B: "),
print(points_B)
print("")
print("reaches line 109")
#affine transformation
M = cv2.getPerspectiveTransform(points_A, points_B)
warped = cv2.warpPerspective(image, M, (int(width), int(height)))
 
cv2.imshow('warpPerspective', warped)
cv2.waitKey(0)

#print all contours for reference
cv2.drawContours(image, contours,-1, (0,255,0), 3)
cv2.imshow('All Contours', image)
cv2.waitKey()
cv2.destroyAllWindows()
