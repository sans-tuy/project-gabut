import cv2
cam = cv2.VideoCapture(0)  #untuk membaca video index 0 untuk webcam default bisa isi lokasi file jika ingin mengambil dari file video
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #import data pengenalan wajah
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')  #import data pengenalan mata
id_face = input('Masukkan id wajah : ')
print('mohon tunggu sebentar dalam proses pengambilan gambar')
ambilData = 0  
direktori = 'data wajah'  #lokasi menyimpan hasil perekaman wajah
while True:
	retV, frame = cam.read() #membaca video pada webcam dan menyimpanya dalam frame
	abu_abu = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #mengubah warna dari webcam yang dibaca menjadi abu-abu
	faces = face_detector.detectMultiScale(abu_abu, 1.3, 5)  #parameter(frame, scale, min neighbour)  
	eyes = eye_detector.detectMultiScale(abu_abu,1.3,5)	#scale dan min neighbor mempengaruhi akurasi dan lamanya deteksi wajah
	for (x,y,w,h) in faces:
		namaFile = str(ambilData)+str(id_face)+'.jpg'  #format nama file
		cv2.imwrite(direktori+'/'+namaFile,frame)  #membuat file
		ambilData+=1
		frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)  #membuat bingkai penanda area wajah
		for (a,b,c,d) in eyes:
			frame1 = cv2.rectangle(frame, (a,b), (a+c,b+d), (0,255,255), 2)  #membuat bingkai penanda area mata
	cv2.imshow('webcam ku',frame) #menampilkan hasil pembacaan
	if cv2.waitKey(1) & 0xFF == ord('q'):  #stop membaca webcam
		break
	elif ambilData>=30:
		break
#menghapus memori yang digunakan untuk membaca webcam 
print('pengambilan data selesai')
#membebaskan penggunaan camera dan window
cam.release()
cv2.destroyAllWindows()