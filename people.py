# -*- coding: UTF-8 -*-
# 人の認識
import cv2
import os

f_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_fullbody.xml')

# カメラの起動
cap = cv2.VideoCapture(0)

while(True):

    # 動画ストリームからフレームを取得
    ret, frame = cap.read()
    # original = cv2.flip(frame, 1)
    # cv2.imshow('Inversion', original)

    #物体認識（人）の実行
    facerect = f_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    
    #検出した人を囲む矩形の作成
    for rect in facerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), (0, 0, 255), thickness=2)
        
        text = 'person'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,text,(rect[0],rect[1]-10),font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        
    # 表示
    cv2.imshow("Show FLAME Image", frame) 

    # qを押したら終了。
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
