import numpy as np
import cv2

cascade_src = 'cars.xml'
# video = 'data/Cars_On_Highway.mp4'
video = 'data/video1.avi'
# video = 'data/video2.avi'

def detectCars(filename):
    rectangle = []
    cascade = cv2.CascadeClassifier(cascade_src)

    vc = cv2.VideoCapture(filename)

    if not vc.isOpened():
        print(f"Error: Could not open video file {filename}")
        return

    frame_count = 0
    skip_frames = 2  # Process every 3rd frame

    while True:
        rval, frame = vc.read()
        if not rval:
            break

        frame_count += 1
        if frame_count % skip_frames != 0:
            continue

        # frameHeight, frameWidth, fdepth = frame.shape

        # Resize
        frame = cv2.resize(frame, (700, 400))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Haar detection
        cars = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Show result
        cv2.imshow("Result", frame)

        if cv2.waitKey(30) == ord('q'):  # Adjusted to process frames at a more appropriate rate
            break

    vc.release()
    cv2.destroyAllWindows()

detectCars(video)
