import cv2

stream = "rtsp://admin:admin@192.168.0.106:1935"

cap = cv2.VideoCapture(stream, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("Cannot open stream")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Drone Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()