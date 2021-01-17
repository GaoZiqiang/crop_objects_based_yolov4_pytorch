import time

import cv2
import numpy as np
from PIL import Image
from IPython import embed

from yolo import YOLO

yolo = YOLO()
#-------------------------------------#
#   调用摄像头
#   capture=cv2.VideoCapture("1.mp4")
#-------------------------------------#
capture=cv2.VideoCapture(0)# 问题出在这里，应该是没有读取进来