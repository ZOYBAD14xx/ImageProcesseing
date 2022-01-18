import cv2
import numpy as np

# Open the image.
img = cv2.imread('nature.jpg')

# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)

font                   = cv2.FONT_HERSHEY_DUPLEX
bottomLeftCornerOfText = (10,100) #position of text
fontScale              = 1 #size of text
fontColor              = (255,255,255)
thickness              = 2 #width of text

cv2.putText(img,'Original', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,)

cv2.putText(log_transformed,'log_transformed', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    (0,0,0),
    thickness,)


# Horizontally concatenate the images
img_concat = cv2.hconcat([img,log_transformed ])        #Concat image
imS = cv2.resize(img_concat, (1000, 500))               # Resize image

#Save image
cv2.imwrite('log_transformed.jpg', img_concat)

# Display the concatenated image
cv2.imshow('a2',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()



