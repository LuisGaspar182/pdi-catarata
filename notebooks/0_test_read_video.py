import cv2
vid = cv2.VideoCapture('data/raw_videos/VIDEO-2025-10-13-18-42-18.mp4')
ret, frame = vid.read()
if ret:
    print("frame shape:", frame.shape)
    cv2.imwrite('results/frame0.png', frame)
vid.release()
