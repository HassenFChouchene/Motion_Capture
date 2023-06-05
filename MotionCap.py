import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('Video.mp4')


detector = PoseDetector()
poseList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList,bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ' '
        for lm in lmList:
            lmString+=f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'
        poseList.append(lmString)
    print(lmString)

    cv2.imshow("Image", img)
    key = cv2.waitKey(100)
    if key ==ord('s'):
        with open("AnimationFile.txt",'w') as f:
            f.writelines(["%s\n" % item  for item in poseList])

