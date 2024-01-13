import cv2 # cv2 가져오기

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 높이

while cv2.waitKey(33) !=  ord('q'): # 33ms 마다 반복문 실행
    #print(cv2.waitKey(33))
    ret, frame = capture.read() # ret : 영상을 잘 가져 오면 참 , frame : 영상 정보
    # 영상이 나올때 x : 200 , y : 200 위치에 가로 50 세로 50 짜리 사각형을 그리기 위해서는 어떻게 할까?
    frame = cv2.rectangle(frame, (200, 200), (250,250), (177, 74, 33), 5, cv2.LINE_8)
    cv2.imshow("VideoFrame", frame)

capture.release() # 메모리 해제
cv2.destroyAllWindows() # 모든 윈도우 창 닫기