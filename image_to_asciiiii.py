import cv2
import sys, os.path

class picToAscii():

	def __init__(self, argv, c):
		#to lazy to flip entire string in reverse
		res = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.          "
		self.res = res[::-1]
		self.name = argv
		self.clar = c

# usage = "python3 image_to_asciiiii.py [*.png]"
# argv = sys.argv[1]

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

#opens the image and converts to black and white
	def toAscii_BlackWhite(self):
		image = cv2.imread(f"{self.name}")
		image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

		x = image.shape[0]
		y = image.shape[1]

		 #ascii image res

		fileOut = open(f'{self.name[:-4]}_ascii.txt','w') #opens file

		#prints to file by pixel intensity
		for i in range(0,x,self.clar):
			for j in range(0,y,self.clar):
				inte = int(image[i,j])
				#print(f"{self.res[self.per(inte,len(self.res))]}",file = fileOut, end = " ")
				print(f"{self.res[self.per(inte,len(self.res))]}", end = " ")
			#print("",file = fileOut)
			print("")

		fileOut.close()

	def main(self):
		if(self.check()):
			self.toAscii_BlackWhite()

if __name__ == "__main__":
	argv_file = sys.argv[1]
	argv_clar = int(sys.argv[2])
	a = picToAscii(argv_file, argv_clar)
	a.main()