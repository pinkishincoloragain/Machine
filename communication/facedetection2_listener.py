# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import numpy as np
from urllib.request import urlopen


# TODO
# 인화성 물질
# 고양이 멍멍이
# 우선순위 - 위험도 (인간 가중치)
# 물건 대비 위험도

url = "http://121.65.177.106:8091/?action=stream"
stream = urlopen(url)
buffer = b''

# loop through frames
while True:
    buffer += stream.read(4096 * 4)
    head = buffer.find(b'\xff\xd8')
    end = buffer.find(b'\xff\xd9')

    # read frame from stream
    if head > -1 and end > -1:
        jpg = buffer[head:end+2]
        buffer = buffer[end+2:]
        img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        img = cv2.flip(img,1)
    # if not status:
    #     break
    # 물체 검출
        bbox, label, conf = cv.detect_common_objects(img)

        # print(bbox, label, conf)
        # print(time.time())

        # 검출된 물체 가장자리에 바운딩 박스 그리기
        out = draw_bbox(img, bbox, label, conf, write_conf=True)
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
cv2.destroyAllWindows()
