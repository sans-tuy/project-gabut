import cv2, os, numpy as np
cam = cv2.VideoCapture(0)  #untuk membaca video index 0 untuk webcam default bisa isi lokasi file jika ingin mengambil dari file video
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')	#import data pengenalan wajah

direktori = 'data training'	#direktori data training
recognizer = cv2.face.LBPHFaceRecognizer_create()	#memanggil algoritma pengenalan wajah
recognizer.read(direktori+'/training.xml')	#membuka hasil pembelajaran model ML
id = 0
dbWajah = ['tidak diketahui','fauzi','sanusi']	#list nama wajah yang terdaftar
font = cv2.FONT_HERSHEY_SIMPLEX	#font teks 

while True:
	retV, frame = cam.read() #membaca video pada webcam dan menyimpanya dalam frame
	frame = cv2.flip(frame,1)
	abu_abu = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #mengubah warna dari webcam yang dibaca menjadi abu-abu
	faces = face_detector.detectMultiScale(abu_abu, 1.3, 5)
	for (x,y,w,h) in faces:
		frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
		Id,prediksi = recognizer.predict(abu_abu[y:y+h,x:x+w])
		if int(str(Id)[-1]) == 1 and 100-prediksi > 50:
			teksPredict = "{0}%".format(round(100-prediksi))
			nama = dbWajah[1]
		elif int(str(Id)[-1]) == 2 and 100-prediksi > 50:
			teksPredict = "{0}%".format(round(100-prediksi))
			nama = dbWajah[2]
		else:
			teksPredict = "{0}%".format(round(100-prediksi))
			nama = dbWajah[0]
		cv2.putText(frame, nama, (x+5,y+5), font, 1, (0,255,0), 2)
		cv2.putText(frame, teksPredict, (x+w,y+h), font, 1, (0,0,255), 2)

		print("id = {0}".format(Id))

	cv2.imshow('webcam ku',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):  #stop membaca webcam
		break
#membebaskan penggunaan camera dan window
cam.release()
cv2.destroyAllWindows()