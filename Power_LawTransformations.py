import cv2
import numpy as np
# Load the image
img = cv2 .imread('nature.jpg')

# Perform Operations you want. Here, I did Gamma Correction of 2.2, 1 and 0.4
gamma2_2 = np.array(255*(img/255)**2.2,dtype='uint8')
gamma1 = np.array(255*(img/255)**1,dtype='uint8')
gamma0_4 = np.array(255*(img/255)**0.4,dtype='uint8')


font                   = cv2.FONT_HERSHEY_DUPLEX
bottomLeftCornerOfText = (10,100) #position of text
fontScale              = 1 #size of text
fontColor              = (255,255,255)
thickness              = 2 #width of text

cv2.putText(gamma2_2,'Gamar = 2.2', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,)

cv2.putText(gamma1,'Gamar = 1', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,)

cv2.putText(gamma0_4,'Gamar = 0.4', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    fontColor,
    thickness,)


# Horizontally concatenate the images
img_concat = cv2.hconcat([gamma2_2,gamma1,gamma0_4])    #Concat image
imS = cv2.resize(img_concat, (1000, 500))               # Resize image

#Save image
cv2.imwrite('gamma_transformed.jpg', img_concat)

# Display the concatenated image
cv2.imshow('a2',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
