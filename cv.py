import cv2 # 패키지명 : opencv-python
import numpy as np

image_path = "output.png"
image_array = cv2.imread((image_path)) #cv2영상처리 패키지

#imread : image read (이미지 경로) image_array에 데이터 저장
print(image_array)
print(image_array.shape)
print(image_array.size)
height, width,_ = image_array.shape
print(height)
print(width)
# print(_)
# widthhalf = width//2
# image_array[:,:widthhalf] = [0,0,0]
cv2.imshow("image result", image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()
# x = 1
# y = 1
# pix_v = image_array[y,x] #1,1 픽셀의 B값 출력
# print("value",pix_v) # 특정 RBG 값을 가져오는데 RGB가 아닌 BGR 순서로 가져온다.

#opencv로 불러온 이미지는 numpy배열 형태의 픽셀에 해당하는 B G R 값을 가진다.
