import cv2
#creating an video object - starting thr video from your computer camera
video = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i = 1
#capturing frames and displaying them
while True:
    i += 1
    check,frame = video.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_img,
                                    scaleFactor = 1.1,
                                    minNeighbors = 5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),6)
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
#numbers of frames
print(f'{i} frames')    
cv2.destroyAllWindows()
video.release()