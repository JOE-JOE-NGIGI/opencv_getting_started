import cv2

# to read from file, you can  give the file name in place of 0
cap = cv2.VideoCapture(1); #or -1 1 for second cam

while (True):
    ret, frame = cap.read() #retirn true if frame is available
    #change to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
