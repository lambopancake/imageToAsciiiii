import cv2
import sys, os.path

class picToAscii():

	def __init__(self ,c , argv = None):
		#to lazy to flip entire string in reverse
		res = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.             "
		self.res = res[::-1]
		self.name = argv
		self.clar = c


	def per(self,inte, resLen):
		return int((inte/255.0)* 100 * ((resLen-1)*0.01)) 


	#Checks if the file exist
	def check(self):
		usage = "python3 image_to_asciiiii.py [*.png]"
		if(not(os.path.isfile(f"./{self.name}"))):
			print(usage)
			print("no such file")
			return False
		return True

	def RGBToHEX(self,r,g,b):
		num = "0123456789abcdef"
		hexCode = ""


	#opens the image and converts to black and white
	def toAscii_BlackWhite(self, pic, f = 0, toFile = 0):
		if(f == 1):
			image = cv2.imread(f"{pic}")
		else:	
			image = pic
		imageBW = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

		x = image.shape[0]
		y = image.shape[1]

		 #ascii image res
		if(f == 1):
			fileOut = open(f'{self.name[:-4]}_ascii.txt','w') #opens file

		#prints to file by pixel intensity
		for i in range(0,x,self.clar):
			for j in range(0,y,self.clar):
				inte = int(imageBW[i,j])
				if(toFile == 1):
					print(f"{self.res[self.per(inte,len(self.res))]}",file = fileOut, end = " ")
				else:
					print(f"{self.res[self.per(inte,len(self.res))]}", end = " ")
			if(toFile == 1):
				print("",file = fileOut)
			else:
				print("")
		if(f == 1):
			fileOut.close()

	def main(self):
		if(self.check()):
			self.toAscii_BlackWhite(self.name, f = 1)

if __name__ == "__main__":
	argv_file = sys.argv[1]
	argv_clar = int(sys.argv[2])
	a = picToAscii(argv_clar, argv_file)
	a.main()