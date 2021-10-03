import cv2
#creating an video object - starting thr video from your computer camera
video = cv2.VideoCapture(0)
i = 1
#capturing frames and displaying them
while True:
    i += 1
    check,frame = video.read()
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
#numbers of frames
print(i)    
cv2.destroyAllWindows()
video.release()