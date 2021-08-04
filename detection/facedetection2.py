# import necessary packages
import cvlib as cv
import asyncio
import websockets
from cvlib.object_detection import draw_bbox
import cv2
from calculation import Calc

from tensorflow.python.client import device_lib
device_lib.list_local_devices()

# TODO
# 인화성 물질
# 고양이 멍멍이
# 우선순위 - 위험도 (인간 가중치)
# 물건 대비 위험도

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


# 비동기로 서버에 접속
async def connect():
    # 웹 소켓에 접속
    async with websockets.connect("ws://ec2-52-78-90-230.ap-northeast-2.compute.amazonaws.com:8080/ws") as websocket:
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

            person_num = 0

            all_items = []
            for item in label:
                if item == "person":
                    person_num += 1
                all_items.append(item)

            # print(f"number of people : {person_num}", end=" ")
            # print(f"Flammable score : {Calc.flame_score(0,all_items)}")

            await websocket.send(str(person_num) + " " + str(Calc.flame_score(0, all_items)))

            data = await websocket.recv()

            print(data)

            # 디스플레이
            cv2.imshow("Real-time object detection", out)

            # Q 누르면 정지
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

asyncio.run(connect())

# release resources
webcam.release()
cv2.destroyAllWindows()
