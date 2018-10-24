from django.shortcuts import render
from dwebsocket.decorators import accept_websocket, require_websocket
import numpy as np
import cv2
from detect_rec import detect
from detect_rec import recognition
from create_newdir import createdir
import random

def index(request):
    return render(request, 'zhuye.html')
def index1(request):
    return render(request, 'caiji.html')
def index2(request):
    return render(request, 'jiance.html')
def index3(request):
    return render(request, 'shibie.html')

@accept_websocket
def echo2(request):
    global message_part1, message_part2
    while True:
        message1 = request.websocket.wait()
        if message1==None:
                pass
        else:
            a = message1.find(b'\xff\xd8' )
            b = message1.find(b'\xff\xd9' )
            if a != -1 and b != -1:      # 能找到上述字符
                jpg = message1[a:b+2]
                imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                imghtml = cv2.imencode('.jpg', imgweb)[1].tostring()
                request.websocket.send(imghtml)
            else:
                if a != -1 and b == -1:  # 字符前半段
                    message_part1 = message1

                if a == -1 and b != -1:  # 字符后半段
                    message_part2 = message1
                    message = message_part1 + message_part2
                    a = message.find(b'\xff\xd8' )
                    b = message.find(b'\xff\xd9' )
                    if a != -1 and b != -1:      # 能找到上述字符
                        jpg = message[a:b+2]
                        imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        imghtml = cv2.imencode('.jpg', imgweb)[1].tostring()
                        request.websocket.send(imghtml)


@accept_websocket
def caiji(request):
    global message_part1, message_part2, path
    while True:
        message1 = request.websocket.wait()
        if message1==None:
                pass
        else:
            a = message1.find(b'\xff\xd8' )
            b = message1.find(b'\xff\xd9' )
            if a != -1 and b != -1:      # 能找到上述字符
                jpg = message1[a:b+2]
                #  写入二进制数据
                number = random.randint(0,10000)
                f = open(path +"/"+str(number)+".jpg","wb")
                f.write(jpg)
                f.close()
                imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                imghtml = cv2.imencode('.jpg', imgweb)[1].tostring()
                request.websocket.send(imghtml)
            else:
                if a == -1 and b == -1:
                    dirname = message1.decode('ascii')
                    path = "./dataset/"+dirname
                    createdir.mkdir(path)
                if a != -1 and b == -1:  # 找到图像前半段
                    message_part1 = message1
                if a == -1 and b != -1:  # 找到图像后半段
                    message_part2 = message1
                    message = message_part1 + message_part2
                    a = message.find(b'\xff\xd8' )
                    b = message.find(b'\xff\xd9' )
                    if a != -1 and b != -1:      # 能找到上述字符
                        jpg = message[a:b+2]
                        #  写入二进制数据
                        number = random.randint(0,10000)
                        f = open(path +"/"+str(number)+".jpg","wb")
                        f.write(jpg)
                        f.close()
                        imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        imghtml = cv2.imencode('.jpg', imgweb)[1].tostring()
                        request.websocket.send(imghtml)

@accept_websocket
def jiance(request):
    global message_part1, message_part2
    face = detect.facerec()
    while True:
        message1 = request.websocket.wait()
        print("到这")
        if message1==None:
                pass
        else:
            a = message1.find(b'\xff\xd8' )
            b = message1.find(b'\xff\xd9' )
            if a != -1 and b != -1:      # 能找到上述字符
                jpg = message1[a:b+2]
                imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                print("检测一")
                img = face.pridict(imgweb)
                imghtml = cv2.imencode('.jpg', img)[1].tostring()
                request.websocket.send(imghtml)
            else:
                if a != -1 and b == -1:  # 字符前半段
                    message_part1 = message1
                if a == -1 and b != -1:  # 字符后半段
                    message_part2 = message1
                    message = message_part1 + message_part2
                    a = message.find(b'\xff\xd8' )
                    b = message.find(b'\xff\xd9' )
                    if a != -1 and b != -1:      # 能找到上述字符
                        jpg = message[a:b+2]
                        imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        print("检测二")
                        img = face.pridict(imgweb)
                        imghtml = cv2.imencode('.jpg', img)[1].tostring()
                        request.websocket.send(imghtml)

@accept_websocket
def shibie(request):
    global message_part1, message_part2
    face = recognition.facerec()
    while True:
        message1 = request.websocket.wait()
        print("到这")
        if message1==None:
                pass
        else:
            a = message1.find(b'\xff\xd8' )
            b = message1.find(b'\xff\xd9' )
            if a != -1 and b != -1:      # 能找到上述字符
                jpg = message1[a:b+2]
                imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                print("识别一")
                img = face.pridict(imgweb)
                imghtml = cv2.imencode('.jpg', img)[1].tostring()
                request.websocket.send(imghtml)
            else:
                if a != -1 and b == -1:  # 字符前半段
                    message_part1 = message1
                if a == -1 and b != -1:  # 字符后半段
                    message_part2 = message1
                    message = message_part1 + message_part2
                    a = message.find(b'\xff\xd8' )
                    b = message.find(b'\xff\xd9' )
                    if a != -1 and b != -1:      # 能找到上述字符
                        jpg = message[a:b+2]
                        imgweb = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        print("识别二")
                        img = face.pridict(imgweb)
                        imghtml = cv2.imencode('.jpg', img)[1].tostring()
                        request.websocket.send(imghtml)

