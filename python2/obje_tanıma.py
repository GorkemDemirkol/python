import cv2
import torch
from ultralytics import YOLO

devaice = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def main():
    model=YOLO('yolo11n.pt')
    model.to(devaice)

    #video yakalama 0,default camera
    cap=cv2.VideoCapture(0)

    #cihaz açık mı kapal mı kontrol et
    if not cap.isOpened():
        print("Kamera kapalı durumda.")
        return
    while True:
        #Çerçeve yakala
        ret, frame=cap.read()
        if not ret:
            print("HATA!! çerçeve okunamadı.")
            break
        result=model(frame)
        #sonuçları işleme
        for result in result:
            for box in result.boxes:
                #box koordinatları
               x1,y1,x2,y2=box.xyxy[0]
               label_id=int(box.cls[0].item())
               conf=box.conf[0].item()
               #Başlığı yolodan alma
               class_label=model.names[label_id]
               #Başlığı text olarak ekleme
               label_text=f"{class_label} {conf:.2f}"
               cv2.rectangle(frame,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
               cv2.putText(frame,label_text,(int(x1),int(y1)-5),(cv2.FONT_HERSHEY_COMPLEX),0.5,(0,255,0),1)
               
        #Çerçeveyi çizdirme
            cv2.imshow("Çerçeve",frame)
        #Q ya bsıldığında kapansın
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()