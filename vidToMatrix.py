import cv2,os,time
from image_to_asciiiii import picToAscii




if __name__ == "__main__":
	vid = cv2.VideoCapture(0)
	i = 0
	os.system('cls')
	while True:
		
		time.sleep(0.01)
		os.system("cls")
		
		# os.system("clear")
		# os.system("clear")os.system("clear")

		frame = vid.read()[1]
		
		blackAndWhite = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		a = picToAscii(10)  #make this parameter smaller the resolution increases
							#make it greater it decreases
		a.toAscii_BlackWhite(frame)
	
		
		key = cv2.waitKey(20)
		if key == 27: #hit esc to quit
			break
		i += 1

	vid.release()
	#cv2.destroyWindow()
