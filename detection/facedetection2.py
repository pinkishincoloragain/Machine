# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import time

# TODO
# 인화성 물질
# 고양이 멍멍이
# 우선순위 - 위험도 (인간 가중치)
# 물건 대비 위험도

# 웹캠 열기
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()

# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()

    if not status:
        break
    # 물체 검출
    bbox, label, conf = cv.detect_common_objects(frame)

    # print(bbox, label, conf)
    # print(time.time())

    # 검출된 물체 가장자리에 바운딩 박스 그리기
    out = draw_bbox(frame, bbox, label, conf, write_conf=True)

    num = 0
    for item in label:
        if item == "person":
            num+=1
    print(num)

    # 디스플레이
    cv2.imshow("Real-time object detection", out)

    # Q 누르면 정지
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()