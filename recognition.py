import threading

import cv2
from deepface import DeepFace

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False

reference_img = cv2.imread("img0.jpeg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False

    except ValueError:
        face_match = False

while True:
    return_v, frame = capture.read()

    if return_v:
        if counter % 30 == 0:
            try:
                threading.Thread(target= check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "Match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
        else:
            cv2.putText(frame, "Not Match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()