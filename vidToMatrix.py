import cv2,os,time
from image_to_asciiiii import picToAscii




if __name__ == "__main__":
	vid = cv2.VideoCapture(0)
	i = 0
	os.system('cls')
	while i < 100:
		
		time.sleep(0.01)
		
		os.system("clear")

		frame = vid.read()[1]
		blackAndWhite = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		a = picToAscii(15)
		a.toAscii_BlackWhite(frame)
	


		key = cv2.waitKey(20)
		if key == 27: #hit esc to quit
			break
		i += 1

	vid.release()
	#cv2.destroyWindow()
