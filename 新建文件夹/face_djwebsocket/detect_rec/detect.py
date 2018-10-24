# -*- coding: utf-8 -*-
# 利用开源库face_recognition进行人脸检测及识别

import face_recognition
import cv2
import time

class facerec(object):

    def pridict(self, img):

        # 若输入为图像路径
    #    frame = face_recognition.load_image_file(img)

        # 若输入为图像数组
        frame = img
        known_image = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        aa = time.time()
        face_locations = face_recognition.face_locations(known_image)
        ab = time.time()
        print("检测人脸时间", ab - aa)

        for (top, right, bottom, left) in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),  2)

        return frame

if __name__ == '__main__':
    img ="ceshi.png"
    img1 = "duoren.jpg"
    a = time.time()
    face = facerec()
    b = time.time()
    face.pridict(img1)
    c = time.time()
    face.pridict(img)
    d = time.time()
    print(b-a, c-b, d-c)