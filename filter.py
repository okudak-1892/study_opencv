# -*- coding: utf-8 -*-
import cv2

def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)


if __name__ == '__main__':

    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # 待ち時間
    FRAME_RATE = 30  # fps

    ORG_WINDOW_NAME = "org"
    GAUSSIAN_WINDOW_NAME = "gaussian"

    GAUSSIAN_FILE_NAME = "gaussian.avi"

    DEVICE_ID = 0

    cap = cv2.VideoCapture(DEVICE_ID)

    # 保存ビデオファイルの準備
    end_flag, c_frame = cap.read()
    height, width, channels = c_frame.shape
    rec = cv2.VideoWriter(GAUSSIAN_FILE_NAME, \
                          cv_fourcc('X', 'V', 'I', 'D'), \
                          FRAME_RATE, \
                          (width, height), \
                          True)

    # ウィンドウ準備
    cv2.namedWindow(ORG_WINDOW_NAME)
    cv2.namedWindow(GAUSSIAN_WINDOW_NAME)

    while end_flag == True:
        # ガウシアンフィルタ
        g_frame = cv2.GaussianBlur(c_frame, (15, 15), 10)

        # 表示
        cv2.imshow(ORG_WINDOW_NAME, c_frame)
        cv2.imshow(GAUSSIAN_WINDOW_NAME, g_frame)

        #originalの反転
        original = cv2.flip(g_frame, 1)
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
