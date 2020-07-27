import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('camera_test.avi', fourcc, 60.0, (640,480))

# setup initial location of window
x, y, w, h = 480, 0, 160, 300  # simply hardcoded the values
track_window = (x, y, w, h)

while (1):
    ret, frame = cap.read()

    if ret:
        # Draw it on image
        x, y, w, h = track_window
    	cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0, 0), 5)
    	dst = np.zeros_like(frame)
    	dst[y:y+h,x:x+w] = frame[y:y+h,x:x+w]
        out.write(dst)
    	cv2.imshow('Record', dst)
      
        if cv2.waitKey(1) & 0xFF == 27:
            break;
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
