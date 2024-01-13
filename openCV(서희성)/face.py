import cv2
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) 
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800) 
face_cascade = cv2.CascadeClassifier("opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

while cv2.waitKey(33) !=  ord('q'): 
    #print(cv2.waitKey(33))
    ret, frame = capture.read() 
    faces = face_cascade.detectMultiScale(frame , 1.03 , 5)

    for x,y,w,h in faces:
        print(x,y,w,h)
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (105, 74, 33), 5, cv2.LINE_8)
    
    cv2.imshow("VideoFrame", frame)

capture.release() 
cv2.destroyAllWindows()