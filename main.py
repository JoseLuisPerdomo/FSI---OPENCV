import cv2

video = cv2.VideoCapture("people_walking.mp4")

while 1:

    _, frame_color = video.read()

    if not _:
        break

    frame_display = frame_color.copy()

    frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', frame_display)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
