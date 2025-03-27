import cv2
import cv2.data
cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
body_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_fullbody.xml")
while True:
    _,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.3,5)
    for(x, y , w , h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("camera",frame)
    if cv2.waitKey(1)==ord("q")==ord("Q"):
        break
cap.release()
cv2.destroyAllWindows