import cv2
import numpy as np

stream = "rtsp://admin:admin@192.168.0.106:1935"

cap = cv2.VideoCapture(stream)

net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

CLASSES = [
    "background","aeroplane","bicycle","bird","boat",
    "bottle","bus","car","cat","chair","cow","diningtable",
    "dog","horse","motorbike","person","pottedplant",
    "sheep","sofa","train","tvmonitor"
]

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    frame = cv2.resize(frame, (600, 400))

    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300,300), 127.5)

    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]

        if confidence > 0.5:
            idx = int(detections[0,0,i,1])

            box = detections[0,0,i,3:7] * np.array([600,400,600,400])
            (startX,startY,endX,endY) = box.astype("int")

            label = f"{CLASSES[idx]} {confidence:.2f}"

            cv2.rectangle(frame,(startX,startY),(endX,endY),(0,255,0),2)
            cv2.putText(frame,label,(startX,startY-5),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()