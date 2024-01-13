# 76 105 109 101 33 - 1001100 1101001 1101101 100001
import cv2
import numpy as np

src = np.zeros((768, 1366, 3), dtype=np.uint8)

src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA) # 직선 (시작점 , 종점 , 색 ,테두리 두께 , 종류)
src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4) # 원 ( 시작점, 반지름,색 , 전부 채우기, 종류)
src = cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)# 사각형 (시작점 , 종점 , 색, 테두리,종류)
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2) # 타원 (시작 , 종점, 타원 각도 , 색)

pts1 = np.array([[100, 500], [300, 500], [200, 600]]) #역삼각형 꼭짓점 위치
pts2 = np.array([[600, 500], [800, 500], [700, 600]]) #역삼각형 위와 같음
src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2) # 위와 같음 , 마지막 선의 존재 여부,색 ,테두리
src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA) # 꼭짓점 위치 , 색 

#src = cv2.putText(src, "YUNDAEHEE", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3) 
# YUNDAEHEE 글자 출력

cv2.imshow("src", src)
cv2.waitKey() # 키 기다리기
cv2.destroyAllWindows() # 모든 윈도우 창 닫기