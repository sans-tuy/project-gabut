import cv2, os, numpy as np
from PIL import Image

def imgPath(path):
	impaths = [os.path.join(path,f) for f in os.listdir(path)]	#menyimpan seluruh path pada direktori dalam list
	faceSample = []  #list untuk menampung sample wajah
	faceIds = [] 	#list untuk menampung id wajah
	for impath in impaths:
		image = Image.open(impath).convert('L')	#mengubah gambar menjadi grayscale
		arrayImg = np.array(image,'uint8')		#mengubah gambar menjadi matrix
		faceId = int(os.path.split(impath)[-1].split('.')[0])  #mengambil id pada nama path
		faces = faceDetect.detectMultiScale(arrayImg)	#mendeteksi wajah dan mereturn 4 koordinat sekitar area wajah 
		for (x, y, w, h) in faces:
			faceSample.append(arrayImg[y:y+h, x:x+w])  #menambahkan matriks koordinat wajah sample kedalam list
			faceIds.append(faceId)	#menambahkan id wajah sample kedalam list
	return faceSample,faceIds
	
direktori = 'data wajah'	#direktori wajah yang akan ditraining
recognizer = cv2.face.LBPHFaceRecognizer_create()	#memanggil algoritma pengenalan wajah LBPH
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')	#import data wajah
Face,Id = imgPath(direktori)  #memanggil fungsi
recognizer.train(Face,np.array(Id))	#melatih sample wajah yang sudah dibuat
recognizer.write("data training/training.xml")	#menulis hasil pelatihan 
print('berhasil dilakukan training')