import cv2

def pose_func():
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) 
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800) 
    pose_cascade = cv2.CascadeClassifier("opencv-master/data/haarcascades/haarcascade_fullbody.xml")

    while cv2.waitKey(33) !=  ord('q'): 
        #print(cv2.waitKey(33))
        ret, frame = capture.read() 
        faces = pose_cascade.detectMultiScale(frame , 1.01, 2, 0, minSize=(70, 70))

        for x,y,w,h in faces:
            print(x,y,w,h)
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (105, 74, 33), 5, cv2.LINE_8)
        c = len(faces)
        frame = cv2.putText(frame, f"pose : {c}", (30, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (1,1,1), 3) 
        cv2.imshow("VideoFrame", frame)

    capture.release() 
    cv2.destroyAllWindows()

