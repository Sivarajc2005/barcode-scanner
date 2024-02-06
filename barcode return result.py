import cv2
from pyzbar import pyzbar
bar=False
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    barcodes=pyzbar.decode(frame)
    for barcode in barcodes:
        
        (x,y,w,h)=barcode.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        barcode_value = barcode.data.decode("utf-8")
        print(barcode_value)
        
        cv2.putText(frame,barcode_value,(x,y - 10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2 )
        bar=True
    if bar:
        break
                
    cv2.imshow("Barcode Scanner",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()