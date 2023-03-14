import cv2
import sys, os.path

class picToAscii():

	def __init__(self, argv):
		#to lazy to flip entire string in reverse
		res = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.          "
		self.res = res[::-1]
		self.name = argv

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
	def toAscii(self):
		image = cv2.imread(f"{self.name}")
		image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	

# cv2.imshow("hi",image)
# cv2.waitKey(0)

		x = image.shape[0]
		y = image.shape[1]

		a = 15 #ascii image res

		fileOut = open(f'{self.name[:-4]}_ascii.txt','w') #opens file

		#prints to file by pixel intensity
		for i in range(0,x,a):
			for j in range(0,y,a):
				inte = int(image[i,j])
				#print(f"{self.res[self.per(inte,len(self.res))]}",file = fileOut, end = " ")
				print(f"{self.res[self.per(inte,len(self.res))]}", end = " ")
			#print("",file = fileOut)
			print("")

		fileOut.close()

	def main(self):
		if(self.check()):
			self.toAscii()

if __name__ == "__main__":
	argv = sys.argv[1]
	a = picToAscii(argv)
	a.main()