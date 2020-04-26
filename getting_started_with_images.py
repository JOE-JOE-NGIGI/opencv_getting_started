import cv2

# to read from file, you can  give the file name in place of 0
cap = cv2.VideoCapture(0); #or -1 1 for second cam

while (True):
    ret, frame = cap.read() #return true if frame is available

    #change to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    #Use keyboard character 'q' to terminate
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
