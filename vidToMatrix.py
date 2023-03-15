import cv2
from os import system 
from time import sleep
from image_to_asciiiii import picToAscii




if __name__ == "__main__":
	vid = cv2.VideoCapture(0)
	i = 0
	system('cls')
	while True:
		
		sleep(0.01)
		system("cls")
		
		# os.system("clear")
		# os.system("clear")os.system("clear")

		frame = vid.read()[1]
		
		#blackAndWhite = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		a = picToAscii(8)  #make this parameter smaller the resolution increases
							#make it greater it decreases
		a.toAscii_BlackWhite(frame)
	
		
		key = cv2.waitKey(20)
		if key == 27: #hit esc to quit
			break
		i += 1

	vid.release()