import cv2
import numpy as np
import time
camera=cv2.VideoCapture(0)
print("System is preparing, please wait...")
time.sleep(2)

print("background is saving! please step out of the camera's view for 3 seconds...")
time.sleep(3)
for i in range(30):
    success,background=camera.read()

background=cv2.flip(background,1)
print("Background is saved, you can step in camera's view.")
while True:
    success,frame=camera.read()
    if not success:
        break
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_color=np.array([90,50,50])
    upper_color=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower_color,upper_color)
    mask_inv=cv2.bitwise_not(mask)
    bg_part=cv2.bitwise_and(background,background,mask=mask)
    frame_part=cv2.bitwise_and(frame,frame,mask=mask_inv)
    last_image=cv2.add(bg_part,frame_part)
    cv2.imshow("visibility",last_image)
    if cv2.waitKey(1)&0xFF==27:
        break

camera.release()
cv2.destroyAllWindows()    