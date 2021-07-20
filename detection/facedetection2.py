# import necessary packages
import cvlib as cv
import asyncio
import websockets
from cvlib.object_detection import draw_bbox
import cv2

# 웹캠 열기
webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Could not open webcam")
    exit()


# 비동기로 서버에 접속
async def connect():
    # 웹 소켓에 접속
    async with websockets.connect("ws://210.204.38.78:8080/python") as websocket:
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
                    num += 1
            #print(num)

            await websocket.send(str(num))

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
