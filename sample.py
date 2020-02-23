import cv2

cap = cv2.VideoCapture(0)
print("exposure : ", cap.get(cv2.CAP_PROP_EXPOSURE))
#print(cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0))
#print(cap.set(cv2.CAP_PROP_EXPOSURE, 5))
#print("exposure : ", cap.get(cv2.CAP_PROP_EXPOSURE))

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
    frame = cv2.flip(frame, 1)

    sub_frame = frame
    chaged_frame = cv2.Canny(frame, 50, 110)
    cv2.putText(sub_frame, 'Exit:Press ESC key', (0,50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255,0), 3, cv2.LINE_AA)
    cv2.imshow('input image', sub_frame)


    #chaged_frame = cv2.Canny(frame, 50, 110)

    cv2.imshow('Edge image', chaged_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
