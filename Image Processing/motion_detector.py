import cv2,datetime,pandas
    
#creating an video object - starting thr video from your computer camera
video = cv2.VideoCapture(0)
i = 1
first_frame = None
status_list = [0]
times = []
df = pandas.DataFrame(columns = ['Start','End','Frames']) 
#capturing frames and displaying them
while True:
    i += 1
    status = 0
    check,frame = video.read()
    #convorting the frames to gray for better accuracy
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    #capturing firs frame to create a dalta frame
    if first_frame is None:
        first_frame = gray
        continue
    #creating a dalta and thresh for the motion detector
    dalta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(dalta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame,None,iterations = 2)
    #finding contours of moving objects
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #capturing the moving objects that are big enough
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
            
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
    status_list.append(status)
    if status_list[-1] != status_list[-2]:
        times.append(datetime.datetime.now())
    #showing the color frames with a rectangle on moving object   
    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.datetime.now())
        break
#creating a cvs file of the data we collected - when moving object detected and when they are not + number of frames
df = df.append({'Frames':i},ignore_index = True)   
for i in range(0,len(times),2):
    df = df.append({'Start':times[i],'End':times[i+1]},ignore_index = True)
    
df.to_csv('Times.csv')

cv2.destroyAllWindows()
video.release()