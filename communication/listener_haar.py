import cv2
import numpy as np
from urllib.request import urlopen

url = "http://121.65.177.49:8091/?action=stream"
stream = urlopen(url)
buffer = b''

xml = 'data/haarcascades/haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(xml)

while True:
    buffer += stream.read(4096*4)
    head = buffer.find(b'\xff\xd8')
    end = buffer.find(b'\xff\xd9')

    if head > -1 and end > -1:
        jpg = buffer[head:end+2]
        buffer = buffer[end+2:]
        img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        print("Number of faces detected: " + str(len(faces)))

        if len(faces):
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("stream", img)




    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()