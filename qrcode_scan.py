import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
def scan_for_data(path):
	img=cv2.imread(path)
	FF = pyzbar.decode(img)
	for obj in FF:
		#print("Type:", obj.type)
		print(obj.data)
def scan_for_type(path):
	img=cv2.imread(path)
	FF = pyzbar.decode(img)
	for obj in FF:
		print(obj.type)
		#print("Data: ", obj.data, "\n")