import cv2
#cascade object for face recognition
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#recognise a face 
img = cv2.imread('photo.jpg')#you can put any picture you want here 
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray_img,
                                scaleFactor = 1.05,
                                minNeighbors = 5)
for x,y,w,h in faces:
    img_detect = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),6)
#show the face
cv2.imshow('show',img_detect)
cv2.waitKey(0)
cv2.destroyAllWindows()