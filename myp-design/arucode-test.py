import numpy as np
import cv2
import cv2.aruco as aruco
import cameratools as ct


# image = cv2.imread("c:/Users/pab/Desktop/arucodes.jpg")
camera = ct.Camera(0)
image = camera.take_photo()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
parameters = aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict, parameters=parameters)
# print("corners")
# print(corners)
print("ids")
print(ids)
# print("rejects")
# print(rejectedImgPoints)
# aruco.drawDetectedMarkers(image, corners, borderColor=(50, 0, 120))
# aruco.drawDetectedMarkers(image, rejectedImgPoints, borderColor=(100, 0, 240))
# aruco.drawDetectedMarkers(image, rejectedImgPoints)
# cv2.imshow('gray_im', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
