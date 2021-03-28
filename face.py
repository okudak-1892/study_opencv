# -*- coding: utf-8 -*-
import cv2

if __name__ == '__main__':
   
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "org"
    GAUSSIAN_WINDOW_NAME = "result"

    DEVICE_ID = 0

    # 分類器の指定
    cascade_file = "haarcascade_frontalface_alt2.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    # カメラ映像取得
    cap = cv2.VideoCapture(DEVICE_ID)

    # 初期フレームの読込
    end_flag, c_frame = cap.read()
    height, width, channels = c_frame.shape

    # ウィンドウ準備
    cv2.namedWindow(ORG_WINDOW_NAME)
    cv2.namedWindow(GAUSSIAN_WINDOW_NAME)

    while end_flag == True:

        # 画像の取得と顔の検出
        img = c_frame
        _, frame = cap.read()
        face_list = cascade.detectMultiScale(img, minSize=(100, 100))

        # 検出した顔を囲む
        for (x, y, w, h) in face_list:
            color = (0, 0, 225)
            pen_w = 3
            cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)

        #originalの反転
        original = cv2.flip(img, 1)
        cv2.imshow('Inversion', original)

        # Escキーで終了
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        # 次のフレーム読み込み
        end_flag, c_frame = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()
