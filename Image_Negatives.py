import cv2
# Load the image
img = cv2 .imread('nature.jpg')

imgNegative = 255 - img

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

cv2.putText(imgNegative,'ImageNegatives', 
    bottomLeftCornerOfText, 
    font, 
    fontScale,
    (0,0,0),
    thickness,)


# Horizontally concatenate the images
img_concat = cv2.hconcat([img,imgNegative ])            #Concat image
imS = cv2.resize(img_concat, (1000, 500))               # Resize image

#Save image
cv2.imwrite('Image_Negatives.jpg', img_concat)

# Display the concatenated image
cv2.imshow('a2',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
